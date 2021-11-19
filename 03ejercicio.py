'''
3 - Los strings son inmutables, escribir una funcion que reciba un string,
un indice y una letra a modificar de ese string y que devuelve el string modificado.
'''

def modificar_string(cadena,numero,letra):
    cadena2 = cadena
    largo = len(cadena)
    if((numero + 1) > largo):
        return print("El indice no se encuentra en el string")
    elif((cadena[numero] == ' ')):
        return print("No se pueden reemplazar los espacios")
    else:
        cadena2 = cadena2.replace(cadena[numero],letra)
        return print(cadena2)

cadena = input("Ingrese una frase: ")
numero = int(input("Ingrese un indice: "))
letra = input("Ingrese una letra: ")
modificar_string(cadena,numero,letra)