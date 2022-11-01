# Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
# (Es cierto que python tiene una función max() incorporada, 
# pero hacerla nosotros mismos es un muy buen ejercicio.

mensaje = "son iguales"

def max(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    else:
        return mensaje

print("\n\nEl numero mayor entre dos numeros\n")
a = int(input("Ingresa un numero: "))
b = int(input("Ingresa otro numero: "))
print("\nEl numero mayor entre " + str(a) + " y " + str(b) + " es: " + str(max(a, b)))
