# Las entradas de los datos nos permite darle un manejo mas dinamico a nuestras variables
# La funcion input siempre devuelve una cadena de caracteres

nombre = input("¿Cual es tu nombre?: ")
print('Hola ' + nombre + ', ¿como estas?')

numero = input('Ingresa un numero: ')
print('Tu numero es: ' + numero)

# Si queremos usar numero para realizar operaciones debemos rodear el input
# indicando que tipo de dato necesitamos, por ejemplo:

num = int(input('Ingresa un numero a sumar: '))
num2 = int(input('Ingresa otro valor para sumar: '))
resultado = str(num + num2)     # En esta linea convierto los numero a cadena para imprimirlos 
print('Tu resultado es: ' +resultado)
