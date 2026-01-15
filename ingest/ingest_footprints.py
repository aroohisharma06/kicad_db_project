import os
from datetime import datetime
from core.parser import parse_footprint
from core.db import get_connection, create_table, insert_or_update
from config import FOOTPRINTS_FOLDER, FOOTPRINTS_TABLE

def ingest_footprints():
    conn = get_connection()
    create_table(conn, FOOTPRINTS_TABLE)

    summary = []

    for root, dirs, files in os.walk(FOOTPRINTS_FOLDER):
        for file in files:
            if file.endswith(".kicad_mod"):
                file_path = os.path.join(root, file)

                # ✅ ONLY filename (no path)
                display_name = os.path.basename(file_path)

                try:
                    data = parse_footprint(file_path)
                    data["ingested_at"] = datetime.now().isoformat()

                    insert_or_update(conn, FOOTPRINTS_TABLE, data)
                    summary.append((display_name, "SUCCESS"))

                except Exception as e:
                    summary.append((display_name, f"ERROR: {e}"))

    conn.close()
    return summary
