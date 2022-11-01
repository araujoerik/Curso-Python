# Al utilizar ficheros para guardar los datos estos perdurarán tras la ejecución del programa, 
# pudiendo ser consultados o utilizados más tarde.

# Las operaciones más habituales con ficheros son:

# Crear un fichero.
# Escribir datos en un fichero.
# Leer datos de un fichero.
# Borrar un fichero.

# Para crear un fichero nuevo se utiliza la siguiente función:

# open(ruta, 'w') : Crea el fichero con la ruta ruta, lo abre en modo escritura 
# (el argumento ‘w’ significa write) y devuelve un objeto que lo referencia.

# open(ruta, 'r') : Abre un archivo creado en modo lectura (el argumento 'r' significa read)

# open(ruta, 'a') : Abre o crea un archivo y lo hace en el modo de agregar (el argumento 'a' significa append)

fw = open("Fichero.txt", "w")   # Modo escritura
fa = open("Fichero.txt", "a")   # Modo agregar
fr = open("Fichero.txt", "r")   # Modo lectura

# Metodo de escritura
fw.write("¡Bienvenido!")
fw.close()

# Metodo de escritura
fa.write("\nA Python")
fa.write("\nEs una nueva linea\n")
fa.write("Agregando otra linea mas")
fa.close()

# Imprime lo que contiene el fichero
print(fr.read())