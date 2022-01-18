
"""
Strings: rebanadas, función len()

"""

word = "Python"

rebanada1 = word[0:6]   # desde el caracter 0 (incluido) hasta el 6 (excluido)
rebanada2 = word[0:]    # desde el caracter 0 (incluido) hasta el ultimo de la cadena

rebanada3 = word[0:3]   # desde el caracter 0 (incluido) hasta el 3 (excluido)
                        # Para índices no negativos, la longitud de la rebanada es 
                        # la diferencia de los índices, si ambos están dentro de los límites

print(rebanada1)
print(rebanada3)

print(word + ' Tutorial') # imprimir variable concatenado a un literal


"""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""

"""print(word[80])""" # IndexError: string index out of range
# NO se puede utilizar un índice fuera del rango de los índices de la cadena

# Sin embargo, los índices fuera de rango no provocan un error al utilizar rebanadas
print(word[:80]) # Si se excede del rango tomará hasta el último valor de la cadena

# Las cadenas de Python no se pueden modificar, son immutable
""" word[0] = 'J' """ # TypeError: 'str' object does not support item assignment

# Si queremos obtener una nueva cadena a partir de alguna modificación de la anterior
# Por ejemplo, podemos hacerlo así:
word_2= 'J' + word[1:]
print(word_2)

# Largo de una cadena: utilizamos la función incorporada len()
# que nos devuelve un entero positivo o un cero si la cadena está vacía
print(len(word))
print(len("")) #  cadena vacía