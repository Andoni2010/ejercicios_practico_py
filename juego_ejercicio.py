"""
dato = input( "Ingrese dato: ")

lista = ["hola", "mundo", "chanchito","feliz", "dragones"]

if lista.count(dato) > 0:
    print("El dato existe: ", dato)
else:
    print("El dato no existe: ", dato)
"""
# Calculadora
primer_numero = input( "Ingrese dato uno: ")

try:
    primer_numero = int(primer_numero)
except:
    primer_numero = "chanchito feliz"
if primer_numero == "chanchito feliz":
    print("Solo numeros enteros")
    exit()

segundo_numero = input( "Ingrese dato dos: ")

try:
    segundo_numero = int(segundo_numero)
except:
    segundo_numero = "chanchito feliz"
if segundo_numero == "chanchito feliz":
    print("Solo numeros enteros")
    exit()
simbolo = input ("Ingresa operacion: " )
if simbolo == "+":
    print("Suma: ", primer_numero + segundo_numero)
elif simbolo == "-":
    print("Resta: ", primer_numero - segundo_numero)
elif simbolo == "*":
    print("Multiplicando: ", primer_numero * segundo_numero)
elif simbolo == "/":
    print("Dividiendo: ", primer_numero / segundo_numero)
else:
    print("Indica simbolos. No es correcto")