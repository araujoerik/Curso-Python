# Enunciado: Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm.
# Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales).
# Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".

def ohm(v , i, r):
  if v != 0 and r != 0 and i == 0:
    print("I = " F"{v / r}")
  elif v != 0 and i != 0 and r == 0:
    print("R = " F"{v / i}")
  elif r != 0 and i != 0 and v == 0:
    print("V = " F"{r * i}")
  elif v == 0 and i == 0 and r == 0:
    print("Datos Invalidos")
  else:
    print("Datos Invalidos")

ohm(5, 0, 0) 
ohm(5, 0, 4)
ohm(5, 4, 0)
ohm(0, 4, 5)
ohm(5.125, 0, 4)
ohm(5, 4.125, 0)
ohm(0, 4.125, 5)
ohm(5, 0, 0)
ohm(5, 0, 0)
ohm(0, 0, 5)
ohm(5, 3, 4)

