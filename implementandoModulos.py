# Importar modulos externos

import modulos

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))
modulos.suma(num1, num2)

numfact = int(input("Ingresa un numero para calcular su factorial: "))
print("El resultado es: ", modulos.factor(numfact))

y = int(input("Ingresa un numero: "))
modulos.numpos(y)