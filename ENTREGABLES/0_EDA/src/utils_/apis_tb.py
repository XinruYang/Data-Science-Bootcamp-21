import json
import pandas as pd 

# Function to read a json
def read_json(fullpath):
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    return json_readed 

# Function to return a json
def return_json(filepath):
    df = pd.read_csv(filepath)
    return df.to_json()
