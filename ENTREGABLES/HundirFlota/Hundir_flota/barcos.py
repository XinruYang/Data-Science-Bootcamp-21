import pandas as pd

#Definimos la Clase Barco con la función colocar barco, la cual coloca los barcos en el tablero:

# df = tablero1
# size = dimensiones del barco ( pequeño: 2, mediano: 3, grande: 4, gigante: 5)
# fil = fila
# col = columna

tablero1 = pd.DataFrame({1: "~", 2: "~",3: "~",4: "~",5: "~",6: "~",7: "~",8: "~",9: "~",10: "~"},index=[1, 2,3,4,5,6,7,8,9,10])
tablero2 = pd.DataFrame({1: "~", 2: "~",3: "~",4: "~",5: "~",6: "~",7: "~",8: "~",9: "~",10: "~"},index=[1, 2,3,4,5,6,7,8,9,10])


class Barco: 
    def __init__(self, df): 
        self.df = df

    def colocar_barco(self, size, df): # Introducimos el DataFrame (tablero que escogemos) y el size
        self.size = size

        fil = int(input("Introduce la coordenada fila")) 
        col = int(input("Introduce la coordenada columna"))

# Si tenemos ya barco en la coordenada introducida:
        if df.loc[fil,col] == "#" : 
            print("Ops! There´s already a boat,try again!")


        else:

# Pedimos cómo queremos colocar el barco a partir de la coordenada inicial:
            h_v = input("escribe 'h' si quieres horizontal o 'v' si quieres vertical")

# Ponemos las condiciones para que el barco no se sobreponga o no se sobresalga del tablero para el caso horizontal: 
            if h_v == "h":

                if col == 10:
                    print("You´re out of range")

                elif size == 5 and (col == 7 or col == 8 or col == 9):
                    print("You´re out of range")
                
                elif size == 4 and (col == 9 or col == 8):
                    print("You´re out of range")
                
                elif size == 3 and (col == 9):
                    print("You´re out of range")

                elif size == 2 and df.loc[fil,col + 1 ] == "#": 
                    print("You´re crushing with another boat. Try again!")
                
                elif size == 3 and (df.loc[fil,col + 1 ] == "#" or df.loc[fil,col + 2] == "#"):
                    print("You´re crushing with another boat. Try again!")
                
                elif size == 4 and (df.loc[fil,col + 1 ] == "#" or df.loc[fil,col + 2] == "#" or df.loc[fil,col + 3] == "#"):
                    print("You´re crushing with another boat. Try again!")

                elif size == 5 and (df.loc[fil,col + 1 ] == "#" or df.loc[fil,col + 2] == "#" or df.loc[fil,col + 3] == "#" or df.loc[fil,col + 4] == "#"):
                    print("You´re crushing with another boat. Try again!")

# Si todo está bien, entonces rellena el tablero con el barco indicado:
                else:
                    fil = fil 
                    col_f = col + size - 1
            
                    df.loc[fil,col:col_f] = "#"
                    print(tablero1)
                    return df
        

# Ponemos las condiciones para que el barco no se sobreponga o no se sobresalga del tablero para el caso horizontal: 
            if h_v == "v":

                if fil == 10:
                    print("You´re out of range")
                
                elif size == 5 and (fil == 7 or fil == 8 or fil == 9):
                    print("You´re out of range")
                
                elif size == 4 and (fil == 9 or fil == 8):
                    print("You´re out of range")
                
                elif size == 3 and (fil == 9):
                    print("You´re out of range")

                elif size == 2 and (df.loc[fil + 1, col] == "#"): 
                    print("You´re crushing with another boat. Try again!")
                
                elif size == 3 and (df.loc[fil + 1, col] == "#" or df.loc[fil + 2, col] == "#"):
                    print("You´re crushing with another boat. Try again!")
                
                elif size == 4 and (df.loc[fil + 1, col] == "#" or df.loc[fil + 2, col] == "#" or df.loc[fil + 3, col] == "#"):
                        print("You´re crushing with another boat. Try again!")

                elif size == 5 and (df.loc[fil + 1, col] == "#" or df.loc[fil + 2, col] == "#" or df.loc[fil + 3, col] == "#" or df.loc[fil + 4 , col] == "#"):
                        print("You´re crushing with another boat. Try again!")

# Si todo está bien, entonces rellena el tablero con el barco indicado:
                else: 
                    fil_f = fil + size -1
                    col = col
                    df.loc[fil:fil_f,col] = "#"
                    print(tablero1)
                    return df


barco_pequeño = Barco(tablero1)
barco_mediano = Barco(tablero1)
barco_grande = Barco(tablero1)
barco_gigante = Barco(tablero1)

# Definimos una función para que te vaya pidiendo los barcos que hay que colocar:
# n_barcos = número de barcos que hay que introducir
# tamaño: pequeño, mediano, grande o gigante
# n: la dimensión del barco (2, 3, 4, 5)
# tablero: el tablero sobre el que colocamos los barcos

def coloca_tus_barcos(n_barcos,barco,tamaño,n, tablero):
    contador = 1
    print("contador1:", contador)
    while contador < n_barcos: 
        print(f'Coloca el barco{contador} de tamaño {tamaño} en el tablero')
        
        if type(barco.colocar_barco(n,tablero1)) != pd.core.frame.DataFrame:
            print("Try Again!") 
            contador -= 1
        contador += 1

    return tablero

def coloca_jugador1():
    coloca_tus_barcos(2, barco_gigante, "gigante", 5, tablero1)
    coloca_tus_barcos(3, barco_grande, "grande", 4, tablero1)
    coloca_tus_barcos(4, barco_mediano, "mediano", 3, tablero1)
    coloca_tus_barcos(5, barco_pequeño, "pequeño", 2, tablero1)

def coloca_jugador2():
    coloca_tus_barcos(2, barco_gigante, "gigante", 5, tablero2)
    coloca_tus_barcos(3, barco_grande, "grande", 4, tablero2)
    coloca_tus_barcos(4, barco_mediano, "mediano", 3, tablero2)
    coloca_tus_barcos(5, barco_pequeño, "pequeño", 2, tablero2)