# Los diccionarios son una collecion de pares clave-valor 
# las claves deben ser unicas e inmutables
# los valores asociados pueder ser de cualquier tipo

myDict = {"A" : 45, "B" : 25}

print(myDict["A"])

del myDict["A"]     #Borra elementos pares del diccionario
print(myDict)

print("C" in myDict)    #Para buscar elementos en los diccionarios