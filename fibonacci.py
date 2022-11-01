# Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
# La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...

def main():
  n1, n2 = 0, 1
  for cont in range(1, 50):
    print(n1)
    fib = n1 + n2
    n1 = n2
    n2 = fib


if __name__ == '__main__':
  main()