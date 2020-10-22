"""Ejercicio 8
Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar. (Un poco mas emocionante)"""

nombres = ('juan', 'pedro', 'andres', 'amparo', 'jose')
contador = 0
letra = input('introduce la inicial del nombre:')

for nombre in nombres:
    if nombre[0] == letra:
        contador += 1

print(f'hay {contador} nombres que empiecen por {letra}')
