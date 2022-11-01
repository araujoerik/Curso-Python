# La sentencial condicional es una instruccion o un
# grupo de instrucciones cuya ejecucion depende del
# valor de una condicion booleana 

num = 10

if num < 20:    # Se imprime El numero es menor
    print('El numero es menor')
else:
    print('El numero es mayor')

if num > 5:    # Se imprime El numero es mayor
    print('El numero es mayor')
else:
    print('El numero es menor')

temp = -10

if temp <= 0:
    print('Muy frio')
elif temp < 25:
    print('Frio')
else:
    print('Calor')

# El numero de elif pueden ser mas de uno, pero else solo se puede respetir una sola vez