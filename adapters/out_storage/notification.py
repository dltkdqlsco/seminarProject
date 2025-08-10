class PrintNotifier:
    def notify(self, event, media_file):
        print(f"{event}: {media_file.name} (id={media_file.id})")
