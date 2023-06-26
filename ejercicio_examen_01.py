# Define una funcion mac ()  que tome como argumento dos numeros y devuelva el mayor de ellos. (Es cierto que en python ya tiene esa funcion)

def maxi(n1 ,n2): #def maxi(n1: int ,n2: int): Para que sea solo numeros enteros
    # Docstring
    """ Dado dos numeros de entrada retorna el maximo de ambos
    Args: 
        n1 (int): Primer numero a comparar
        n2 (int): Segundo numero a comparar
    Returns:
        int : Mayor de ambos
    """
    if n1 > n2:
        return n1
    elif n2 > n1 :
        return n2
    elif n1 == n2:
        raise Exception("No pueden seriguales")
    raise Exception("Algo salio mal")

print(maxi(2, 5))
    
