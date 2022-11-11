# Puser-Python-App

Cara Menggunakan API/Server (Ambil Data Dari API)
1. Buka terminal wsl
2. Bikin venv dengan
```sh
python3 -m venv venv
```
3. Aktifkan venv dengan
```sh
source venv/bin/activate
```
4. Install module yang ada di requirements.txt dengan
```sh
cd src
pip install -r requirements.txt
```
5. Connect database menggunakan secret DATABASE_URL-nya dengan membuat file .env pada folder server dan membuat variabel DATABASE_URL. Bisa dilakukan dengan
```sh
cd server
touch .env

#Didalam file .env
DATABASE_URL = "postgresql://wgnkqtmt:NHQ1LhueR2QAauehJrWyQ8dXA3-D5-Jh@tiny.db.elephantsql.com/wgnkqtmt"
```
6. Run server dengan
```sh
cd ..
python3 app.py
```
7. Selesai! Kalau mau tes pakai API-nya bisa pakai contoh.py yang ada di folder client. Tinggal di run aja filenya. 

### Note
1. JANGAN KILL TERMINAL SERVER! PASTIKAN SERVER TETAP JALAN!
2. Bagian client(fron-end) dan server(back-end) sebenernya bisa dijalankan secara barengan langsung mengugnakan 1 file, yakni app.py. Untuk sekarang, front-end bikin aja app.py sendiri di folder client untuk ngetes front-endnya. Tapi kalau udah bisa, langsung masukin ke fungsi __name__ = __main__ di app.py aja fungsi buat ngeload front-endnya
