import sqlite3
from datetime import datetime

DB_FILE = "email_log.db"

# Create the table if it doesn't exist
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS email_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            subject TEXT,
            sent_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Check if email was already sent
def was_email_sent(email):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM email_log WHERE email = ?", (email,))
    result = c.fetchone()
    conn.close()
    return result is not None

# Log new email send
def log_email_sent(email, subject):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO email_log (email, subject, sent_at) VALUES (?, ?, ?)",
              (email, subject, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()
