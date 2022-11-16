from flask import Blueprint, jsonify, request


from server.controllers.menuControllers import menuController

menuRoutes = Blueprint('menuRoutes', __name__)

@menuRoutes.route('/', methods=['GET'])
def get_menus():
    try:
        menus = menuController.getAllMenu()
        return jsonify(menus)
    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@menuRoutes.route('/search-id/<id>', methods=['GET'])
def get_menu_by_id(id):
    try:
        menu = menuController.getMenuDataById(id)
        if menu != None:
            return (menu)
        else:
            return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@menuRoutes.route('/search-nama/<nama>', methods=['GET'])
def get_menu_by_nama(nama):
    try:
        menu = menuController.getMenuDataByNama(nama)
        if menu != None:
            return jsonify(menu)
        else:
            return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@menuRoutes.route('/nama/<id>', methods=['GET'])
def get_nama(id):
    try:
        menu = menuController.getNama(id)
        if menu != None:
            return jsonify(menu)
        else:
            return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@menuRoutes.route('/harga/<id>', methods=['GET'])
def get_harga(id):
    try:
        menu = menuController.getHarga(id)
        if menu != None:
            return jsonify(menu)
        else:
            return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@menuRoutes.route('/kategori/<id>', methods=['GET'])
def get_kategori(id):
    try:
        menu = menuController.getKategori(id)
        if menu != None:
            return jsonify(menu)
        else:
            return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@menuRoutes.route('/jumlah-stok/<id>', methods=['GET'])
def get_jumlahStok(id):
    try:
        menu = menuController.getJumlahStok(id)
        if menu != None:
            return jsonify(menu)
        else:
            return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@menuRoutes.route('/foto/<id>', methods=['GET'])
def get_foto_menu(id):
    try:
        menu = menuController.getMenuFoto(id)
        if menu != None:
            return jsonify(menu)
        else:
            return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@menuRoutes.route('/add', methods=['POST'])
def add_menu():
    try:
        menu = menuController.createMenu()
        if menu != None:
            return jsonify(menu)
        else:
            return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@menuRoutes.route('/update/nama/<id>', methods=['PUT'])
def update_menu_nama(id):
    try:
        menuController.setMenuNama(id)
        return jsonify({'Pesan': "Nama Menu Berhasil Diperbarui!"})

    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@menuRoutes.route('/update/harga/<id>', methods=['PUT'])
def update_menu_harga(id):
    try:
        menuController.setHarga(id)
        return jsonify({'Pesan': "Harga Menu Berhasil Diperbarui!"})

    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@menuRoutes.route('/update/jumlah-stok/<id>', methods=['PUT'])
def update_menu_jumlahStok(id):
    try:
        menuController.setJumlahStok(id)
        return jsonify({'Pesan': "Jumlah Stok Menu Berhasil Diperbarui!"})

    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 50

@menuRoutes.route('/update/foto/<id>', methods=['PUT'])
def update_menu_foto(id):
    try:
        menuController.setMenuFoto(id)
        return jsonify({'Pesan': "Foto Menu Berhasil Diperbarui!"})

    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 50

@menuRoutes.route('/delete/<id>', methods=['DELETE'])
def delete_menu(id):
    try:
        menuController.deleteMenu(id)
        return jsonify({'Pesan': "Menu Berhasil Dihapus!"})

    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 50