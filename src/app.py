from flask import Flask
from threading import Thread
import sys

# Routes
from server.routes import menuRoutes

app = Flask(__name__)
app.debug = True

def loadBackend():
    #Blueprint
    app.register_blueprint(menuRoutes.menuRoutes, url_prefix='/api/menus')

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