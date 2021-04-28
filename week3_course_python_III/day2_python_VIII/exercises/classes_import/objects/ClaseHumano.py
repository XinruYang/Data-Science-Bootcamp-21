class Humano: 
    def __init__(self, nombre, armadura, nivel, ataque, salud=100, ojos=2, piernas=2, dientes=32):
        self.nombre = nombre
        self.armadura = armadura
        self.nivel = nivel
        self.ataque = ataque
        self.salud = salud
        self.ojos = ojos
        self.piernas = piernas
        self.dientes = dientes

    def atacaque_a_orco(self,Orco):
        Orco.salud= Orco.salud - (self.ataque - Orco.armadura)
        print(Orco.salud)
        return Orco.salud

    def no_vive_humano(self, vida):
        if self.salud <= 0: 
            return True
        else:
            return False
    
    def atributos_humano(self):
        print(f"Nombre: {self.nombre} | Armadura: {self.armadura} | Nivel: {self.nivel} | Ataque: {self.ataque} | Salud: {self.ojos} | Piernas: {self.dientes}")