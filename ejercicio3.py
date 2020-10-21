''' Ejercicio 3
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y
devuelva las palabras que tengan más de n carácteres.'''


def filtar_palabras(palabras, n):
    palabras_mayores = []
    for palabra in palabras:
        if len(palabra) > n:
            palabras_mayores.append(palabra)

    return palabras_mayores


# comprobacion
palabras = ['jose', 'alberto', 'juanito', 'marta', 'pato']
print(f'palabras con mas (estricto) de 5 caracteres:{filtar_palabras(palabras, 5)}')
print(f'palabras con mas (estricto) de 4 caracteres:{filtar_palabras(palabras, 4)}')
