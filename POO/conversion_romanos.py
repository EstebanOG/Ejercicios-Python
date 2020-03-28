import math
class Romanos:
    Unidades= ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    Decenas = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    Centenas = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    unidades=0
    decenas=0
    centenas=0
    def __init__(self, numero):
        self.numero = numero

    def convertir_romano(self):
        self.unidades = self.numero % 10
        self.decenas = int(math.floor(self.numero/ 10)) % 10
        self.centenas = int(math.floor(self.numero/ 100))

    def mostrar_romano(self):
        if self.numero == 1000:
            print("M")
        elif self.numero >= 100:
            print(self.Centenas[self.centenas] + self.Decenas[self.decenas] + self.Unidades[self.unidades])
        elif self.numero >= 10:
            print(self.Decenas[self.decenas] + self.Unidades[self.unidades])
        else:
            print(self.Unidades[self.unidades])

print("Programa para convertir números arábigos a números romanos")
while True:
    while True:
        numero = int(input("Ingrese un numero entero mayor que 0 y menor que 1001: "))
        if numero > 0 and numero< 1001:
            break
    romano1 = Romanos(numero)
    romano1.convertir_romano()
    romano1.mostrar_romano()
    cerrar = input("Si desea salir ingrese 0: ")
    str(cerrar)
    if cerrar == "0":
        break