# Escribe una funcion que tome un caracter y devuelva Terue si es una voca

def vocal (caracter):
    lista = ["a", "e", "i", "o", "u"]
    if caracter in lista:
        return True
    else:
        return False
print (vocal("l"))