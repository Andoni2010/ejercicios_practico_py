# Definir una funcion max_de_tres() que tome tres numeros como argumentos y devuelva el mayor de ellos

def max_tres (n1, n2, n3):
        # Docstring
    """ Dado dos numeros de entrada retorna el maximo de ambos
    Args: 
        n1 (int): Primer numero a comparar
        n2 (int): Segundo numero a comparar
        n3 (int): Tercer numero a comparar
    Returns:
        int : Mayor de ambos
   
   a > b > c
   b > c
   a > c
    """
    
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    elif n3 > n1 and n3 > n2 :
        return n3
    elif n1 == n2 and n1 == n2:
        raise Exception("No pueden seriguales")
    elif n2 == n3 and n2 == n3:
        raise Exception("No pueden seriguales")
    raise Exception("Algo salio mal")


print(max_tres(5,5,7))

