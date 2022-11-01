# Definir una función max_de_tres(), que tome tres números como argumentos 
# y devuelva el mayor de ellos.

mensaje = "son iguales"

def max3(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return mensaje


print("\n\nEl numero mayor de 3\n")
x = int(input("Ingresa el primer numero: "))
y = int(input("Ingresa el segundo numero: "))
z = int(input("Ingresa el tercer numero: "))

print("\nEl numero mayor entre " + str(x) + ", " + str(y) + " y " + str(z) + " es: " + str(max3(x, y, z)))