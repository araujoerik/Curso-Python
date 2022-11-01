# Enunciado: Escribe una función que reciba dos palabras (String) 
# y retorne verdadero o falso (Boolean) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.

def anagrama(palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    palabra1_arreglo = list(palabra1)
    palabra2_arreglo = list(palabra2)
    # Ordenar lista
    palabra1_arreglo.sort()
    palabra2_arreglo.sort()
    # Convertir a cadena
    palabra1_ordenada = "".join(palabra1_arreglo)
    palabra2_ordenada = "".join(palabra2_arreglo)
    return palabra1_ordenada == palabra2_ordenada

cadena1 = "Amor"
cadena2 = "Roma"
es_anagrama = anagrama(cadena1, cadena2)
if es_anagrama:
    print(f"{cadena1} es anagrama de {cadena2}")
else:
    print(f"{cadena1} NO es anagrama de {cadena2}")

# Solicitar al usuario las cadenas
cadena1 = input("Ingresa una cadena: ")
cadena2 = input("Ingresa otra cadena: ")
es_anagrama = anagrama(cadena1, cadena2)
if es_anagrama:
    print(f"{cadena1} es anagrama de {cadena2}")
else:
    print(f"{cadena1} NO es anagrama de {cadena2}")
