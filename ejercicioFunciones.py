# Crea una funcion que reciba 3 numeros y devuelva su suma

def suma(a, b, c):
    res = a + b + c
    return res

print("\nSuma de tres numeros\n")
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
num3 = int(input("Ingresa el tercer numero: "))
print("\nLa suma es: " + str(suma(num1, num2, num3)))

# Crea una funcion que reciba una cadena de texto
# y una letra, y devuelva la cantidad de veces que aparece
# dentro de la cadena

def rep(cad, let):
    count = 0
    for i in range(0, len(cad)):
        if cad[i] == let:
            count += 1
    return count

print("\n")
cadena = input("Ingresa una palabra al azar: ")
mins = cadena.lower()
letra = input("Ingresa una letra al azar: ")

print("\nEl numero de veces que aparece la letra " + letra + " en la palabra " + cadena + " es " + str(rep(mins, letra)))

# Crea un procedimiento que escriba una linea formada por 2 letras, repetidas varias veces.
# Por ejemplo, para "-", "=" y 3, escribiria "-=-=-="

def reps(a, b):
    repetida = a * b
    return repetida

print("\nRepeticion de una cadena 'n' veces\n")
x = input("Ingresa una letra: ")
y = input("Ingresa una letra: ")
z = x + y
n = int(input("Ingresa un numero de veces que quieras que se repitan: "))
print("\nTu cadena repetida es: " + reps(z, n)) 