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
# pylint: disable=E1120

'''Import Module'''
from flask import request

from server.models.detailPesananModels import DetailPesanan


class detailPesananController:
    @staticmethod
    def createDetailPesanan():
        try:
            dine_in_status = request.json.get("dine_in_status")

            DetailPesanan(dine_in_status)

            return "Detail Pesanan Berhasil Ditambahkan!", 201

        except Exception as err:
            raise Exception(err)

    @staticmethod
    def getAllDetailPesanan():
        return DetailPesanan.getAllDetailPesanan()

    @staticmethod
    def getDetailPesananDataById(id):
        pesanan = DetailPesanan.getDetailPesananById(id)
        return pesanan

    @staticmethod
    def getDineInStatus(id):
        pesanan = DetailPesanan.getDetailPesananById(id)
        return {"dine_in_status": pesanan.getDineInStatus()}

    @staticmethod
    def setDineInStatus(id):
        statusbaru = request.json.get("dine_in_status")
        pesanan = DetailPesanan.getDetailPesananById(id)
        pesanan.setDineInStatus(statusbaru, id)
        return "Dine In Status Berhasil Diperbarui!", 201

    @staticmethod
    def getNomorMeja(id):
        pesanan = DetailPesanan.getDetailPesananById(id)
        return {"nomor_meja": pesanan.getNomorMeja()}

    @staticmethod
    def setNomorMeja(id):
        nomormejabaru = request.json.get("nomor_meja")
        pesanan = DetailPesanan.getDetailPesananById(id)
        pesanan.setNomorMeja(nomormejabaru, id)
        return "Nomor Meja Berhasil Diperbarui!", 201

    @staticmethod
    def deleteDetailPesanan(id):
        return DetailPesanan.deleteDetailPesanan(id)
