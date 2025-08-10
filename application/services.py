class MediaService:
    def __init__(self, repo, notifier, metadata_store):
        self.repo = repo
        self.notifier = notifier
        self.metadata_store = metadata_store

    def upload(self, file_stream, filename, content_type, size, owner_id, metadata):
        from domain.media_factory import MediaFileFactory
        import uuid

        file_id = str(uuid.uuid4())
        media_file = MediaFileFactory.create(content_type, file_id, filename, owner_id, content_type, size, metadata=metadata)
        self.repo.save(media_file, file_stream)
        self.metadata_store.save_metadata(media_file)
        self.notifier.notify("upload", media_file)
        return media_file

    def download(self, file_id, requesting_user_id):
        media_file = self.repo.get(file_id)
        if media_file.deleted:
            raise FileNotFoundError("File is deleted")
        # add your auth/perm check here
        return media_file

    def delete(self, file_id, requesting_user_id):
        media_file = self.repo.get(file_id)
        # add your auth/perm check here
        self.repo.delete(file_id)
        media_file.deleted = True
        self.metadata_store.save_metadata(media_file)
        self.notifier.notify("delete", media_file)
        return True

    def organize(self, cleanup_strategy):
        files = self.repo.list()
        for f in cleanup_strategy.select_files_to_delete(files):
            self.delete(f.id, f.owner_id)
