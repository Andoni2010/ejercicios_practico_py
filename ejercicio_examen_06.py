# Definir una funcion superposicion() que tomen dos listas y devuelva True si tiene al menos 1 miembro en comun o devuelva false de lo contrario.
def superposicion(lista1, lista2):
    for elem in lista1:
        for elem2 in lista2:
            if elem == elem2:
                return True

    return False
    """
    # De manera mas elegante
    for elem in lista1:
        if elem in lista2:
            return True
    return False
    """
print(superposicion([1,2,3],[3,4,5]))
