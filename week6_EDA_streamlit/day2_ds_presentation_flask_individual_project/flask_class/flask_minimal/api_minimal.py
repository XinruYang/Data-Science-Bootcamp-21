from flask import Flask, flash, request, render_template, redirect, url_for
import pandas as pd
import os
import json

UPLOAD_FOLDER = os.sep + "static" + os.sep # Estamos apuntando a la carpeta static


# Flask es una clase
app = Flask(__name__) # Para decirle que estamos haciendo un archivo Flask
# Aquí __name__ es sinónimo de "__main__", es el nombre del archivo que estoy ejecutando

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # Apunta a la carpeta donde se van a guardar las cosas 
app.secret_key = 'hellohello' # Atributo que es necesario para interactuar si quiero subir cosas



options = {"Genre_list":["hola", "adios"],
"Platform_list":[1,2,3,4,5,6],
"Publisher_list":['Clara', 'Borja', 'Gabriel']}

# Tenemos dos funciones que son accesibles desde la API, yo en algun momento desde la URL puedo acceder a alguna de estas funciones


@app.route("/") # Esta es la que se va a ejecutar por defecto
def home():
    return render_template("upload.html", 
                           Genre_list = options["Genre_list"],
                           Platform_list= options["Platform_list"], 
                           Publisher_list= options["Publisher_list"]) # Esto pasa a upload HTML
    
@app.route("/upload_form", methods = ['POST', 'GET']) # POST: añadir información, GET:enviar información 
def upload_form(): 
    if request.method == 'POST': 
        genre_res = request.form['Genre']
        platform_res= request.form['Platform']
        publisher_res = request.form['Publisher']
        all_returned = str(genre_res) + str(platform_res) + str(publisher_res)
        return json.dumps({"genre": genre_res,
                            "platform": platform_res,
                            "publisher": publisher_res,
                            "all_returned": all_returned})

if __name__ == '__main__': 
    # host='127.0.0.1' --> No permite recibir llamadas desde el exterior
    # host='0.0.0.0' --> Permite recibir llamadas desde el exterior
    # si 0.0.0.0 no funciona externamente desde la IP privada de tu PC
    # es que tu ordenador o del dispositivo desde el que se accede 
    # tiene bloqueada la conexión (antivirus / firewall)
    app.run(host='0.0.0.0',port=os.getenv("PORT", 1991), debug=True) # app es la instancia de la clase Flask, hacemos un run. debug=True: si me da un error que me lo muestr

    # host=0.0.0.0, vamos a permitir que nuestro ordenador sea público, no significa que podamos de acceder de cualquier sitio.
    # 127.0.1.0 esto es privado 
    # Para acceder a mi ordenador: 1) poner en internet