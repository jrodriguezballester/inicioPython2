"""Ejercicio 9
Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras
"a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra."""


def contar_vocales(palabra):
    vocales = ('a', 'e', 'i', 'o', 'u')
    for vocal in vocales:
        contador=0
        for letra in palabra:
            if letra == vocal:
               contador+=1
        print(f'Hay {contador} {vocal} en la palabra {palabra}')


palabra = input('Introduce una palabra:')
contar_vocales(palabra)
