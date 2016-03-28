from lab_assistant.storage.backends.base import StorageBackend


class NullBackend(StorageBackend):
    def get(self, key):
        return None

    def set(self, key, result):
        return None

    def remove(self, key):
        return None

    def clear(self):
        return None

    def list(self):
        return []
