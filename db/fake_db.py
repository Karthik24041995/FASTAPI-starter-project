from typing import List, Dict, Optional
from threading import Lock

class FakeDB:
    def __init__(self):
        self.users: Dict[int, dict] = {}
        self.items: Dict[int, dict] = {}
        self.user_id_seq = 1
        self.item_id_seq = 1
        self.lock = Lock()

    # User methods
    def add_user(self, user: dict) -> dict:
        with self.lock:
            user['id'] = self.user_id_seq
            self.users[self.user_id_seq] = user.copy()
            self.user_id_seq += 1
        return user

    def get_user(self, user_id: int) -> Optional[dict]:
        return self.users.get(user_id)

    def list_users(self) -> List[dict]:
        return list(self.users.values())

    # Item methods
    def add_item(self, item: dict) -> dict:
        with self.lock:
            item['id'] = self.item_id_seq
            self.items[self.item_id_seq] = item.copy()
            self.item_id_seq += 1
        return item

    def get_item(self, item_id: int) -> Optional[dict]:
        return self.items.get(item_id)

    def list_items(self) -> List[dict]:
        return list(self.items.values())

db = FakeDB()