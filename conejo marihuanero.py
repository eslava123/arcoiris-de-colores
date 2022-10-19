class Conejo:
    def __init__(self, nombre, comida, tamaño, color, edad):
        self.nombre = nombre
        self.comida = comida
        self.tamaño = tamaño
        self.color = color
        self.edad = edad

p1 = Conejo("antonio", "remolacha", "pequeño", "verde", "75")
print (p1.edad)
