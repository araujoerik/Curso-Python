# Las tuplas son estructuras de datos inmutables que contiene 
# una secuencia ordenanda de elementos

letras = ('A', 'B', 'C')
print(letras[0])
print(letras[1])
print(letras[2])

print('A' in letras)
print('d' in letras)

print(letras.index('B'))    # Muestra el numero del indice donde se encuentra el elemento

numeros = (1, 2, 1, 3, 4, 5, 5, 6, 6, 6, 6)
print(numeros.count(6))     # Muestra el numero de veces que aparece un elemento en la tupla


