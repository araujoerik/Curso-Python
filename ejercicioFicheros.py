# Pide al usuario 3 frases y guardalas en un fichero "Frases.txt"
# Añade una cuarta frase al fichero anterior.
# Muestra el contenido de "Frases.txt", procediendo
# cada linea con un numero correlativo

fichero = "Frases.txt"
f = open(fichero, "w")
fa = open(fichero, "a")
fr = open(fichero, "r")

frase1 = input("Ingresa una frase: ")
frase2 = input("Ingresa otra frase: ")
frase3 = input("Ingresa una ultima frase: ")
frase4 = "Olvide pedir una frase mas\n"

f.write(frase1 + "\n")
f.close()
fa.write(frase2 + "\n")
fa.write(frase3 + "\n")
fa.write(frase4)
fa.close()

print("\nEl contenido del fichero es: ")
print(fr.read())