'''
NOTE
Proses kerja testing tidak berjalan secara sekuensial (tidak terurut dari atas ke bawah) dan
data yang diperiksa merupakan data dinamis sehingga untuk mencoba file ini hanya dapat
dilakukan 1 kali (karena ada tes add, update, delete yang mengubah index pada database).

TATA CARA PENGGUNAAN FILE
Silahkan lakukan comment untuk setiap fungsi pada kelas kecuali fungsi dengan HTTP request "post"
dan jalankan file ini.
Selanjutnya, silahkan comment setiap fungsi pada kelas kecuali fungsi dengan HTTP request "get"
dan jalankan file ini.
Selanjutnya, silahkan comment setiap fungsi pada kelas kecuali fungsi dengan HTTP request "put"
dan jalankan file ini.
Terakhir, silahkan comment setiap fungsi pada kelas kecuali fungsi dengan HTTP request "delete"
dan jalankan file ini.
'''

import unittest
import requests
import sys
sys.path.append('../..')

from app import app


class TestMenuAPI(unittest.TestCase):
    URL = "http://localhost:5000/api/menus/"

    menu_data = {
        "nama": "Testing menu",
        "harga": 10000,
        "kategori": "makanan",
        "jumlahStok": 1
    }

    menu_data_id_1 = {
        "harga": 25000,
        "id": 1,
        "jumlahStok": 0,
        "kategori": "makanan",
        "nama": "Mie Rebus"
    }

    expected_updated_nama_menu = {
        "harga": 10000,
        "id": 32,
        "jumlahStok": 1,
        "kategori": "makanan",
        "nama": "updated"
    }

    expected_updated_harga_menu = {
        "harga": 9999,
        "id": 32,
        "jumlahStok": 1,
        "kategori": "makanan",
        "nama": "updated"
    }

    expected_updated_jumlahStok_menu = {
        "harga": 9999,
        "id": 32,
        "jumlahStok": 3,
        "kategori": "makanan",
        "nama": "updated"
    }

    def test_add_menu(self):
        res = requests.post(self.URL + "/add", json=self.menu_data)
        self.assertEqual(res.status_code, 200)

    def test_get_menus(self):
        res = requests.get(self.URL)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 28)

    def test_get_menus_by_id(self):
        res = requests.get(self.URL + "/search-id/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), self.menu_data_id_1)

    def test_get_menus_by_nama(self):
        res = requests.get(self.URL + "/search-nama/Mie%20Rebus")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()[0], self.menu_data_id_1)

    def test_get_nama(self):
        res = requests.get(self.URL + "/nama/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), self.menu_data_id_1["nama"])

    def test_get_harga(self):
        res = requests.get(self.URL + "/harga/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), self.menu_data_id_1["harga"])

    def test_get_kategori(self):
        res = requests.get(self.URL + "/kategori/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), self.menu_data_id_1["kategori"])

    def test_get_jumlahStok(self):
        res = requests.get(self.URL + "/jumlah-stok/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), self.menu_data_id_1["jumlahStok"])

    def test_update_menu_nama(self):
        res = requests.put(self.URL + "/update/nama/32",
                           json={"nama": "updated"})
        res2 = requests.get(self.URL + "/search-id/32")
        self.assertEqual(res2.json(), self.expected_updated_nama_menu)

    def test_update_menu_harga(self):
        res = requests.put(self.URL + "/update/harga/32", json={"harga": 9999})
        res2 = requests.get(self.URL + "/search-id/32")
        self.assertEqual(res2.json(), self.expected_updated_harga_menu)

    def test_update_menu_jumlahStok(self):
        res = requests.put(
            self.URL + "/update/jumlah-stok/32", json={"jumlahStok": 3})
        res2 = requests.get(self.URL + "/search-id/32")
        self.assertEqual(res2.json(), self.expected_updated_jumlahStok_menu)

    def test_delete_menu(self):
        res = requests.delete(self.URL + "/delete/32")
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
