from flask import Flask
from threading import Thread
import sys

# Routes
from server.routes import menuRoutes
from server.routes import pesananRoutes
from server.routes import detailPesananRoutes


app = Flask(__name__)
app.debug = True

def loadBackend():
    #Blueprint
    app.register_blueprint(menuRoutes.menuRoutes, url_prefix='/api/menus')
    app.register_blueprint(pesananRoutes.pesananRoutes, url_prefix='/api/pesanan')
    app.register_blueprint(detailPesananRoutes.detailPesananRoutes, url_prefix='/api/detail-pesanan')

    app.run(port=5000, use_reloader=False)

if __name__ == '__main__':
    # #Dipakai kalau front-end udah siap
    threadBackend = Thread(target=loadBackend)
    threadBackend.setDaemon(True)
    threadBackend.start()

    import client.controller as cont
    from PyQt6.QtWidgets import QApplication

    window = QApplication(sys.argv)
    controller = cont.Controller()
    controller.start()
    sys.exit(window.exec())