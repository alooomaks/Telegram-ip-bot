import sqlite3
from datetime import datetime, timezone

DB_NAME = "users.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER,
            ip TEXT NOT NULL,
            user_agent TEXT,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_visit(telegram_id, ip, user_agent):
    conn = sqlite3.connect(DB_NAME)

    conn.execute(
        """
        INSERT INTO visits
        (telegram_id, ip, user_agent, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (
            telegram_id,
            ip,
            user_agent,
            datetime.now(timezone.utc).isoformat()
        )
    )

    conn.commit()
    conn.close()
