# Programa con diferentes tipos de conversiones, un menu y funciones para cada conversion

def kilos_libras(entrada):
  resultado = round(entrada * 2.20462, 2)
  print("El resultado de la conversión es: {} ".format(resultado))

def libras_kilos(entrada):
  resultado = round(entrada * 0.453592,2)
  print("El resultado de la conversión es: {} ".format(resultado))

def euros_dolares(entrada):
  resultado = round(entrada * 1.11, 2)
  print("El resultado de la conversión es: {} ".format(resultado))

def dolares_euros(entrada):
  resultado = round(entrada / 1.11, 2)
  print("El resultado de la conversión es: {} ".format(resultado))


if __name__ == "__main__":
  print("****** CONVERSOR DE UNIDADES ******")
  print("******      Opciones         ******")
  print(" 1) Kilos a Libras\n 2) Libras a Kilos\n 3) Euros a Dolares\n 4) Dolares a Euros")

  opcion = int(input("Selecciona la operacion a realizar: "))
  resultado = 0

  if opcion == 1:
    print("De Kilos a Libras")
    x = float(input("Ingresa los kilos a convertir: "))
    kilos_libras(x)
  elif opcion == 2:
    print("De Libras a Kilos")
    x = float(input("Ingresa las libras a convertir: "))
    libras_kilos(x)
  elif opcion == 3:
    print("De Euros a Dolares")
    x = float(input("Ingresa los euros a convertir: "))
    euros_dolares(x)
  elif opcion == 4:
    print("De dolares a Euros")
    x = float(input("Ingresa los dolares a convertir: "))
    dolares_euros(x)
