#!/bin/bash

# Mengaktifkan virtual environment jika ada
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Menjalankan aplikasi
echo "Menjalankan aplikasi..."
python app.py

# Menjalankan perintah lain jika perlu
# python other_script.py
