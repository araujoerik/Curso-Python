# Una lista con los numeros 10, 20, 30, 40, 50 y luego 
# muestra los que hay en las posiciones impares(1, 3 y 5)

numeros = [10, 20, 30, 40, 50]
for i in range(0, 5, 2):
    print(numeros[i])

# Pide al usuario 10 numeros y luego muestra los que son pares 

datos = []
for i in range(0, 10):
    datos.append(int(input("Dame un numero: ")))

print("Los numeros pares son:")
for i in range(0, 10):
    if datos[i] %2 == 0:
        print(datos[i])

# Pide al usuario un numero de 1 al 12 y escribe el nombre del mes 
# que corresponde

mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

opc = int(input("Dame un numero del 1 al 12: "))
print("El mes selecionado fue: " + mes[opc - 1])