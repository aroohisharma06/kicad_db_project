import os
from datetime import datetime
from core.parser import parse_footprint
from core.db import get_connection, create_table, insert_or_update
from config import FOOTPRINTS_FOLDER, FOOTPRINTS_TABLE, DATA_DIR
from core.path_utils import to_virtual_path

def ingest_footprints():
    conn = get_connection()
    create_table(conn, FOOTPRINTS_TABLE)

    summary = []

    for root, dirs, files in os.walk(FOOTPRINTS_FOLDER):
        for file in files:
            if file.endswith(".kicad_mod"):
                abs_path = os.path.abspath(os.path.join(root, file))

                # ✅ convert to virtual path
                virtual_path = to_virtual_path(abs_path, DATA_DIR)

                try:
                    data = parse_footprint(abs_path)
                    data["ingested_at"] = datetime.now().isoformat()

                    # ✅ store virtual path
                    data["file_path"] = virtual_path

                    insert_or_update(conn, FOOTPRINTS_TABLE, data)
                    summary.append((file, "SUCCESS"))

                except Exception as e:
                    summary.append((file, f"ERROR: {e}"))

    conn.close()
    return summary

