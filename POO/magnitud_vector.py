import math
class Vector:
    dimension = 0
    coordenadas = []
    norma = 0
    def __init__(self, dimension):
        self.dimension = dimension
        self.coordenadas = []
        self.norma = 0

    def llenar_vector(self):
        for i in range(self.dimension):
            self.coordenadas.append(int(input("Ingrese la coordenada [{}]: ".format(i))))

    def calcular_norma(self):
        for i in range(self.dimension):
            self.norma += self.coordenadas[i]**2
        print("Vector = {}".format(self.coordenadas))
        print("La norma es: {}".format(math.sqrt(self.norma)))
print("Programa para calcular la magnitud de un vector")
while True:
    dimension = int(input("Ingrese la dimensión en la que se encuentra el vector: "))
    vector = Vector(dimension)
    vector.llenar_vector()
    vector.calcular_norma()
    cerrar = input("Si desea salir ingrese 0: ")
    str(cerrar)
    if cerrar == "0":
        break