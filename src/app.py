# pylint: disable=W4902

'''Importing module'''
import sys
from threading import Thread
from flask import Flask


# Routes
from server.routes import menuRoutes
from server.routes import pesananRoutes
from server.routes import detailPesananRoutes


app = Flask(__name__)
app.debug = True


def load_backend():
    '''Fungsi untuk load backend'''
    app.register_blueprint(menuRoutes.menuRoutes, url_prefix='/api/menus')
    app.register_blueprint(pesananRoutes.pesananRoutes,
                           url_prefix='/api/pesanan')
    app.register_blueprint(
        detailPesananRoutes.detailPesananRoutes, url_prefix='/api/detail-pesanan')

    app.run(port=5000, use_reloader=False)


if __name__ == '__main__':
    threadBackend = Thread(target=load_backend)
    threadBackend.setDaemon(True)
    threadBackend.start()

    import client.controller as cont
    from PyQt6 import QtWidgets

    window = QtWidgets.QApplication(sys.argv)
    controller = cont.Controller()
    controller.start()
    sys.exit(window.exec())
