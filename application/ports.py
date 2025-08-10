from abc import ABC, abstractmethod

class MediaRepository(ABC):
    @abstractmethod
    def save(self, media_file, file_stream): pass
    @abstractmethod
    def get(self, file_id): pass
    @abstractmethod
    def delete(self, file_id): pass
    @abstractmethod
    def list(self, owner_id=None): pass

class MetadataStorePort(ABC):
    @abstractmethod
    def save_metadata(self, media_file): pass
    @abstractmethod
    def get_metadata(self, file_id): pass

class NotificationPort(ABC):
    @abstractmethod
    def notify(self, event, media_file): pass
