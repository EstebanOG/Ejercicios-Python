class Matriz:
    matriz_a = []
    matriz_b = []
    matriz_c = []
    filas_a = 0
    columnas_a = 0
    filas_b = 0
    columnas_b = 0
    def llenar_matriz_a(self):
        print("Matriz A")
        self.filas_a = int(input("Introduce el numero de filas: "))
        self.columnas_a = int(input("Introduce el numero de columnas: "))
        for i in range(self.filas_a):
            self.matriz_a.append([])
            for j in range(self.columnas_a):
                valor = float(input("Fila {}, Columna {} : ".format(i+1,j+1)))
                self.matriz_a[i].append(valor)
        return self.matriz_a

    def llenar_matriz_b(self):
        print("Matriz B")
        self.filas_b = int(input("Introduce el numero de filas: "))
        self.columnas_b = int(input("Introduce el numero de columnas: "))
        for i in range(self.filas_b):
            self.matriz_b.append([])
            for j in range(self.columnas_b):
                valor = float(input("Fila {}, Columna {} : ".format(i+1,j+1)))
                self.matriz_b[i].append(valor)
        return self.matriz_b

    def sumar_matrices(self):
        if self.filas_a == self.filas_b and self.columnas_a == self.columnas_b:
            for i in range(self.filas_a):
                self.matriz_c.append([])
                for j in range(self.columnas_a):
                    self.matriz_c[i].append(self.matriz_a[i][j] + self.matriz_b[i][j])
            return self.matriz_c
        else:
            return None

    def restar_matrices(self):
        if self.filas_a == self.filas_b and self.columnas_a == self.columnas_b:
            for i in range(self.filas_a):
                self.matriz_c.append([])
                for j in range(self.columnas_a):
                    self.matriz_c[i].append(self.matriz_a[i][j] - self.matriz_b[i][j])
            return self.matriz_c
        else:
            return None

    def multiplicar_matrices(self):
        if self.columnas_a == self.filas_b:
            for i in range(self.filas_a):
                self.matriz_c.append([])
                for j in range(self.columnas_b):
                    self.matriz_c[i].append(0)
            for i in range(self.filas_a):
                for j in range(self.columnas_b):
                    for k in range(self.columnas_a):
                        self.matriz_c[i][j] += self.matriz_a[i][k] * self.matriz_b[k][j]
            return self.matriz_c
        else:
            return  None
    def traspuesta(self):
        for i in range(self.columnas_a):
            self.matriz_c.append([])
            for j in range(self.filas_a):
                self.matriz_c[i].append(self.matriz_a[j][i])
        return self.matriz_c
    def mostrar_matriz(self, matriz):
        for fila in matriz:
            print("[", end=" ")
            for elemento in fila:
                print(elemento, end=" ")
            print("]")

while True:
    print("Calculadora de matrices")
    print("1.Suma"+'\n'"2.Resta"+'\n'+"3.Multiplicacion"+'\n'+"4.Traspuesta")
    matriz_a = []
    matriz_b = []
    matriz_c = []
    while True:
        opcion = int(input("Elija una opcion: "))
        if opcion == 1:
            suma = Matriz()
            matriz_a = suma.llenar_matriz_a()
            matriz_b = suma.llenar_matriz_b()
            matriz_c = suma.sumar_matrices()
            if matriz_c == None:
                print("No se pueden sumar")
            else:
                suma.mostrar_matriz(matriz_c)
        elif opcion == 2:
            resta = Matriz()
            matriz_a = resta.llenar_matriz_a()
            matriz_b = resta.llenar_matriz_b()
            matriz_c = resta.restar_matrices()
            if matriz_c == None:
                print("No se pueden restar")
            else:
                resta.mostrar_matriz(matriz_c)
        elif opcion == 3:
            multiplicacion = Matriz()
            matriz_a = multiplicacion.llenar_matriz_a()
            matriz_b = multiplicacion.llenar_matriz_b()
            matriz_c = multiplicacion.multiplicar_matrices()
            if matriz_c == None:
                print("No se pueden multiplicar")
            else:
                multiplicacion.mostrar_matriz(matriz_c)
        elif opcion == 4:
            traspuesta = Matriz()
            matriz_a = traspuesta.llenar_matriz_a()
            matriz_c = traspuesta.traspuesta()
            traspuesta.mostrar_matriz(matriz_c)
        else:
            opcion = 5
            print("La opción es invalida")
        if opcion != 5:
            break
    cerrar = int(input("Si desea salir ingrese 0: "))
    if cerrar == 0:
        break