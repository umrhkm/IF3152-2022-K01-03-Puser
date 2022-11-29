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


from server.controllers.pesananControllers import pesananController

pesananRoutes = Blueprint('pesananRoutes', __name__)


@pesananRoutes.route('/', methods=['GET'])
def get_pesanan():
    try:
        pesanan = pesananController.getAllPesanan()
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@pesananRoutes.route('/<id>', methods=['GET'])
def get_pesanan_by_id(id):
    try:
        pesanan = pesananController.getPesananDataById(id)
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@pesananRoutes.route('/<id_pesanan>/<id_menu>', methods=['GET'])
def get_menu_pesanan_by_id(id_pesanan, id_menu):
    try:
        pesanan = pesananController.getMenuPesananDataById(id_pesanan, id_menu)
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@pesananRoutes.route('/kuantitas/<id_pesanan>/<id_menu>', methods=['GET'])
def get_kuantitas(id_pesanan, id_menu):
    try:
        pesanan = pesananController.getKuantitas(id_pesanan, id_menu)
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@pesananRoutes.route('/catatan/<id_pesanan>/<id_menu>', methods=['GET'])
def get_catatan(id_pesanan, id_menu):
    try:
        pesanan = pesananController.getCatatan(id_pesanan, id_menu)
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@pesananRoutes.route('/update/kuantitas/<id_pesanan>/<id_menu>', methods=['PUT'])
def update_kuantitas(id_pesanan, id_menu):
    try:
        pesanan = pesananController.setKuantitas(id_pesanan, id_menu)
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@pesananRoutes.route('/update/catatan/<id_pesanan>/<id_menu>', methods=['PUT'])
def update_catatan(id_pesanan, id_menu):
    try:
        pesanan = pesananController.setCatatan(id_pesanan, id_menu)
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@pesananRoutes.route('/add', methods=['POST'])
def add_pesanan():
    try:
        pesanan = pesananController.createPesanan()
        if pesanan is not None:
            return jsonify(pesanan)

        return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@pesananRoutes.route('/delete/<id>', methods=['DELETE'])
def delete_pesanan(id):
    try:
        pesananController.deletePesanan(id)
        return jsonify({'Pesan': "Pesanan Berhasil Dihapus!"})

    except Exception as err:
        return jsonify({'Pesan': str(err)}), 50


@pesananRoutes.route('/delete/<id_pesanan>/<id_menu>', methods=['DELETE'])
def delete_menu_in_pesanan(id_pesanan, id_menu):
    try:
        pesananController.deleteMenuInPesanan(id_pesanan, id_menu)
        return jsonify({'Pesan': "Menu Pada Pesanan Berhasil Dihapus!"})

    except Exception as err:
        return jsonify({'Pesan': str(err)}), 50
