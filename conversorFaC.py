# Enunciado: Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
# Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F").
# En caso contrario retornará un error.

def celsius(x):
  F = float(x[:-2])
  F = (F * 9 / 5) + 32
  print(F'{float(F)} °F')

def fahrenheit(y):
  C =  float(y[:-2])
  C = (C - 32) * 5 / 9 
  print(F'{float(C)} °C')

a = input("Escribe la temperatura a covertir: ")
A = a.upper()
if '°C' in A or '°F' in A:
  if '°C' in A:
    celsius(A)
  if '°F' in A:
    fahrenheit(A)
else:
  TypeError: print('Error - Introduzca la temperatura a convertir con su respectiva unidad °C o °F. Ejemplo: 32°C o 125°F')