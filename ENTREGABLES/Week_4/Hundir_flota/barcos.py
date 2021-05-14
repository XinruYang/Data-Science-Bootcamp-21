class Barco:
    def __init__(self, size): 
        self.size = size

    def colocar_barco(self, size):
    
        fil = int(input("Introduce la coordenada fila"))
        col = int(input("Introduce la coordenada columna"))

        h_v = input("write horizontal o vertical")

        if h_v == "horizontal":
            fil = fil 
            col_f = col + size + 1
            df.loc[fil,col:col_f] = "#"

        if h_v == "vertical":
            fil_f = fil + size + 1
            col = col
            df.loc[fil:fil_f,col] = "#"

        return df