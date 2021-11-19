#Ejercicio 1: Dado un string, escribir una funcion que cambie todos los espacios por guiones.
def replaceSpaceByGuion(string):
    """ Funcion que reemplaza los espacios por guiones """
    return string.replace(" ","-")

#Ejercicio 2: Cambiar Mayusculas por Minusculas. (Ejemplo: "Hola Mundo" -> "hOLA mUNDO"). Tiene como limite 100 caracteres.
def mayusculasPorMinusculas(string):
    '''Función que reemplaza Mayusculas por minusculas y visceversa'''
    return string.swapcase()

#Ejercicio 3: Los strings son inmutables.
# Escribir una funcion que reciba un string, un indice y una letra a modificar de ese string y que devuelve el string modificado.
def sustituyeIndiceConLetra(string, indice, letra):
    '''Función que reemplaza el indice indicado en un string por el valor asignado como letra'''
    return string.replace(string[indice],letra)

#Ejercicio 4: Escribir una funcion que reciba un string con nombre y apellido y devuelva un string 
# con el nombre y apellido pero con capitalizacion(primera letra mayuscula).
def capitalizacion(string):
    return string.capitalize()

#Ejercicio 5: Escribir una funcion que reciba N numeros, los cuales representan la puntuacion de un concurso, y esta devuelve la 
# puntuacion del subcampeon. (ejemplo de ingreso de datos... [2,6,10,10,7,5,6], debe devolver 7)
def puntosSubcampeon():
    puntuaciones = []
    respuesta = "S"
    while respuesta.upper() !="N":
        numero = int(input("Ingrese puntuacion: "))
        puntuaciones.append(numero)
        respuesta = input("Desea agregar otro puntaje? | si (S) | no (N) ")
    puntuaciones.sort()
    return puntuaciones





#Ejercicio Extra a): Extra: Escribir una funcion que recibe un numero entero y imprima por salida estandar(usando print) un 
# triangulo de numeros de altura igual al numero ingresado. Ej. Si se ingresa el numero 5, debe imprimir:
'''
1
22
333
4444
55555
'''



#Ejercicio Extra b): Escribir una funcion que reciba un string(el cual representara el nombre de una empresa) y devuelve por salida estandar(usando print) los 3 caracteres mas usados en un orden descendiente. Ejemplo. "Codo a Codo" Debe imprimir:
'''
o 4
c 2
d 2
'''

