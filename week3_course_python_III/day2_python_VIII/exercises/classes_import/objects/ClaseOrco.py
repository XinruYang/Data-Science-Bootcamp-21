class Orco: 
    def __init__(self, nombre, armadura, nivel, ataque, salud=100, ojos=2, piernas=2, dientes=56):
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.salud = salud
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes

    def ataque_a_humano(self,Humano):
        Humano.salud = Humano.salud - (self.ataque - Humano.armadura)
        print(Humano.salud)
        return Humano.salud

    def no_vvie_orco(self, vida):
        if self.salud <= 0: 
            return True
        else:
            return False
    
    def atributos_orco(self):
        print(f"Nombre: {self.nombre} | Armadura: {self.armadura} | Nivel: {self.nivel} | Ataque: {self.ataque} | Salud: {self.ojos} | Piernas: {self.dientes}")