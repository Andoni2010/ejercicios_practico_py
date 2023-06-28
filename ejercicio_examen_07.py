# Definir una funcion generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n

def generar_n_caracteres(caracter, n):
    string = caracter
    print(string * n)
    """
    for i in range(1, n):
        string += caracter

    print(string)
    """
generar_n_caracteres("x", 3)
