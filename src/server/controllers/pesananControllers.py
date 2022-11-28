from flask import request, jsonify

from server.models.pesananModels import Pesanan


class pesananController:
    @staticmethod
    def createPesanan():
        try:
            id_pesanan = request.json.get("id_pesanan")
            id_menu = request.json.get("id_menu")
            kuantitas = request.json.get("kuantitas")

            Pesanan(id_pesanan, id_menu, kuantitas)

            return "Pesanan Berhasil Ditambahkan!", 201

        except Exception as err:
            raise Exception(err)

    @staticmethod
    def getAllPesanan():
        return Pesanan.getAllPesanan()

    @staticmethod
    def getPesananDataById(id):
        pesanan = Pesanan.getPesananById(id)
        return pesanan

    @staticmethod
    def getMenuPesananDataById(id_pesanan, id_menu):
        pesanan = Pesanan.getMenuPesananById(id_pesanan, id_menu)
        return pesanan.getPesananData()

    @staticmethod
    def getKuantitas(id_pesanan, id_menu):
        pesanan = Pesanan.getMenuPesananById(id_pesanan, id_menu)
        return {"kuantitas": pesanan.getKuantitas()}

    @staticmethod
    def setKuantitas(id_pesanan, id_menu):
        print("HALO1")
        kuantitasbaru = request.json.get("kuantitas")
        print("HALO2")
        pesanan = Pesanan.getMenuPesananById(id_pesanan, id_menu)
        print("HALO3")
        pesanan.setKuantitas(kuantitasbaru, id_pesanan, id_menu)
        print("HALO4")
        return "Kuantitas Berhasil Diperbarui!", 201

    @staticmethod
    def getCatatan(id_pesanan, id_menu):
        pesanan = Pesanan.getMenuPesananById(id_pesanan, id_menu)
        return {"catatan": pesanan.getCatatan()}

    @staticmethod
    def setCatatan(id_pesanan, id_menu):
        catatanbaru = request.json.get("catatan")
        pesanan = Pesanan.getMenuPesananById(id_pesanan, id_menu)
        pesanan.setCatatan(catatanbaru, id_pesanan, id_menu)
        return "Catatan Berhasil Diperbarui!", 201

    @staticmethod
    def deleteMenuInPesanan(id_pesanan, id_menu):
        pesanan = Pesanan.getMenuPesananById(id_pesanan, id_menu)
        return pesanan.deleteMenuInPesanan(id_pesanan, id_menu)

    @staticmethod
    def deletePesanan(id_pesanan):
        return Pesanan.deletePesanan(id_pesanan)
