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

from flask import Blueprint, jsonify


from server.controllers.menuControllers import menuController

menuRoutes = Blueprint('menuRoutes', __name__)


@menuRoutes.route('/', methods=['GET'])
def get_menus():
    try:
        menus = menuController.getAllMenu()
        return jsonify(menus)
    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@menuRoutes.route('/search-id/<id>', methods=['GET'])
def get_menu_by_id(id):
    try:
        menu = menuController.getMenuDataById(id)
        if menu is not None:
            return (menu)

        return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@menuRoutes.route('/search-nama/<nama>', methods=['GET'])
def get_menu_by_nama(nama):
    try:
        menu = menuController.getMenuDataByNama(nama)
        if menu is not None:
            return jsonify(menu)

        return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@menuRoutes.route('/nama/<id>', methods=['GET'])
def get_nama(id):
    try:
        menu = menuController.getNama(id)
        if menu is not None:
            return jsonify(menu)

        return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@menuRoutes.route('/harga/<id>', methods=['GET'])
def get_harga(id):
    try:
        menu = menuController.getHarga(id)
        if menu is not None:
            return jsonify(menu)

        return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@menuRoutes.route('/kategori/<id>', methods=['GET'])
def get_kategori(id):
    try:
        menu = menuController.getKategori(id)
        if menu is not None:
            return jsonify(menu)

        return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@menuRoutes.route('/jumlah-stok/<id>', methods=['GET'])
def get_jumlahStok(id):
    try:
        menu = menuController.getJumlahStok(id)
        if menu is not None:
            return jsonify(menu)

        return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@menuRoutes.route('/add', methods=['POST'])
def add_menu():
    try:
        menu = menuController.createMenu()
        if menu is not None:
            return jsonify(menu)

        return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@menuRoutes.route('/update/nama/<id>', methods=['PUT'])
def update_menu_nama(id):
    try:
        menuController.setMenuNama(id)
        return jsonify({'Pesan': "Nama Menu Berhasil Diperbarui!"})

    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@menuRoutes.route('/update/harga/<id>', methods=['PUT'])
def update_menu_harga(id):
    try:
        menuController.setHarga(id)
        return jsonify({'Pesan': "Harga Menu Berhasil Diperbarui!"})

    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@menuRoutes.route('/update/jumlah-stok/<id>', methods=['PUT'])
def update_menu_jumlahStok(id):
    try:
        menuController.setJumlahStok(id)
        return jsonify({'Pesan': "Jumlah Stok Menu Berhasil Diperbarui!"})

    except Exception as err:
        return jsonify({'Pesan': str(err)}), 50


@menuRoutes.route('/delete/<id>', methods=['DELETE'])
def delete_menu(id):
    try:
        menuController.deleteMenu(id)
        return jsonify({'Pesan': "Menu Berhasil Dihapus!"})

    except Exception as err:
        return jsonify({'Pesan': str(err)}), 50
