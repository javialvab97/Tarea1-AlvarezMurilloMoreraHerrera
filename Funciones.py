def funcion_1(a):
    indice = 0
    mayusculas = 0
    if type(a) != (str):
        return("Error de tipo")  # este es el error único 2
    else:
        while indice < len(a):
            letra = a[indice]
            if letra.isupper():
                mayusculas += 1
                indice = indice + 1
            else:
                indice = indice + 1
        if mayusculas >= 1:
            return ("Mayúscula encontrada")  # error único 1
        else:
            return (a.upper())


def funcion_2(texto):
    val = False
    count = 0
    try:
        lista = list(texto)
        #print(lista)
        for i in range(len(lista)):
            #print(i)
            if lista[i] == "w":
                count += 1
        if count != 0:
            val = True
        return val
    except (NameError, TypeError, ValueError):
        return ("Error de tipo")  # este es el error único 2


def funcion_3(num1, num2):
    try:
        if((num1 - num2) < 0) or(num1 < 0) or(num2 < 0):
            return ("MathError")  # este es el error de resultado y
        # de número negativo
        elif (type(num1) is not (int)):
            return ("Error de tipo")  # este es el error único 2
        elif (type(num2) is not (int)):
            return ("Error de tipo")  # este es el error único 2
        else:
            return (num1 - num2)
    except (NameError, TypeError, ValueError):
        return ("Error de tipo")  # este es el error único 2
