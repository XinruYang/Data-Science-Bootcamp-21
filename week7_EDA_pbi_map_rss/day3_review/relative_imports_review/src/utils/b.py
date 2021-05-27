import sys
import os

# os.getcwd() # --> Lo utilizamos con jupyter notebook
# __file__ --> nos da la ruta al archivo, por lo que siempre hay que subir una vez más que desde jupyter notebook

def utiliza_a():
    pass

if __name__ == "__main__":
    print(__file__)
    dir = os.path.dirname
    src_path = dir(dir(__file__)) # Estamos subiendo dos veces, porque estamos en b, no en utils
    print("")
    print(src_path)
    sys.path.append(src_path)

    from dashboard.a import function_a 
    print(function_a())