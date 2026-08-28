"""
Database utilities & migrations for Phase 1.
Wraps sqlite3 connections and applies simple migrations.
"""

import sqlite3
from sqlite3 import Connection
from pathlib import Path
import os
from typing import Optional

CREATE_TABLES_SQL = [
    # conversations
    """
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id TEXT UNIQUE,
        title TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,
    # messages
    """
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        conversation_id INTEGER,
        role TEXT,
        content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(conversation_id) REFERENCES conversations(id)
    );
    """,
    # memory
    """
    CREATE TABLE IF NOT EXISTS memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        key TEXT,
        value TEXT,
        category TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,
]

class Database:
    def __init__(self, path: str):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn: Optional[Connection] = None
        self._connect()
        self._migrate()

    def _connect(self):
        self.conn = sqlite3.connect(str(self.path), check_same_thread=False)
        self.conn.row_factory = sqlite3.Row

    def _migrate(self):
        cur = self.conn.cursor()
        for sql in CREATE_TABLES_SQL:
            cur.executescript(sql)
        self.conn.commit()

    def get_conn(self) -> Connection:
        if self.conn is None:
            self._connect()
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None
