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