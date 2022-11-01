# Definir una función que calcule la longitud de una lista o una cadena dada. 
# (Es cierto que python tiene la función len() incorporada, 
# pero escribirla por nosotros mismos resulta un muy buen ejercicio.

def long(cadena):
  cont = 0
  for i in cadena:
    cont += 1
  return cont

if __name__ == "__main__":
  palabra = input("Ingresa una palabra: ")
  print("El numero de caracteres es: " + str(long(palabra)))