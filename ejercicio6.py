"""Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla."""
datos = {}
years = {}
year = int(input('introduce el año: '))
for index in range(3):
    persona = input(f'nombre de la persona {index + 1}:')
    year_nac = int(input(f'año de nacimiento de la persona {index + 1}:'))
    datos[persona] = year_nac
    years[persona] = year - year_nac

# mostrar por pantalla
for nombre in years.keys():
    print(f'{nombre} cumplirá {years.get(nombre)} años')

# print(datos)
# print(anos)
