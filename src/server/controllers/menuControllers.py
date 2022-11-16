from flask import request, jsonify

from server.models.menuModels import Menu

class menuController:
    @staticmethod
    def createMenu():
        try:
            nama = request.json.get("nama")
            harga = request.json.get("harga")
            kategori = request.json.get("kategori")

            Menu(nama, harga, kategori)

            return "Menu Berhasil Ditambahkan!", 201
        
        except Exception as err:
            raise Exception(err)
    
    @staticmethod
    def getAllMenu():
        return Menu.getAllMenu()
    
    @staticmethod
    def getMenuDataByNama(nama):
        menu = Menu.getMenuByNama(nama)
        return menu

    @staticmethod
    def getMenuDataById(id):
        menu = Menu.getMenuById(id)
        return menu.getMenuData()

    @staticmethod
    def setMenuNama(id):
        namabaru = request.json.get("nama")
        menu = Menu.getMenuById(id)
        menu.setNama(namabaru, id)
        return "Menu Berhasil Diperbarui!", 201
    
    @staticmethod
    def setHarga(id):
        hargabaru = request.json.get("harga")
        menu = Menu.getMenuById(id)
        menu.setHarga(hargabaru, id)
        return "Menu Berhasil Diperbarui!", 201
    
    @staticmethod
    def setJumlahStok(id):
        jumlahStokbaru = request.json.get("jumlahStok")
        menu = Menu.getMenuById(id)
        menu.setJumlahStok(jumlahStokbaru, id)
        return "Menu Berhasil Diperbarui!", 201
    
    @staticmethod
    def getNama(id):
        menu = Menu.getMenuById(id)
        return menu.getNamaMenu()
    
    @staticmethod
    def getHarga(id):
        menu = Menu.getMenuById(id)
        return menu.getHargaMenu()
    
    @staticmethod
    def getKategori(id):
        menu = Menu.getMenuById(id)
        return menu.getKategoriMenu()
    
    @staticmethod
    def getJumlahStok(id):
        menu = Menu.getMenuById(id)
        return menu.getJumlahStokMenu()
    
    @staticmethod
    def setMenuFoto(id):
        fotobaru = request.json.get("fotoUrl")
        menu = Menu.getMenuById(id)
        menu.setFoto(fotobaru, id)
        return "Foto Menu Berhasil Diperbarui!", 201

    @staticmethod
    def getMenuFoto(id):
        menu = Menu.getMenuById(id)
        return menu.getFoto()
    
    @staticmethod
    def deleteMenu(id):
        menu = Menu.getMenuById(id)
        return menu.deleteMenu(id)