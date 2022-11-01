# Una función te permite definir un bloque de código reutilizable 
# que se puede ejecutar muchas veces dentro de tu programa.
# Una de las grandes ventajas de usar funciones en tu código es que reduce el 
# número total de líneas de código en tu proyecto.

def subrayar():
    for i in range(0, 16):
        print("-", end = "")
    print()

def sub(espacios):
    for i in range(0, espacios):
        print("-", end = "")
    print()

#Declaro cadenas para hacerlo mas dinamico, aunque tambien se puede hacer de manera directa
hi = "Hola, como estas"
happend = "Hola, que tal?"
tomorrow = "Hasta mañana"

print("Funciones sin parametros\n")
print(hi)
subrayar()      
print(happend)
subrayar()
print(tomorrow)
subrayar()
print("\n")

print("Funciones con parametros\n")
print(hi)
sub(len(hi))    # Tomo como referencia el tamaño de la cadena para enviarlo como parametro
print(happend)
sub(len(happend))
print(tomorrow)
sub(len(tomorrow))
print("Hola")
sub(4)          # Tambien puedo enviarle un numero entero si asi lo deseo

# Funcion que devuelve el numero mayor entre dos numeros

def maximo(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print("Imprimimos el numero mayor entre 5 y 12:")
print(maximo(5, 12))
print("Imprimimos el numero mayor entre 25 y 12:")
print(maximo(25, 12))