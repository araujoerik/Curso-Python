# Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del 
# lenguaje que lo hagan de forma automática.
# Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

if __name__ == '__main__':
  cadena = 'Hola mundo'
  reversa = ''
  for letra in cadena:
    reversa = letra + reversa
print(reversa)
    