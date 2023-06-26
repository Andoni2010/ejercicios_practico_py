# Escribe una funcion sum() y una funcion multip() que sumen y multiplique respectivamente todos los numeros de una lista
def sum(lista):
    resultado = 0
    for n in lista:
        resultado += resultado + (n)
    print(resultado)
sum((1,-2,3))

def mult(lista):
    resultado = lista[0]
    i = 1
    while i in range(1, len(lista)):
        resultado = resultado * lista[1]
        i += 1
        print(resultado)
mult((5, 5, 5))