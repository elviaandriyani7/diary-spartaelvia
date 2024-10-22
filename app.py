from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient  
from datetime import datetime
import os  # Untuk menghapus file jika perlu

# Ganti dengan string koneksi yang benar
connection_string = 'mongodb+srv://elviaandriani:Sparta@cluster0.c5lws.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(connection_string)  
db = client.dbsparta 

app = Flask(__name__)
CORS(app)  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/diary', methods=['GET'])
def show_diary():
    articles = list(db.diary.find({}, {'_id': False}))
    return jsonify({'articles': articles})

@app.route('/diary', methods=['POST'])
def save_diary():
    title_receive = request.form.get('title_give')  
    content_receive = request.form.get('content_give') 
    file = request.files.get('file_give')
    profile = request.files.get('profile_give')

    # Validasi input
    if not title_receive or not content_receive:
        return jsonify({'message': 'Title and content cannot be empty!'}), 400

    # Validasi file
    if not file or not profile:
        return jsonify({'message': 'Both files (image and profile) are required!'}), 400
    
    # Mendapatkan ekstensi file
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d %H-%M-%S')

    # Simpan gambar utama
    extension = file.filename.split('.')[-1]  
    filename = f'static/post-{mytime}.{extension}'
    file.save(filename)

    # Simpan gambar profil
    profile_extension = profile.filename.split('.')[-1]
    profile_name = f'static/profile-{mytime}.{profile_extension}'
    profile.save(profile_name)


    # Mempersiapkan dokumen untuk disimpan di MongoDB
    doc = {
        'file': filename,
        'profile': profile_name,
        'title': title_receive,
        'content': content_receive
    }

    # Simpan ke MongoDB
    db.diary.insert_one(doc)  
    print(f'Title: {title_receive}, Content: {content_receive}')  

    return jsonify({'message': 'Data was saved!'}), 201  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
