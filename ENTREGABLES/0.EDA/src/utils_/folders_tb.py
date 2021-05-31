import pandas as pd 

# Fucntions to store the df 
def create_csv(data, route):
    return data.to_csv(route, index=False)

def create_json(data, route):
    return data.to_json(route)

# Function to read another file 
def read(filepath):
    df = pd.read_csv(filepath)
    return df



