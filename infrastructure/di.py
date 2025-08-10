from adapters.out_storage.local_repo import LocalMediaRepository
from adapters.out_storage.notification import PrintNotifier
from adapters.out_storage.metadata_adapter import LocalMetadataStore
from application.services import MediaService

def get_media_service():
    repo = LocalMediaRepository()
    notifier = PrintNotifier()
    metadata_store = LocalMetadataStore()
    return MediaService(repo, notifier, metadata_store)
