"""
History helpers for conversations and messages (Phase 1)
CRUD utilities used by the UI and AI brain.
"""

from typing import Optional, List, Dict
from database.database import Database

class History:
    def __init__(self, db: Database):
        self.db = db

    def create_conversation(self, chat_id: str, title: str = '') -> int:
        conn = self.db.get_conn()
        cur = conn.cursor()
        cur.execute('INSERT OR IGNORE INTO conversations (chat_id, title) VALUES (?, ?)', (chat_id, title))
        conn.commit()
        cur.execute('SELECT id FROM conversations WHERE chat_id = ?', (chat_id,))
        row = cur.fetchone()
        return row['id'] if row else -1

    def add_message(self, conversation_id: int, role: str, content: str) -> int:
        conn = self.db.get_conn()
        cur = conn.cursor()
        cur.execute('INSERT INTO messages (conversation_id, role, content) VALUES (?, ?, ?)', (conversation_id, role, content))
        conn.commit()
        return cur.lastrowid

    def list_conversations(self) -> List[Dict]:
        conn = self.db.get_conn()
        cur = conn.cursor()
        cur.execute('SELECT id, chat_id, title, created_at, updated_at FROM conversations ORDER BY updated_at DESC')
        rows = cur.fetchall()
        return [dict(r) for r in rows]

    def get_messages(self, conversation_id: int) -> List[Dict]:
        conn = self.db.get_conn()
        cur = conn.cursor()
        cur.execute('SELECT id, role, content, created_at FROM messages WHERE conversation_id = ? ORDER BY created_at', (conversation_id,))
        return [dict(r) for r in cur.fetchall()]
