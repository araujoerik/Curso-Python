# Herencia

class Humano:
  def __init__(self, edad): # Metodo
    self.edad = edad # Atributo
  def hablar(self, mensaje):
    print(mensaje)

class ingSistemas(Humano):
  def programar(self, lenguaje):
    print('Voy a programar en ', lenguaje)

class licDerecho(Humano):
  def estudiarCaso(self, de):
    print('Debo estudiar el caso de ', de)

# Creacion de objetos
pedro = ingSistemas(26)
raul = licDerecho(21)

pedro.programar('Python')
raul.estudiarCaso('Pedro')

pedro.hablar('Hola')
raul.hablar('Hola, Pedro')