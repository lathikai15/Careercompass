import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            first_name TEXT,
            last_name TEXT,
            dob TEXT,
            qualification TEXT,
            institute TEXT,
            experience TEXT,
            domain TEXT,
            known_skills TEXT
        )
    """)

    conn.commit()
    conn.close()
