import os
from datetime import datetime
from core.parser import parse_footprint
from core.db import get_connection, create_table, insert_or_update
from config import FOOTPRINTS_FOLDER, FOOTPRINTS_TABLE

def ingest_footprints():
    # Open DB connection
    conn = get_connection()
    create_table(conn, FOOTPRINTS_TABLE)

    summary = []

    #  Walk through all subfolders recursively
    for root, dirs, files in os.walk(FOOTPRINTS_FOLDER):
        for file in files:
            if file.endswith(".kicad_mod"):
                file_path = os.path.join(root, file)

                try:
                    # Parse the footprint
                    data = parse_footprint(file_path)
                    data["ingested_at"] = datetime.now().isoformat()

                    # Insert or update in DB
                    insert_or_update(conn, FOOTPRINTS_TABLE, data)

                    summary.append((file, "SUCCESS"))
                except Exception as e:
                    summary.append((file, f"ERROR: {e}"))

    # Close DB connection
    conn.close()
    return summary
