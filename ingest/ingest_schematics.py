import os
from datetime import datetime
from core.parser import parse_schematic
from core.db import get_connection, create_table, insert_or_update
from config import SCH_FILES_FOLDER, SCH_FILES_TABLE
from core.path_utils import to_virtual_path          
from config import SCH_FILES_FOLDER, SCH_FILES_TABLE, DATA_DIR  


def ingest_schematics():
    conn = get_connection()
    create_table(conn, SCH_FILES_TABLE)

    summary = []

    for file in os.listdir(SCH_FILES_FOLDER):
        if file.endswith(".kicad_sch"):
            file_path = os.path.join(SCH_FILES_FOLDER, file)
            virtual_path = to_virtual_path(abs_path, DATA_DIR)
            try:
                data = parse_schematic(file_path)
                data["ingested_at"] = datetime.now().isoformat()
                 data["filepath"] = virtual_path

                insert_or_update(conn, SCH_FILES_TABLE, data)

                summary.append((file, "SUCCESS"))
            except Exception as e:
                summary.append((file, f"ERROR: {e}"))

    conn.close()
    return summary
