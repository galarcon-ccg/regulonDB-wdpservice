
ejecucion en entorno virtual (venv)
 to install
- sudo apt install python3-venv
- python3 -m venv venv
to activate
. venv/bin/activate

dependencias
- flask
- "graphene>=3.0"
- flask-cors
- csv
to install on venv
(venv) 
pip install flask flask-cors "graphene>=3.0"

Ejecutar
- export FLASK_APP=app.py
- export FLASK_APP=app.py
- flask run --host=0.0.0.0