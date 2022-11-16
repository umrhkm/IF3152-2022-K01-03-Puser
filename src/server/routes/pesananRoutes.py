from flask import Blueprint, jsonify, request


from server.controllers.pesananControllers import pesananController

pesananRoutes = Blueprint('pesananRoutes', __name__)

@pesananRoutes.route('/', methods=['GET'])
def get_pesanan():
    try:
        pesanan = pesananController.getAllPesanan()
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@pesananRoutes.route('/<id>', methods=['GET'])
def get_pesanan_by_id(id):
    try:
        pesanan = pesananController.getPesananDataById(id)
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@pesananRoutes.route('/<id_pesanan>/<id_menu>', methods=['GET'])
def get_menu_pesanan_by_id(id_pesanan, id_menu):
    try:
        pesanan = pesananController.getMenuPesananDataById(id_pesanan, id_menu)
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@pesananRoutes.route('/kuantitas/<id_pesanan>/<id_menu>', methods=['GET'])
def get_kuantitas(id_pesanan, id_menu):
    try:
        pesanan = pesananController.getKuantitas(id_pesanan, id_menu)
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@pesananRoutes.route('/update/kuantitas/<id_pesanan>/<id_menu>', methods=['PUT'])
def update_kuantitas(id_pesanan, id_menu):
    try:
        pesanan = pesananController.setKuantitas(id_pesanan, id_menu)
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@pesananRoutes.route('/add', methods=['POST'])
def add_pesanan():
    try:
        pesanan = pesananController.createPesanan()
        if pesanan != None:
            return jsonify(pesanan)
        else:
            return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 500

@pesananRoutes.route('/delete/<id>', methods=['DELETE'])
def delete_pesanan(id):
    try:
        pesananController.deletePesanan(id)
        return jsonify({'Pesan': "Pesanan Berhasil Dihapus!"})

    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 50

@pesananRoutes.route('/delete/<id_pesanan>/<id_menu>', methods=['DELETE'])
def delete_menu_in_pesanan(id_pesanan, id_menu):
    try:
        pesananController.deleteMenuInPesanan(id_pesanan, id_menu)
        return jsonify({'Pesan': "Menu Pada Pesanan Berhasil Dihapus!"})

    except Exception as err:
        return jsonify({'Pesan' : str(err)}), 50