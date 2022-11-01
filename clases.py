# Clases y objetos

class Humano:
  def __init__(self, edad): # Metodo
    self.edad = edad # Atributo
  def hablar(self, mensaje):
    print(mensaje)

# Creacion de objetos
pedro = Humano(26)
raul = Humano(21)

# Llamada por objeto.atributo
print('Soy Pedro y tengo ', pedro.edad)
print('Soy Raul y tengo ', raul.edad)

# Llamada por objeto.metodo
pedro.hablar('Hola')
raul.hablar('Hola, Pedro')