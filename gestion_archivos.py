""".
leer_archivo = open("ejercicio_bootcamp\hoja_ruta.txt")#"a"Amliaa el archivo / "w" crea el archivo si no existe y te deja escribir / "x" si esta creado nos da error y si no lo crea
print(leer_archivo.readline())# lee una lineas

c = open("ejercicio_bootcamp\hoja_ruta.txt")
for x in c:
    print(x)

c.close()

c = open("ejercicio_bootcamp\hoja_ruta.txt", "a")
c.write("\nAgregamos mas texto")
c.close()
x = open("ejercicio_bootcamp\hoja_ruta.txt")
print(x.read())
"""
import os

if os.path.exists("hoja.txt"):
    os.remove("ejercicio_bootcamp\hoja_ruta.txt")
else:
    print("No existe")

os.rmdir("ejercicio_bootcamp\mi_carpet")