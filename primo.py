# Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
# Hecho esto, imprime los números primos entre 1 y 100.

def primo(x):
  if x < 1: 
    return False
  elif x == 2:
    return True
  else:
    for i in range(2, x):
      if x % i == 0:
        return False
    return True 

def main():
  for num in range(1, 101):
    resultado = primo(num)
    if resultado == True:
      print(str(num) + ' PRIMO')
    else:
      print(str(num) + ' NO PRIMO')

if __name__ == '__main__':
  main()