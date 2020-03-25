import math
class Cuadratica:
    tipo_raiz = 0
    disc = 0
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.discriminante()
    def discriminante(self):
        if self.a != 0:
            self.disc = ((self.b ** 2) - (4 * self.a * self.c))
            if self.disc == 0:
                self.tipo_raiz = 0
            elif self.disc > 0:
                self.tipo_raiz = 1
            else:
                self.tipo_raiz = -1
        else:
            print("No es una ecuacion cuadratica ya que el coeficiente de x^2 es 0")
    def solucion(self):
        if(self.tipo_raiz==0):
            self.raices_iguales()
        elif(self.tipo_raiz==1):
            self.raices_normales()
        else:
            self.raices_imaginarias()
    def raices_iguales(self):
        x1 = x2 = (-self.b / (2 * self.a))
        print("El discriminante es cero, por lo cual tiene una unica solucion.")
        print("El resultado de la ecuacion es: ")
        print("x1 = ", x1)
        print("x2 = ", x2)
    def raices_normales(self):
        x1 = (((-1 * (self.b)) - math.sqrt(self.disc)) / 2 * self.a);
        x2 = (((-1 * (self.b)) + math.sqrt(self.disc)) / 2 * self.a);
        print("El discriminante es mayor a cero, por lo cual tiene dos soluciones reales.")
        print("EL resultado de la ecuacion es:")
        print("x1 = ", x1)
        print("x2 = ", x2)
    def raices_imaginarias(self):
        x1 = (-self.b + (self.disc)) / (2 * self.a);
        x2 = (-self.b + -(self.disc)) / (2 * self.a);
        print("El discriminante es menor a cero, por lo cual tiene dos soluciones.")
        print("El resultado de la ecuacion es:")
        print("x1 = ", x1, " + ", x2, " i ")
        print("x2 = ", x1, " - ", x2, " i ")


print("Programa para calcular la solucion de la ecuacion expresada de la siguiente manera ax^2+bx+c=0")
print("----------------------------------------------------------------------------------------------")
print("Ingrese los valores de los coeficientes(a, b y c) de la ecuacion")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
respuesta = Cuadratica(a,b,c)
respuesta.solucion()
