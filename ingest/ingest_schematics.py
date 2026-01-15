import os
from datetime import datetime
from core.parser import parse_schematic
from core.db import get_connection, create_table, insert_or_update
from config import SCH_FILES_FOLDER, SCH_FILES_TABLE


def ingest_schematics():
    conn = get_connection()
    create_table(conn, SCH_FILES_TABLE)

    summary = []

    for file in os.listdir(SCH_FILES_FOLDER):
        if file.endswith(".kicad_sch"):
            file_path = os.path.join(SCH_FILES_FOLDER, file)
            try:
                data = parse_schematic(file_path)
                data["ingested_at"] = datetime.now().isoformat()

                insert_or_update(conn, SCH_FILES_TABLE, data)

                summary.append((file, "SUCCESS"))
            except Exception as e:
                summary.append((file, f"ERROR: {e}"))

    conn.close()
    return summary
