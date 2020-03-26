class Texto:
    texto = ""
    def __init__(self, texto):
        self.texto = texto

    def verificar_palindromo(self):
        palindromo = str(self.texto).lower().replace(' ','')
        verificar = palindromo == palindromo[::-1]
        if(verificar == True):
            print("El texto ingresado es palindromo")
        else:
            print("El texto ingresado no es palindromo")

print("Programa que verifica si un texto es palindromo o no")
while True:
    palabra = input("Ingrese un texto: ")
    texto1 = Texto(palabra)
    texto1.verificar_palindromo()
    cerrar = input("Si desea salir ingrese 0: ")
    str(cerrar)
    if cerrar == "0":
        break