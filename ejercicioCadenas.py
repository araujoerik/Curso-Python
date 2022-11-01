# Pregunta su nombre al usuario y responde: 
# Su inicial 
# La cantidad de letras 
# La ultima letra 
# Su nombre en mayuscula 
# Su nombre al reves 
# La cantidad de vocales que tiene 

nombre = input("Cual es tu nombre?: ")
count = 0
long = len(nombre)
inicial = nombre[0]
fin = nombre[-1]
may = nombre.upper()
vocal = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
vLong = len(vocal)
reverse = nombre[long : : -1]
print("Tu nombre es: " + nombre)
print("Tu inicial es: " + inicial)
print("El numero de letras que tiene tu nombre es: " + str(long))
print("La ultima letra de tu nombre es: " + fin)
print("Tu nombre en mayuscula es: " + may)
print("Tu nombre al reves es: " + reverse)

for i in range(0, int(long)):
    nombre[i]
    for j in range(0, vLong):
        vocal[j]
        if nombre[i] == vocal[j]:
            count += 1

print("Tu nombre tiene: " + str(count) + " vocales")