x = 0
while x < 20:
    x = x + 3
print(x)
# 21
a = ~4 # Seria -5 = ~4
print(a)
b = a+4 # -5 + 4 = -1
print(b)
# -1
a = True
b = False
print(a or a and b and a)
# True
a = "python"
b = "pythoN"
print ( a > b)
# True
def x (values):
    values[0] = 1 #modifica el primer valor que es 0 = 2, 1 = 3 y 2 = 4 [2, 3, 4] pasaria a [1, 3, 4]
v = [2, 3, 4]
x(v)
print(v)
# 1, 3, 4
def add (a, b):
    return a+5, b+5
resultado = add (3, 2) # Ya que 3 y 2 serian a y b respectivamente y a los dos se les suma 5 en la funcion
print(resultado)
# (8, 7)
def fun():
    return 55 + int(55.55) # Valor entero de 55.55 es 55 y si le sumas 55 pues son 110
print(fun())
#110
a = 0
while a < 10:
    a = a + 1
print(a)
# 10
a = {"1": 3, "2": 2, "3": 5,}
items = a.items()
result = sorted(items, key=lambda x: x[1]) # Ordena la lista del segundo indice
"""
Ordenar esta lista de pares clave-valor en base a los valores. 
El parámetro key se establece con una función lambda que toma cada elemento x y devuelve x[1], es decir, 
el segundo elemento de cada par clave-valor (los valores).
"""
print(result)
# [('2', 2), ('1', 3), ('3', 5)]
a = "python"
b = [1, 2, 3]
a_b =  (a, b)
print(a_b[1][1:]) 
"""
Esto hace que a_b tengan python y 1, 2, 3 por separado
al esta en dos filas y al hacer a_b[1] coge el primer indice que es la lista de b. a seria el indice 0 y b el 1
y dentro de b con el print(a_b[1][1:]) cogemos a partir del indice 1 que en la lista de b seria el 2.
"""
# [2, 3]
def fun():
    for x in range(22 , 23, 24):
        print(x)
fun()
"""
ya que no se imprime nada dentro de la función 
debido al rango incorrecto en el bucle
"""
# 22 


