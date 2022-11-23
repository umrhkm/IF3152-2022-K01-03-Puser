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
6. Run aplikasi dengan
```sh
cd .. #Folder src
python3 app.py
```
7. Selesai!


## Daftar Modul yang Diimplementasi
### 1. Menampilkan Seluruh Menu (18220097 Muhamad Fikri Nurohman)
![image](./doc/tampilan_utama.jpg?raw=true "Title")
### 2. Membuat dan implementasi searchbar (18220071 Muhammad Zaky)

### 3. Menampilkan dan implementasi QR Code berisi detail pesanan (18220003 Made Adhika Wiwardhana)

### 4. Menampilkan catatan dan button (18220081 Muhammad Fariz Ramadhan)

### 5. Membuat pilihan Dine-In dan Take-Away serta penomoran Meja (18220061 Vincentius Verel Siedharta)

### 6. Membuat backend serta database (18220073 Umar Hakim)

### 7. Membuat tampilan utama (18220073 Umar Hakim)


  
## Daftar Tabel Basis Data
- Daftar Seluruh Tabel
  ![image](https://user-images.githubusercontent.com/93817324/203573890-f45e205b-69e3-4ce5-bfb5-afee42fffd9c.png)

- Tabel Menu
  ![image](https://user-images.githubusercontent.com/93817324/203574043-8ff3c316-34f9-4300-8be1-39cb32066873.png)
