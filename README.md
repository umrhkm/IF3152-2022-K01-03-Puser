# Puser


## Deskripsi Singkat Program
User memerlukan suatu perangkat lunak yang dapat diakses menggunakan desktop untuk membuat pesanan pada sebuah restoran. Perangkat ini dibuat dengan tujuan dapat mengurangi antrian pada sebuah restoran.

Pengunjung dapat menggunakan layanan pada program dengan langsung datang ke restoran dan menggunakan desktop yang ada pada restoran. Program pada desktop akan langsung menampilkan homepage yang berupa daftar seleuruh menu yang ada pada restoran. Setiap menu yang ditampilkan akan tertera gambar, nama, harga, dan kuantitas dari menu. Kuantitas disini merupakan input dari pengunjung jika ia ingin memesan menu tersebut. Berdasarkan informasi pesanannya, akan ditampilkan juga total harga pesanannya pada homepage. Setelah selesai memilih menu, pengunjung dapat melakukan Checkout/Genereate QR untuk mendapatkan QR Code yang berisi informasi pesanannya. QR Code ini akan ditunjukkan kepada kasir restoran untuk selanjutnya memproses pesanan dari pengunjung.


## Cara Menggunakan Aplikasi

1. Buka terminal (direkomendasikan menggunakan wsl)
3. Persiapkan environment venv dengan
```sh
python3 -m venv venv
```
3. Aktifkan venv
```sh
source venv/bin/activate #Untuk WSL
???????????????????????? #Untuk powershell
```
4. Install module yang ada di requirements.txt dengan
```sh
cd src #Foler src
pip install -r requirements.txt
```
5. Connect database menggunakan secret DATABASE_URL-nya dengan membuat file .env pada folder server dan membuat variabel DATABASE_URL. Bisa dilakukan dengan
```sh
cd server #Folder Server
touch .env #Untuk WSL
#Cukup buat file .env pada folder server jika tidak menggunakan WSL

#Didalam file .env
DATABASE_URL = "postgresql://wgnkqtmt:NHQ1LhueR2QAauehJrWyQ8dXA3-D5-Jh@tiny.db.elephantsql.com/wgnkqtmt"
```
6. Run server dengan
```sh
cd .. #Folder src
python3 app.py
```
7. Selesai!


## Daftar Modul yang Diimplementasi
### 1. Menampilkan Seluruh Menu (18220...)
<foto screen>

### 2. dst

  
## Daftar Tabel Basis Data
- Daftar Seluruh Tabel
  ![image](https://user-images.githubusercontent.com/93817324/203487834-0073055d-324d-42a7-a622-59a77fd58197.png)

- Tabel Menu
  ![image](https://user-images.githubusercontent.com/93817324/203488521-44cdec0d-31d8-40c9-8a22-d5d305e21d98.png)

- Tabel Pesanan
  ![image](https://user-images.githubusercontent.com/93817324/203488453-46550849-7a79-449b-88f0-67396029592a.png)


### Note
1. JANGAN KILL TERMINAL SERVER! PASTIKAN SERVER TETAP JALAN!
2. Bagian client(fron-end) dan server(back-end) sebenernya bisa dijalankan secara barengan langsung mengugnakan 1 file, yakni app.py. Untuk sekarang, front-end bikin aja app.py sendiri di folder client untuk ngetes front-endnya. Tapi kalau udah bisa, langsung masukin ke fungsi __name__ = __main__ di app.py aja fungsi buat ngeload front-endnya
