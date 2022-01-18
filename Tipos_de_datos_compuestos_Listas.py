
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
numeros_impares = [1, 3, 5, 7, 9]                       # ERROR -> El 9 nueve no es un numero par

numeros_impares[4] = 11
print(numeros_impares)

# Agregar un nuevo elemento al FINAL de la lista con la función append()
numeros_impares.append(13)
print(numeros_impares)

# Reemplazar valores intermedios dentro de una lista mediante rebanadas
abecedario = ['a','b','c','d','e','l','m','n','i','j']  # Acá los caracteres l,m,n están mal ubicados
print(abecedario)                                       # Debemos reemplazarlos por f,g,h que están
                                                        # ubicados en las posiciones 5,6,7
# Salida --> ['a', 'b', 'c', 'd', 'e', 'l', 'm', 'n', 'i', 'j']    
abecedario[5:8] = ['f','g','h']                         # lo reemplazamos empleando rebanadas
print(abecedario)                                       # Vemos que ahora ha quedado correctamente
# Salida --> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Obtener el largo de una lista con la funcióm len()
print(len(abecedario))

# Guardar listas dentro de otra lista: Anidar listas
vocales_abiertas = ['a', 'o', 'e']
vocales_cerradas = ['i', 'u']
vocales = [vocales_abiertas, vocales_cerradas]
print(vocales)
# Salida --> [['a', 'o', 'e'], ['i', 'u']]
print(vocales[0]) # Vocales tiene dos índeces: [0] y [1], siendo [0] la lista de vocales_abiertas
# Salida --> ['a', 'o', 'e']

