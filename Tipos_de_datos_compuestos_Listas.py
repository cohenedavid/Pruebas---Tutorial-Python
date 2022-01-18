
"""
Tipos de datos compuestas: listas

"""

# Utilizado para agrupar valores
# El más versátil
# Pueden almacenarse diferentes tipos de valores dentro de ella

numneros = [1, -9, 0, 4320, 7]

# Al igual que los Strings se pueden indexar y segmentar

primeros_3_numeros = numneros[:3]
print(primeros_3_numeros)
print(numneros[-1])

# Todas las operaciones de rebanado retornan una nueva lista que contiene los elementos pedidos
print(numneros[1:4])

# Admiten concatenación

numneros += [25, -10, 350]
print(numneros)

# Las listas son mutables, podemos modificarlas
numeros_impares = [1, 3, 5, 7, 9] # ERROR -> El 9 nueve no es un numero par

numeros_impares[4] = 11
print(numeros_impares)

# Agregar un nuevo elemento al FINAL de la lista con la función append()
numeros_impares.append(13)
print(numeros_impares)