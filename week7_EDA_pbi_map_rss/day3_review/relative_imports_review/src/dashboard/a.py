import sys
import os

print("sys path inicial: ", sys.path)
dir = os.path.dirname
src_path = dir(dir(__file__)) # Estamos subiendo dos veces, porque estamos en b, no en utils
src_path = src_path.replace("/", os.sep) + os.sep
print("---------------------------------------------------")

print("src_path:",src_path)
sys.path.append(src_path)

print("---------------------------------------------------")
print("sys.path:", sys.path)

import utils.c 

print("---------------------------------------------------")
print()

def function_a():
    print("function a")
    return function_c()

if __name__ == "__main__":
    function_a()
