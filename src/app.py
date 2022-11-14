from flask import Flask
from threading import Thread
import sys

# Routes
from server.routes import menuRoutes
from server.routes import pesananRoutes

app = Flask(__name__)
app.debug = True

def loadBackend():
    #Blueprint
    app.register_blueprint(menuRoutes.menuRoutes, url_prefix='/api/menus')
    app.register_blueprint(pesananRoutes.pesananRoutes, url_prefix='/api/pesanan')

    app.run(port=5000, use_reloader=False)

if __name__ == '__main__':
    loadBackend()
    
    #Dipakai kalau front-end udah siap
    # threadBackend = Thread(target=loadBackend)
    # threadBackend.setDaemon(True)
    # threadBackend.start()

    #Front-end, Launch App
    # window = QApplication(sys.argv)
    # sys.exit(window.exec())