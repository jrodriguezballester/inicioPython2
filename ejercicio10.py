"""Ejercicio 10
Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400"""
import calendar

def es_bisiesto(year):
    bisiesto=False
    if year % 4 == 0 and year % 100 != 0:
        bisiesto = True
    if year % 400 == 0:
        bisiesto = True
    if bisiesto:
        print('Es bisiesto')
    else:
        print('no es bisiesto')


year = int(input('introduce un año'))
es_bisiesto(year)
print(f'comprobacion Bisiesto:{calendar.isleap(year)}')
