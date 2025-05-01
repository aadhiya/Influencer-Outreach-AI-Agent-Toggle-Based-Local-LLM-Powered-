
import sqlite3
from datetime import datetime
import os

DB_PATH = "email_log.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sent_emails (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            status TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_email(email, status, toggles):
    if not toggles.get("logging_enabled"):
        return
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT OR IGNORE INTO sent_emails (email, status, timestamp) VALUES (?, ?, ?)",
                       (email, status, datetime.now().isoformat()))
        conn.commit()
    except Exception as e:
        print("[LOG ERROR]", e)
    finally:
        conn.close()

def was_email_sent(email):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM sent_emails WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()
    return result is not None
