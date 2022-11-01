# Los operadores son símbolos que le indican al intérprete que realice una operación específica, 
# como aritmética, comparación, lógica, etc.
# Operadores aritmeticos:
# Un operador aritmético toma dos operandos como entrada, realiza un cálculo y devuelve el resultado

num = 10
num2 = 2

print(num + num2)   # suma
print(num - num2)   # resta
print(num * num2)   # multiplicacion
print(num / num2)   # division
print(num // num2)  # division entera
print(num ** num2)  # exponente o exponencial
print(num % num2)   # modulo o resultado del residuo de la division

# Operadores logicos
# and, not, or

print(bool(num < num2 and num2 > num))
print(bool(num == num2 or num < num2))
print(bool(not num or num2))

# Operadores relacionales
# > mayor que     < menor que
# >= mayor o igual que    <= menor o igual que
# == igual que    != diferente que

# Operador de asignacion
# =       +=
# -=      *=
# /=      **=
# //=     %=