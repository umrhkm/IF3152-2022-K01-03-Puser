# pylint: disable=W0622
# pylint: disable=C0301
# pylint: disable=C0114
# pylint: disable=C0115
# pylint: disable=C0116
# pylint: disable=C0103
# pylint: disable=W0603
# pylint: disable=W0201
# pylint: disable=I1101
# pylint: disable=W0602
# pylint: disable=R0902
# pylint: disable=R0915
# pylint: disable=W0707
# pylint: disable=R0801
# pylint: disable=E0211
# pylint: disable=C0325
# pylint: disable=W0703

from server.config.db import get_connection


class DetailPesanan():
    def __init__(self, dine_in_status):
        self.dine_in_status = dine_in_status

        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO detail_pesanan (dine_in_status) VALUES (%s)", (self.dine_in_status,))
            connection.commit()
            connection.close()

        except Exception as err:
            raise Exception(err)

    def getAllDetailPesanan():
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM detail_pesanan")
                resultset = cursor.fetchall()
            connection.commit()
            connection.close()

            hasil = []

            for pesanan in resultset:
                datapesanan = {}
                datapesanan["id"] = pesanan[0]
                datapesanan["dine_in_status"] = pesanan[1]
                datapesanan["nomor_meja"] = pesanan[2]
                hasil.append(datapesanan)

            return (hasil)

        except Exception as err:
            raise Exception(err)

    @classmethod
    def getDetailPesananById(cls, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM detail_pesanan WHERE id = (%s)", (id,))
                resultset = cursor.fetchall()
            connection.commit()
            connection.close()

            if resultset is None:
                raise Exception("Data tidak ditemukan!")

            id, dine_in_status, nomor_meja = resultset[0]

            self = cls.__new__(cls)
            self.id = id
            self.dine_in_status = dine_in_status
            self.nomor_meja = nomor_meja

            return self

        except Exception as err:
            raise Exception(err)

    def getDetailPesananData(self):
        return ({"id": self.id, "dine_in_status": self.dine_in_status, "nomor_meja": self.nomor_meja})

    def getDineInStatus(self):
        return self.dine_in_status

    def setDineInStatus(self, statusbaru, id):
        self.dine_in_status = statusbaru
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE detail_pesanan SET dine_in_status = (%s) WHERE id = (%s)", (self.dine_in_status, id,))
            connection.commit()
            connection.close()

        except Exception as err:
            raise Exception(err)

    def getNomorMeja(self):
        return self.nomor_meja

    def setNomorMeja(self, nomormejabaru, id):
        if (nomormejabaru <= 0):
            raise Exception("Nomor mehja tidak valid, harus lebih dari 0!")

        self.nomor_meja = nomormejabaru
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE detail_pesanan SET nomor_meja = (%s) WHERE id = (%s)", (self.nomor_meja, id,))
            connection.commit()
            connection.close()

        except Exception as err:
            raise Exception(err)

    def deleteDetailPesanan(self, id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM detail_pesanan WHERE id = (%s)", (id,))
            connection.commit()
            connection.close()

        except Exception as err:
            raise Exception(err)
