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
        return {"kuantitas":pesanan.getKuantitas()}
    
    @staticmethod
    def setKuantitas(id_pesanan, id_menu):
        kuantitasbaru = request.json.get("kuantitas")
        pesanan = Pesanan.getMenuPesananById(id_pesanan, id_menu)
        pesanan.setKuantitas(kuantitasbaru, id_pesanan, id_menu)
        return "Kuantitas Berhasil Diperbarui!", 201
    
    @staticmethod
    def deleteMenuInPesanan(id_pesanan, id_menu):
        pesanan = Pesanan.getMenuPesananById(id_pesanan, id_menu)
        return pesanan.deleteMenuInPesanan(id_pesanan, id_menu)
    
    @staticmethod
    def deletePesanan(id_pesanan):
        return Pesanan.deletePesanan(id_pesanan)
    