# ------------------------------ Import the necessary libraries ------------------------------------

from flask import Flask, request, render_template
import os,sys
import argparse
import json
from flask import Flask

# ---------------------------------------------------------------------------------------------------

# Access to the folder and append the path

dir = os.path.dirname
src_path = dir(dir(__file__))
sys.path.append(src_path)

# ------------------------------- Import functions from apis_tb -------------------------------------

from utils_.apis_tb import read_json, return_json
from utils_.sql_tb import MySQL, upload_sql

# ---------------------------------------- Create Flask ---------------------------------------------

app = Flask(__name__)

@app.route("/") 
def home():
    """ Default path """
    return "Alzheimer detection project"

@app.route('/give_me_id', methods=['GET']) # localhost:8080/give_me_id?token_id=T79045618
# Returns the json with the information of my df
def give_id():
    x = request.args['token_id']
    if x == "T79045618": 
        return return_json(dir(__file__) + os.sep + "static" + os.sep + "dataframe.csv")
    else:
        return "Wrong password"

@app.route('/mysql', methods=['GET']) # localhost:8080/mysql?upload=yes
# This function inserts to mySQL the df
def mysql():
    x = request.args['upload']
    if x == "yes":
        settings_file = dir(dir(__file__)) + os.sep + "utils_" + os.sep + "bd_info.json" # Path to bd_info.json
        json_readed = read_json(settings_file) # Imported from apis_tb, read json
        route = dir(__file__) + os.sep + "static" + os.sep + "dataframe.csv"
        upload_sql("xinru_yang_wang", route, json_readed)
        return "Successfully uploaded"

    else:
        return "Insert 'upload=yes' to insert the data in SQL"


def main():
    
    settings_file = dir(__file__) + os.sep + "settings.json"
    
    # Load json from file
    json_readed = read_json(fullpath=settings_file)

    DEBUG = json_readed["debug"]
    HOST = json_readed["host"]
    PORT_NUM = json_readed["port"] 

    app.run(debug=DEBUG, host=HOST, port=PORT_NUM)

parser = argparse.ArgumentParser()
parser.add_argument("-x", "--x", type=str, help="password") # Important! --> type

if __name__ == "__main__": 

    # To run in cmd : python C:\Users\xyang\OneDrive\Escritorio\ARCHIVOS\THEBRIDGE\Data-Science-Bootcamp-21\ENTREGABLES\00_POYECTO_ML\src\api\server.py -x "Xinru"
    args = vars(parser.parse_args())
    print(args.values())
    if args["x"] == "Xinru": 
        main()
    else:
        print("wrong password")