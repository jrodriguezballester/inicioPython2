"""Ejercicio 7
Definir una tupla con 10 edades de personas. Imprimir la cantidad de personas con
edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades"""

cantidad = 0
edadesList = []
# Tupla fija (primera parte ejercicio)
edades = (20, 30, 42, 53, 7, 12, 22, 33, 44, 77)

# Tupla introducida por el usuario (segunda parte ejercicio)
''' Las tuplas son inmutables, insertamos en list que convertimos a tupla'''
for i in range(10):
    edad = int(input('Introduce una edad:'))
    edadesList.append(edad)
edades = tuple(edadesList)

# Calculo datos
for edad in edades:
    if edad > 20:
        cantidad += 1
print(f'edades: {edades}') # comprobacion valor tupla
print(f'Hay {cantidad} mayores de 20 años')
