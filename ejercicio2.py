'''Ejercicio 2
Escribir una función mas_larga() que tome una lista de palabras y devuelva la más larga.'''

# Idea: igual que ejercicio 1 pero comparando longitud. Controlar palabras de maxima longitud

def mas_larga(palabras):
    palabras_mas_largas = []
    palabra_mas_larga = palabras[0]
    # obtenemos la palabra mas larga
    for palabra in palabras:
        if len(palabra_mas_larga) <= len(palabra):
            palabra_mas_larga = palabra
    # controlamos longitud repetida
    for palabra in palabras:
        if len(palabra) == len(palabra_mas_larga):
            palabras_mas_largas.append(palabra)

    return palabras_mas_largas

# comprobacion
palabras = ['jose', 'alberto', 'juanito', 'marta']
print('la palabra o palabras mas largas son: ')
print(mas_larga(palabras))
