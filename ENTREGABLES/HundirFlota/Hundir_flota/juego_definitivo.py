import pandas as pd 
import random
import hundir


import time
turno = 1

hundir.func_random(input("Nombre 1"),input("Nombre 2"))
print()
print("Coloca jugador1""\n")
hundir.coloca_jugador1()
print()
print("Coloca jugador2""\n")
hundir.coloca_jugador2()

while "#" in hundir.tablero1.values or "#" in hundir.tablero2.values:

    print("Turno:", turno)
    time.sleep(1)
    print("Ataca jugador1")
    hundir.jugador1.atacar(jugador2)
    print("Ataca jugador 2")
    hundir.jugador2.atacar(jugador1)
    turno = turno + 1
    print("---------")

else:
    print("game over bitch")


while True:

    print("Turno:", turno)
    time.sleep(1)
    print("Ataca jugador1")
    jugador1.atacar(jugador2)
    print("Ataca jugador 2")
    jugador2.atacar(jugador1)
    turno = turno + 1
    print("---------")

else:
    print("game over bitch")

