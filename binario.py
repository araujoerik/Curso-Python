# Enunciado: Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

num = 1993

modulos = []

while num != 0:
  modulo = num % 2
  cociente = num // 2
  modulos.append(modulo)
  num = cociente

print(modulos)