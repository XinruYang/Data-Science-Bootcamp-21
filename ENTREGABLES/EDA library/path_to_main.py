import os
import sys
def path_(n):
    ruta = __file__
    for i in range(n):
        ruta = os.path.dirname(ruta)
        sys.path.append(ruta)
    return ruta