from flask import Flask, request, send_file, jsonify
from adapters.out_storage.local_repo import LocalMediaRepository
from adapters.out_storage.notification import PrintNotifier
from adapters.out_storage.metadata_adapter import LocalMetadataStore
from application.services import MediaService
from domain.metadate_reader import ImageMetadataReader, VideoMetadataReader, AudioMetadataReader
from domain.cleanup_strategy import AgeBasedCleanup, SizeBasedCleanup

app = Flask(__name__)
repo = LocalMediaRepository()
notifier = PrintNotifier()
metadata_store = LocalMetadataStore()
service = MediaService(repo, notifier, metadata_store)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    owner_id = request.form.get('owner_id')
    content_type = file.content_type

    # Metadata extraction
    if content_type.startswith('image/'):
        metadata = ImageMetadataReader().extract(file)
    elif content_type.startswith('video/'):
        metadata = VideoMetadataReader().extract(file)
    elif content_type.startswith('audio/'):
        metadata = AudioMetadataReader().extract(file)
    else:
        metadata = {}

    mf = service.upload(file, file.filename, content_type, file.content_length, owner_id, metadata)
    return jsonify({"file_id": mf.id})

@app.route('/download/<file_id>', methods=['GET'])
def download(file_id):
    mf = service.download(file_id, request.args.get('owner_id'))
    filepath = f"./uploads/{mf.id}_{mf.name}"
    return send_file(filepath, as_attachment=True)

@app.route('/delete/<file_id>', methods=['DELETE'])
def delete(file_id):
    service.delete(file_id, request.args.get('owner_id'))
    return '', 204

@app.route('/organize', methods=['POST'])
def organize():
    kind = request.json.get('type')
    if kind == 'age':
        days = request.json.get('days', 90)
        strat = AgeBasedCleanup(days)
    else:
        max_storage = request.json.get('max_bytes', 5*1024*1024*1024)
        strat = SizeBasedCleanup(max_storage)
    service.organize(strat)
    return '', 204
