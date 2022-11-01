# Modulos en Python

def suma(a, b):
  print('La suma es: ', a + b)

def factor(num):
  if num == 1:
    return 1
  else:
    return(num * factor(num - 1))

def numpos(x):
  if x > 0:
    print("El numero es positivo")
  elif x < 0:
    print("El numero es negativo")
  elif x == 0:
    print("El numero es 0")