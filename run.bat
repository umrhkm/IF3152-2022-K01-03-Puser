@ECHO OFF
CD src
START python app.py
CD client
START python dita_window.py
EXIT