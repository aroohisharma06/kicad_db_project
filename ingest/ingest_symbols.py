import os
from datetime import datetime
from core.parser import parse_symbol
from core.db import get_connection, create_table, insert_or_update
from config import SYMBOLS_FOLDER, SYMBOLS_TABLE


def ingest_symbols():
    conn = get_connection()
    create_table(conn, SYMBOLS_TABLE)

    summary = []

    for file in os.listdir(SYMBOLS_FOLDER):
        if file.endswith(".kicad_sym"):
            file_path = os.path.join(SYMBOLS_FOLDER, file)
            try:
                data = parse_symbol(file_path)
                data["ingested_at"] = datetime.now().isoformat()

                insert_or_update(conn, SYMBOLS_TABLE, data)

                summary.append((file, "SUCCESS"))
            except Exception as e:
                summary.append((file, f"ERROR: {e}"))

    conn.close()
    return summary
