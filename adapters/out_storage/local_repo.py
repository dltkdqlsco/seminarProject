import os, pickle

class LocalMediaRepository:
    DATA_FILE = './media_db.pkl'
    STORAGE_DIR = './uploads/'

    def __init__(self):
        if not os.path.exists(self.STORAGE_DIR):
            os.makedirs(self.STORAGE_DIR)

    def _load_db(self):
        try:
            with open(self.DATA_FILE, 'rb') as f: return pickle.load(f)
        except: return {}

    def _save_db(self, db): 
        with open(self.DATA_FILE, 'wb') as f: pickle.dump(db, f)

    def save(self, media_file, file_stream):
        db = self._load_db()
        with open(os.path.join(self.STORAGE_DIR, f"{media_file.id}_{media_file.name}"), 'wb') as out:
            out.write(file_stream.read())
        db[media_file.id] = media_file
        self._save_db(db)

    def get(self, file_id):
        return self._load_db().get(file_id)

    def delete(self, file_id):
        db = self._load_db()
        f = db.get(file_id)
        if f:
            fp = os.path.join(self.STORAGE_DIR, f"{f.id}_{f.name}")
            if os.path.exists(fp): os.remove(fp)
            del db[file_id]
        self._save_db(db)

    def list(self, owner_id=None):
        db = self._load_db()
        return [f for f in db.values() if (owner_id is None or f.owner_id == owner_id)]
