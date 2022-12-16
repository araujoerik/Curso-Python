# Las ecuaciones cuadráticas o ecuaciones de segundo grado son aquellas en donde el exponente del término desconocido está elevado al cuadrado, es decir, la incógnita está elevada al exponente 2. 
# Tienen la forma general de un trinomio:
# a x 2 + b x + c = 0 , a ≠ 0

a = float(input('¿Cual es el valor de A²?: '))
b = float(input('¿Cual es el valor de Bx?: '))
c = float(input('¿Cual es el valor de C?: '))

disc = (b ** 2) - (4 * a * c)
raiz = disc ** 0.5

if disc > 0:
  x1 = ((-b) + raiz)/(2*a)
  x2 = ((-b) - raiz)/(2*a)
  print("X1 = ",x1)
  print("X2 = ",x2)
elif disc == 0:
  x1 = ((-b) + raiz) / (2*a)
  x2 = ((-b) - raiz) / (2*a)
  print("X1 = ",x1)
else:
  print("Solucion imaginaria")