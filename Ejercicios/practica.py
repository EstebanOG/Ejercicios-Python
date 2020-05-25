contador = 0
mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnopqrstuvwxyz'
def agregar_campo(matriz):
    matriz.append([])
    tam_matriz = len(matriz)
    for _ in range(9):
        matriz[tam_matriz - 1].append(0)
    return matriz

def estacion(contador):
    matriz[contador][0] = (input("Introduzca la estacion: "))
    p_visado(contador)
    contador = contador + 1
    return  contador

def p_visado(contador):
    punto_visado = str(input("Introduzca el punto visado: "))
    matriz[contador][1] = punto_visado
    if contador == 0:
        matriz[contador][5] = float(input("Ingrese cota principal: "))
        vista_mas(contador)
        cota_hi(contador)
        distancias_b(contador)
    elif matriz[contador][1] in mayusculas: 
        vista_mas(contador)
        vista_menos(contador)
        distancias(contador)
        cota(contador)
        cota_hi(contador)
        distancias_a(contador)
        distancias_b(contador)

    elif matriz[contador][1] in minusculas:
        vista_menos(contador)
        cota(contador)
        distancias(contador)
        distancias_a(contador)
        distancias_b(contador)
    else:
        vista_menos(contador)
        distancias(contador)
        cota(contador)
        distancias_a(contador)
        distancias_b(contador)


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
def distancias_b(contador):
    if contador == 0:
        matriz[contador][8] = float(input("Ingrese la distanciaB: "))
    else:
        matriz[contador][8] = matriz[contador][7]+matriz[contador-1][8]

def cota_hi(contador):
    matriz[contador][4] = matriz[contador][2] + matriz[contador][5]

def vista_mas(contador):
    matriz[contador][2] = float(input("Introduzca la vista +: "))

def vista_menos(contador):
    matriz[contador][3] = float(input("Introduzca la vista -: "))

matriz =[]
inicio = True
while inicio:   
    opcion = str(input("Desea ingresar datos? (S/N): "))
    if opcion == "N":
        inicio = False
    else:
        matriz = agregar_campo(matriz)
        contador = estacion(contador)
print (matriz)