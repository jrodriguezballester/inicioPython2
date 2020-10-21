'''ejercicio 1
escribir una función max_in_list() que tome una lista de números y devuelva el más grande.'''


# idea: que tome el primero y compare con el siguiente

def max_in_list(numeros):
    mas_grande = numeros[0]

    for numero in numeros:
        if mas_grande <= numero:
            mas_grande = numero
    return mas_grande


# comprobacion

numeros = [2, 5, 3, 7, 2, 4, 9, 2, 1]
print(f'el maximo numero de la lista {numeros} es: {max_in_list(numeros)}')
