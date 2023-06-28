# Definir un histograma procedimiento() que tome una lista de umeros enteros e imprima un histograma en la pantalla
def procedimiento(lista):
    for n in lista:
        histograma = "*" * n
        print(f"{histograma} \n ")
procedimiento([1,2,3,4])