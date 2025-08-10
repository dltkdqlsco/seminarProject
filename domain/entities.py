from datetime import datetime

class Role:
    ADMIN = 'admin'
    USER = 'user'
    GUEST = 'guest'

class User:
    def __init__(self, id, username, role=Role.USER):
        self.id = id
        self.username = username
        self.role = role

class MediaFile:
    def __init__(self, id, name, owner_id, content_type, size, created_at=None, metadata=None):
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.content_type = content_type
        self.size = size
        self.created_at = created_at or datetime.utcnow()
        self.metadata = metadata or {}
        self.deleted = False

class ImageFile(MediaFile): pass
class VideoFile(MediaFile): pass
class AudioFile(MediaFile): pass
