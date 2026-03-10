import sqlite3
from datetime import datetime

DB_NAME = "memory.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            message TEXT,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_message(role, message):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO memory (role, message, timestamp) VALUES (?, ?, ?)",
        (role, message, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    conn.close()

def get_history_by_date():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        SELECT date(timestamp), role, message
        FROM memory
        ORDER BY timestamp ASC
    """)
    rows = cur.fetchall()
    conn.close()

    history = {}
    for date, role, message in rows:
        history.setdefault(date, []).append({
            "role": role,
            "message": message
        })
    return history
