#Split o rebanado es tomar porciones de las cadenas e imprimirlas segun sea el caso

palabra = "¡Hola, Mundo!"

# Maneras de dividir las cadenas

#Cualquiera de estas formas imprime en su totalidad la cadena

print(palabra[:13])
print(palabra[0:])
print(palabra[:]) 

# Impresiones parciales de cadena

print(palabra[1:5])     #Hola
print(palabra[7:12])    #Mundo
print(palabra[1:5:2])   #Hl
print(palabra[7:12:2])  #Mno