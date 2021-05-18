import random
import pandas as pd
def func_random(jugador1,jugador2):
    x = random.randint(0,6)
    y = random.randint(0,6)
    print("1º número:", x)
    print("2º número", y)
    if x > y:
        return jugador1
    else:
        return jugador2

func_random(input("Nombre 1"),input("Nombre 2"))
