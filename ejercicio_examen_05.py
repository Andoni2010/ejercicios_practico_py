# Definir una funcion inversa() que calcula la inversion de una cadena
def inversa(cadena): 
    # Esto se hace para poder recorrer la cadena desde el final hasta el principio.
    # Ya que el len si una palabra tiene 4 letras, te dice que tiene 5 por que comienza por el 0
    longitud = -(len(cadena)-1)
    # variable para recoger la cadena invertida
    nueva_cadena = str()
    # el for hace que el bucle recorrerá los índices de la cadena desde el último hasta el segundo.
    for n in range(longitud, 1):
        #El abs se hace para asegurar que el indice sea positivo y valido
        n = abs(n)
        #Se agrega el carácter correspondiente al índice "n" de la cadena original a la variable "nueva_cadena". Esto construye la cadena invertida.
        nueva_cadena += cadena[n]
    return nueva_cadena

inversa("lola")

# Definir una cadena que te devuelva True si es palindromo
"""
cadena_una = input("Dame una cadena: ")
cadena_al_reves = cadena_una[::-1]

if( cadena_una == cadena_al_reves ):
    print("Es un palindormo")
else:
    print("No es palindromo")
"""
def es_palindromo(cadena):
    nueva_cadena = inversa(cadena)
    if nueva_cadena == cadena:
        return True

print(es_palindromo("radar"))