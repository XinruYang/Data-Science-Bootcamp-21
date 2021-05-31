from flask import Flask, request, render_template
from pepito.functions import read_json
import os

# Mandatory
app = Flask(__name__)  # __name__ --> __main__  

# ---------- Flask functions ----------
@app.route("/")  # @ --> esto representa el decorador de la función, ("/") --> es el que se carga por defecto
def home():
    """ Default path """
    return app.send_static_file('greet.html')

@app.route("/greet")
def greet():
    username = request.args.get('name') # Estamos recogiendo "name" en greet, cuando le doy a subbmit en la pag 
    return render_template('index.html', name=username) # Estamos cargando el archivo html y estamos pasando el valor de name

@app.route("/info")
def create_json():
    return 'Tienes que acceder al endpoint "/give_me_id" pasando por parámetro "password" con la contraseña correcta' 

# localhost:6060/give_me_id?password=
@app.route('/give_me_id', methods=['GET'])
def give_id():
    x = request.args['password']
    if x == "12345": # Esto es al introducir una contraseña 
        return request.args
    else:
        return "No es la contraseña correcta"

@app.route("/recibe_informacion")
def recibe_info():
    return'{"columna1": "0", "columna2": "8"}'

# ---------- Other functions ----------

def main():
    print("---------STARTING PROCESS---------")
    print(__file__)
    
    # Get the settings fullpath
    # \\ --> WINDOWS
    # / --> UNIX
    # Para ambos: os.sep
    settings_file = os.path.dirname(__file__) + os.sep + "settings.json"
    print(settings_file)
    # Load json from file
    json_readed = read_json(fullpath=settings_file)
    
    # Load variables from jsons

    DEBUG = json_readed["debug"]
    HOST = json_readed["host"]
    PORT_NUM = json_readed["port"] 

    # Dos posibilidades: 
    # 1) HOST = "0.0.0.0" # Esto estoy escuchando desde fuera, es público
    # 2) HOST = "127.0.0.1" Los que están conectados a la red privada pueden acceder. Para el proyecto vale

    app.run(debug=DEBUG, host=HOST, port=PORT_NUM)

if __name__ == "__main__":
    main()