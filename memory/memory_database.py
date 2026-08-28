"""
Memory database helpers (Phase 1)
Simple wrappers to read/write memory table created in migrations.
"""

from database.database import Database
from typing import List, Dict

class MemoryDatabase:
    def __init__(self, db: Database):
        self.db = db

    def store(self, key: str, value: str, category: str = 'general') -> int:
        conn = self.db.get_conn()
        cur = conn.cursor()
        cur.execute('INSERT INTO memory (key, value, category) VALUES (?, ?, ?)', (key, value, category))
        conn.commit()
        return cur.lastrowid

    def retrieve(self, key: str) -> List[Dict]:
        conn = self.db.get_conn()
        cur = conn.cursor()
        cur.execute('SELECT * FROM memory WHERE key = ?', (key,))
        return [dict(r) for r in cur.fetchall()]

    def list_all(self) -> List[Dict]:
        conn = self.db.get_conn()
        cur = conn.cursor()
        cur.execute('SELECT * FROM memory ORDER BY created_at DESC')
        return [dict(r) for r in cur.fetchall()]
