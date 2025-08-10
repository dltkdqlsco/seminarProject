from abc import ABC, abstractmethod

class MetadataReader(ABC):
    @abstractmethod
    def extract(self, file_path):
        pass

class ImageMetadataReader(MetadataReader):
    def extract(self, file_path):
        from PIL import Image
        with Image.open(file_path) as img:
            return {
                'format': img.format,
                'mode': img.mode,
                'width': img.width,
                'height': img.height
            }

class VideoMetadataReader(MetadataReader):
    def extract(self, file_path):
        import ffmpeg
        probe = ffmpeg.probe(file_path)
        vstream = next(s for s in probe['streams'] if s['codec_type'] == 'video')
        return {
            'codec': vstream['codec_name'],
            'width': vstream['width'],
            'height': vstream['height'],
            'duration': float(vstream.get('duration', 0)),
        }

class AudioMetadataReader(MetadataReader):
    def extract(self, file_path):
        import mutagen
        audio = mutagen.File(file_path)
        return {
            'length': audio.info.length,
            'bitrate': getattr(audio.info, 'bitrate', None)
        }
