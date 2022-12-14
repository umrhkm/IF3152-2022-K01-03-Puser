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


from server.controllers.detailPesananControllers import detailPesananController

detailPesananRoutes = Blueprint('detailPesananRoutes', __name__)


@detailPesananRoutes.route('/', methods=['GET'])
def get_detail_pesanan():
    try:
        pesanan = detailPesananController.getAllDetailPesanan()
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@detailPesananRoutes.route('/<id>', methods=['GET'])
def get_detail_pesanan_by_id(id):
    try:
        pesanan = detailPesananController.getDetailPesananDataById(
            id).getDetailPesananData()
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@detailPesananRoutes.route('/dine-in-status/<id>', methods=['GET'])
def get_dine_in_status(id):
    try:
        pesanan = detailPesananController.getDineInStatus(id)
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@detailPesananRoutes.route('/nomor-meja/<id>', methods=['GET'])
def get_nomor_meja(id):
    try:
        pesanan = detailPesananController.getNomorMeja(id)
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@detailPesananRoutes.route('/update/dine-in-status/<id>', methods=['PUT'])
def update_dine_in_status(id):
    try:
        pesanan = detailPesananController.setDineInStatus(id)
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@detailPesananRoutes.route('/update/nomor-meja/<id>', methods=['PUT'])
def update_nomor_meja(id):
    try:
        pesanan = detailPesananController.setNomorMeja(id)
        return jsonify(pesanan)
    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@detailPesananRoutes.route('/add', methods=['POST'])
def add_detail_pesanan():
    try:
        pesanan = detailPesananController.createDetailPesanan()
        if pesanan is not None:
            return jsonify(pesanan)

        return jsonify({}), 404

    except Exception as err:
        return jsonify({'Pesan': str(err)}), 500


@detailPesananRoutes.route('/delete/<id>', methods=['DELETE'])
def delete_detail_pesanan(id):
    try:
        detailPesananController.deleteDetailPesanan(id)
        return jsonify({'Pesan': "Detail Pesanan Berhasil Dihapus!"})

    except Exception as err:
        return jsonify({'Pesan': str(err)}), 50
