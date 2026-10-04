import json
import os

class NormalizedStore:
    def __init__(self, storage_path="C:/Users/ADMIN/FreelanceOS/memory/session_store.json"):
        self.storage_path = storage_path
        self.data = self._load()

    def _load(self):
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r') as f:
                return json.load(f)
        return {"sessions": {}, "global_knowledge": {}}

    def save(self):
        with open(self.storage_path, 'w') as f:
            json.dump(self.data, f, indent=4)

    def update_session(self, session_id, key, value):
        if session_id not in self.data["sessions"]:
            self.data["sessions"][session_id] = {}
        self.data["sessions"][session_id][key] = value
        self.save()

    def get_session(self, session_id):
        return self.data["sessions"].get(session_id, {})

    def add_knowledge(self, key, value):
        self.data["global_knowledge"][key] = value
        self.save()

    def get_knowledge(self, key):
        return self.data["global_knowledge"].get(key)
