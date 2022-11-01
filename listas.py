# Las listas son estructuras de datos utilizados
# para almacenar multiples valores en secuencia ordenada

lista = []      # Lista vacia
nombre = input('¿Cual es tu nombre?: ')
lista.insert(0 , nombre)
print('Tu nombre es: ' + lista[0])
edad = int(input('¿Cual es tu edad?: '))    # Quiero guardar el valor como entero   
lista.insert(1, edad)
edad = str(lista[1])    # Convierto la variable entera a cadena para poder imprimirla
print('Tu edad es: ' + edad)

# En caso de que se requiera eliminar un elemento se utiliza el metodo 
# remove <lista>.remove(<elemento>)

numeros = [1, 2, 3, 4, 5, 4]
print(numeros)
numeros.remove(4)
print(numeros)

#Si se desea buscar un elemento se usa  el metodo <elemento> in <lista>
# en caso de que se encuentre devuelve un booleano true 

vocales = ['a', 'e', 'i', 'o', 'u']
print('a' in vocales)
print('b' in vocales)

# .index retorna el indice de la primera ocurrencia del elemnto en la lista.
# Si no se encuentra el elemento, ocurre un error 

vocales = ['a', 'e', 'i', 'o', 'u']
print(vocales.index('i'))

# Metodos importantes para el manejo de listas: 
# .count(<elemento>)      .pop()
# .extend(<lista>)        .reverse()
# .sort()

datos = [5, 6, 7, 8, 9]
print("Datos 0 y 2")
print(datos[0])
print(datos[2])

print("Todos los datos")
for i in range(0, 5):
    print(datos[i])

print("Todos los datos al reves")
for i in range(4, -1, -1):
    print(datos[i])

# Si se desea agregar varios datos a las listas 
# basta con hacer un bucle junto al metodo .append

numero = []
for i in range(0, 6):
    numero.append(int(input("Dime un numero: ")))

for i in range(0, 6):
    print(numero[i])