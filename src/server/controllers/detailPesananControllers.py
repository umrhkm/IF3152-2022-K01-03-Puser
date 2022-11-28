from flask import request, jsonify

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
