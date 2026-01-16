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

    if not os.path.exists(FOOTPRINTS_FOLDER):
        print(f"❌ Error: Folder not found at {os.path.abspath(FOOTPRINTS_FOLDER)}")
        return summary
   
    # Walk through all subfolders recursively
    for root, dirs, files in os.walk(FOOTPRINTS_FOLDER):
        for file in files:
            if file.endswith(".kicad_mod"):
                # This is the absolute path used for reading the file
                file_path = os.path.join(root, file)

                try:
                    # Parse the footprint
                    data = parse_footprint(file_path)
                    
                    # --- CONVERSION START ---
                    # Convert absolute file_path to a virtual (relative) path
                    # This removes the FOOTPRINTS_FOLDER prefix
                    virtual_path = os.path.relpath(file_path, FOOTPRINTS_FOLDER)
                    
                    # Update the data dictionary with the virtual path
                    # (Assuming your parser or DB schema uses a key like 'path' or 'filepath')
                    data["filepath"] = virtual_path 
                    # --- CONVERSION END ---

                    print(f"Testing Path: {file} -> {virtual_path}")

                    data["ingested_at"] = datetime.now().isoformat()

                    # Insert or update in DB
                    insert_or_update(conn, FOOTPRINTS_TABLE, data)
                    summary.append((file, "SUCCESS"))
                except Exception as e:
                    summary.append((file, f"ERROR: {e}"))
    # Close DB connection
    conn.close()
    return summary
    
if __name__ == "__main__":
    print("--- DEBUG: Starting Footprint Ingestion Test ---")
    results = ingest_footprints()
    print(f"--- DEBUG: Processed {len(results)} files ---")
    for item, status in results:
        print(f"{item}: {status}")
