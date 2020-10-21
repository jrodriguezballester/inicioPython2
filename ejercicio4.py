""" Ejercicio 4
Escribir un programa que le diga al usuario que ingrese una cadena. El programa
tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""

cadena = input('introduce una cadena: ')
contador1 = 0
contador2 = 0

for i in cadena:
    # utilizamos distinto de lower() xq los caracteres/numeros los considera mayusculas 
    if i != i.lower():
        contador1 += 1

    '''if i == i.upper():  # Verificacion 
        contador2 += 1 '''
print(f'La cadena tiene {contador1} mayusculas')
# print(f'La cadena tiene {contador1} mayusculas')
