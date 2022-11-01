# Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.

class poligono:
  def triangulo(b, h):
    return (b * h) / 2
  def cuadrado(lado):
    return lado * lado
  def rectangulo(base, altura):
    return base * altura

if __name__ == '__main__':
  cuadrado = poligono.cuadrado(3)
  print('El area del cuadrado es: ' F'{(cuadrado)} metros cuadrados')
  triangulo = poligono.triangulo(50, 10)
  print('El area del triangulo es: ' F'{(triangulo)} metros cuadrados')
  rectangulo = poligono.rectangulo(20, 520)
  print('El area del triangulo es: ' F'{(rectangulo)} metros cuadrados')