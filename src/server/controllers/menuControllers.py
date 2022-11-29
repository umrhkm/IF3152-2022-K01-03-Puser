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

from flask import request

from server.models.menuModels import Menu


class menuController:
    @staticmethod
    def createMenu():
        try:
            nama = request.json.get("nama")
            harga = request.json.get("harga")
            kategori = request.json.get("kategori")
            jumlahStok = request.json.get("jumlahStok")

            Menu(nama, harga, kategori, jumlahStok)

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
    def deleteMenu(id):
        menu = Menu.getMenuById(id)
        return menu.deleteMenu(id)
