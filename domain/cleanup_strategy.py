from datetime import datetime, timedelta
from abc import ABC, abstractmethod

class CleanupStrategy(ABC):
    @abstractmethod
    def select_files_to_delete(self, files):
        pass

class AgeBasedCleanup(CleanupStrategy):
    def __init__(self, max_age_days):
        self.max_age_days = max_age_days

    def select_files_to_delete(self, files):
        threshold = datetime.utcnow() - timedelta(days=self.max_age_days)
        return [f for f in files if f.created_at < threshold]

class SizeBasedCleanup(CleanupStrategy):
    def __init__(self, max_storage_bytes):
        self.max_storage_bytes = max_storage_bytes

    def select_files_to_delete(self, files):
        sorted_files = sorted(files, key=lambda f: f.created_at)
        total = sum(f.size for f in files)
        to_delete = []
        for f in sorted_files:
            if total <= self.max_storage_bytes:
                break
            to_delete.append(f)
            total -= f.size
        return to_delete
