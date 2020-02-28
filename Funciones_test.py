import Funciones

#Éxito para cada función. Se llama a la función con una entrada conocida y se verifica que la salida sea la esperada.
def test_1():
    resp_1= Funciones.funcion_1("abc")
    resp_2= Funciones.funcion_2("abcwxyz")
    resp_3= Funciones.funcion_3(10,5)
    assert resp_1 == "ABC"
    assert resp_2 == True
    assert resp_3 == 5

#Error donde se ingresa un valor distinto de string para las primeras dos funciones. En este caso se espera verificar que el valor obtenido es el código de error único.
def test_2():
    resp_1= Funciones.funcion_1(5)
    resp_2= Funciones.funcion_2(5)
    assert resp_1 == "Error de tipo"
    assert resp_2 == "Error de tipo"

#Error en la tercera función cuando el resultado no es un número natural. En este caso se espera verificar que el valor obtenido es el código de error único.
def test_3():
    resp_3= Funciones.funcion_3(5,10)
    assert resp_3 == "MathError"


    
    


