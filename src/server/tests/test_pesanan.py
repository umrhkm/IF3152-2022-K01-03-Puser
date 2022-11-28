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

class TestPesananAPI(unittest.TestCase):
    URL = "http://localhost:5000/api/pesanan/"

    pesanan_data = {
        "id_pesanan": 1,
        "id_menu": 1,
        "kuantitas": 1
    }

    pesanan_data_id_1 = {
        "id_pesanan": 1,
        "id_menu": 1,
        "kuantitas": 1,
        "catatan": ""
    }

    expected_updated_pesanan = {
        "id_pesanan": 1,
        "id_menu": 1,
        "kuantitas": 2,
        "catatan": "updated"
    }

    def test_add_pesanan(self):
        res = requests.post(self.URL + "/add", json=self.pesanan_data)
        self.assertEqual(res.status_code, 200)

    def test_get_pesanan(self):
        res = requests.get(self.URL)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 1)

    def test_get_pesanan_by_id(self):
        res = requests.get(self.URL + "/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()[0], self.pesanan_data_id_1)

    def test_get_menu_pesanan_by_id(self):
        res = requests.get(self.URL + "/1/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), self.pesanan_data_id_1)

    def test_get_kuantitas(self):
        res = requests.get(self.URL + "kuantitas/1/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["kuantitas"], 1)

    def test_get_catatan(self):
        res = requests.get(self.URL + "catatan/1/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["catatan"], "")

    def test_update_kuantitas(self):
        res = requests.put(self.URL + "/update/kuantitas/1/1",
                           json={"kuantitas": 2})
        res2 = requests.get(self.URL + "/1/1")
        self.assertEqual(res2.json()["kuantitas"],
                         self.expected_updated_pesanan["kuantitas"])

    def test_update_catatan(self):
        res = requests.put(self.URL + "/update/catatan/1/1",
                           json={"catatan": "updated"})
        res2 = requests.get(self.URL + "/1/1")
        self.assertEqual(res2.json()["catatan"],
                         self.expected_updated_pesanan["catatan"])

    def test_delete_pesanan(self):
        res = requests.delete(self.URL + "/delete/1")
        self.assertEqual(res.status_code, 200)

    def test_delete_menu_in_pesanan(self):
        res = requests.delete(self.URL + "/delete/1/1")
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
