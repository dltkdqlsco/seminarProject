from .entities import ImageFile, VideoFile, AudioFile, MediaFile

class MediaFileFactory:
    @staticmethod
    def create(content_type, *args, **kwargs):
        if content_type.startswith('image/'):
            return ImageFile(*args, **kwargs)
        elif content_type.startswith('video/'):
            return VideoFile(*args, **kwargs)
        elif content_type.startswith('audio/'):
            return AudioFile(*args, **kwargs)
        else:
            return MediaFile(*args, **kwargs)
