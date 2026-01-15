# core/db.py

import sqlite3
from config import DB_PATH
from datetime import datetime

def get_connection():
    """
    Returns a SQLite3 connection object
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Optional: allows dict-like access
    return conn


def create_table(conn, table_name):
    """
    Create table if it doesn't exist
    """
    query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT UNIQUE,
        file_path TEXT,
        file_size INTEGER,
        library_name TEXT,
        category TEXT,
        symbol_name TEXT,
        description TEXT,
        pin_count INTEGER,
        checksum TEXT,
        license TEXT,
        ingested_at TEXT
    )
    """
    conn.execute(query)
    conn.commit()


def insert_or_update(conn, table_name, data):
    """
    Insert a record, or update if file_name already exists
    """
    data['ingested_at'] = data.get('ingested_at', datetime.now().isoformat())
    query = f"""
    INSERT INTO {table_name} (
        file_name, file_path, file_size, library_name, category,
        symbol_name, description, pin_count, checksum, license, ingested_at
    )
    VALUES (
        :file_name, :file_path, :file_size, :library_name, :category,
        :symbol_name, :description, :pin_count, :checksum, :license, :ingested_at
    )
    ON CONFLICT(file_name) DO UPDATE SET
        file_path=excluded.file_path,
        file_size=excluded.file_size,
        library_name=excluded.library_name,
        category=excluded.category,
        symbol_name=excluded.symbol_name,
        description=excluded.description,
        pin_count=excluded.pin_count,
        checksum=excluded.checksum,
        license=excluded.license,
        ingested_at=excluded.ingested_at
    """
    conn.execute(query, data)
    conn.commit()
