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


class TestDetailPesananAPI(unittest.TestCase):
    URL = "http://localhost:5000/api/detail-pesanan/"

    detailPesanan_data = {
        "dine_in_status": False,
    }

    detailPesanan_data_id_1 = {
        "dine_in_status": False,
        "nomor_meja": 0,
        "id": 1
    }

    expected_updated_detail_pesanan = {
        "dine_in_status": True,
        "nomor_meja": 2,
        "id": 1
    }

    def test_add_detail_pesanan(self):
        res = requests.post(self.URL + "/add", json=self.detailPesanan_data)
        self.assertEqual(res.status_code, 200)

    def test_get_detail_pesanan(self):
        res = requests.get(self.URL)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 1)

    def test_get_detail_pesanan_by_id(self):
        res = requests.get(self.URL + "/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json(), self.detailPesanan_data_id_1)

    def test_get_dine_in_status(self):
        res = requests.get(self.URL + "/dine-in-status/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            res.json()["dine_in_status"], self.detailPesanan_data_id_1["dine_in_status"])

    def test_get_nomor_meja(self):
        res = requests.get(self.URL + "/nomor-meja/1")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            res.json()["nomor_meja"], self.detailPesanan_data_id_1["nomor_meja"])

    def test_update_dine_in_status(self):
        res = requests.put(self.URL + "/update/dine-in-status/1",
                           json={"dine_in_status": True})
        res2 = requests.get(self.URL + "/1")
        self.assertEqual(res2.json()[
                         "dine_in_status"], self.expected_updated_detail_pesanan["dine_in_status"])

    def test_update_nomor_meja(self):
        res = requests.put(self.URL + "/update/nomor-meja/1",
                           json={"nomor_meja": 2})
        res2 = requests.get(self.URL + "/1")
        self.assertEqual(
            res2.json()["nomor_meja"], self.expected_updated_detail_pesanan["nomor_meja"])

    def test_delete_detail_pesanan(self):
        res = requests.delete(self.URL + "/delete/1")
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
