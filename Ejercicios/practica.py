import matplotlib.pyplot as plt
contador = 0
mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnopqrstuvwxyz'
def agregar_campo(matriz):
    matriz.append([])
    tam_matriz = len(matriz)
    for _ in range(9):
        matriz[tam_matriz - 1].append(0)
    return matriz

def estacion(contador, derecha):
    matriz[contador][0] = (input("Introduzca la estacion: "))
    p_visado(contador, derecha)
    contador = contador + 1
    return  contador

def p_visado(contador, derecha):
    punto_visado = str(input("Introduzca el punto visado: "))
    matriz[contador][1] = punto_visado
    if contador == 0:
        matriz[contador][5] = float(input("Ingrese cota principal: "))
        vista_mas(contador)
        cota_hi(contador)
        distancias_b(contador, derecha)
    elif matriz[contador][1] in mayusculas: 
        vista_mas(contador)
        vista_menos(contador)
        distancias(contador)
        cota(contador)
        cota_hi(contador)
        distancias_a(contador)
        distancias_b(contador, derecha)

    elif matriz[contador][1] in minusculas:
        vista_menos(contador)
        cota(contador)
        distancias(contador)
        distancias_a(contador)
        distancias_b(contador, derecha)
    else:
        vista_menos(contador)
        distancias(contador)
        cota(contador)
        distancias_a(contador)
        distancias_b(contador, derecha)


def cota(contador):
    ultima_cota_hi = 0
    contador_temp = contador
    while(ultima_cota_hi == 0):
        ultima_cota_hi = matriz[contador_temp][4]
        contador_temp -= 1
    matriz[contador][5] = ultima_cota_hi - matriz[contador][3]

def distancias(contador):
    matriz[contador][6] = float(input("Ingrese la distancia: "))
def distancias_a(contador):
    distancias_a_temp = 0
    contador_temp = contador
    while(matriz[contador_temp][1] not in mayusculas):
        contador_temp -= 1
    distancias_a_temp = matriz[contador_temp][7]
    if matriz[contador][0] == matriz[0][0]:
        matriz[contador][7] = matriz[contador][6]
    elif matriz[contador][1] in mayusculas:
        matriz[contador][7] = matriz[contador][6]
    else:
        matriz[contador][7] = matriz[contador][6]+distancias_a_temp
def distancias_b(contador, derecha):
    if contador == 0:
        matriz[contador][8] = float(input("Ingrese la distanciaB: "))
    elif derecha == True:
        matriz[contador][8] = matriz[contador][7]+matriz[contador-1][8]
    else:
        matriz[contador][8] = matriz[contador-1][8]-matriz[contador][7]

def cota_hi(contador):
    matriz[contador][4] = matriz[contador][2] + matriz[contador][5]

def vista_mas(contador):
    matriz[contador][2] = float(input("Introduzca la vista +: "))

def vista_menos(contador):
    matriz[contador][3] = float(input("Introduzca la vista -: "))

matriz =[]
derecha = True
inicio = True
while inicio:   
    opcion = str(input("Desea ingresar datos? (S/N): "))
    if opcion == "N":
        inicio = False
    else:
        matriz = agregar_campo(matriz)
        contador = estacion(contador,derecha)
print (matriz)
matriz_temp=matriz
matriz = []
contador = 0
inicio = True
derecha = False
while inicio:   
    opcion = str(input("Desea ingresar datos? (S/N): "))
    if opcion == "N":
        inicio = False
    else:
        matriz = agregar_campo(matriz)
        contador = estacion(contador, derecha)
matriz_invertida = matriz[::-1]
cotas = []
distancias_g = []

for i in range(len(matriz_invertida)):
    cotas.append(matriz_invertida[i][5])
for i in range(len(matriz_invertida)):
    distancias_g.append(matriz_invertida[i][8])

for i in range(1,len(matriz_temp)):
    cotas.append(matriz_temp[i][5])
for i in range(1,len(matriz_temp)):
    distancias_g.append(matriz_temp[i][8])

plt.plot(distancias_g, cotas)
plt.show()