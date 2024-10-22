from datetime import datetime

# Mengambil waktu saat ini
now = datetime.now()

# Menampilkan waktu dalam format tertentu
print(f'Sekarang adalah: {now.strftime("%Y-%m-%d %H:%M:%S")}')

