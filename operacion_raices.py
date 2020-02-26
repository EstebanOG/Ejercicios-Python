import math
def leer_coeficinetes():
    print("Ingrese los valores de los coeficientes(a, b y c) de la ecuacion")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    return a, b, c
def discriminante(a, b, c):
    if a != 0:
        disc = ((b**2) - (4*a*c))
        if disc == 0:
            tipo_raiz = 0
        elif disc > 0:
            tipo_raiz = 1
        else:
            tipo_raiz = -1
    return tipo_raiz, disc
def raices_iguales():
    x1 = x2 = (-b/(2 * a))
    print("El discriminante es cero, por lo cual tiene una unica solucion.")
    print("El resultado de la ecuacion es: ")
    print("x1 = ",x1)
    print("x2 = ",x2)
def raices_normales():
    x1 = (((-1 * (b)) - math.sqrt(disc)) / 2 * a);
    x2 = (((-1 * (b)) + math.sqrt(disc)) / 2 * a);
    print("El discriminante es mayor a cero, por lo cual tiene dos soluciones reales.")
    print("EL resultado de la ecuacion es:")
    print("x1 = ",x1)
    print("x2 = ",x2)
def raices_imaginarias():
    x1 = (-b + (disc)) / (2 * a);
    x2 = (-b + -(disc)) / (2 * a);
    print("El discriminante es menor a cero, por lo cual tiene una dos soluciones.")
    print("El resultado de la ecuacion es:")
    print("x1 = ", x1 , " + ", x2, " i ")
    print("x2 = ",x1," - ",x2," i ")

print("Programa para calcular la solucion de la ecuacion expresada de la siguiente manera ax^2+bx+c=0")
print("----------------------------------------------------------------------------------------------")
a, b, c = leer_coeficinetes()
tipo_raiz, disc = discriminante(a, b, c)
if(tipo_raiz == 0):
    raices_iguales()
elif(tipo_raiz == 1):
    raices_normales()
elif(tipo_raiz == -1):
    raices_imaginarias()
else:
    print("Opcion invalida")