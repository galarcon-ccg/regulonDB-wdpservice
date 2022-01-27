
ejecucion en entorno virtual (venv)
 to install
- sudo apt install python3-venv
- python3 -m venv venv
to activate
. venv/bin/activate

dependencias
- flask
- sgqlc
- flask-cors
- csv
- python-dotenv
to install on venv
(venv) 
pip install flask flask-cors sgqlc python-dotenv

Ejecutar
- export FLASK_APP=app.py
- flask run --host=0.0.0.0