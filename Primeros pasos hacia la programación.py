""" Primeros pasos hacia la programación
"""
# Definiruna nueva serie inicial de Fibonacci
# Serie de Fibonachi:
# La suma de dos numeros previos definen el siguiente en la serie

a, b = 0, 1     # Defino los dos primeros valores de la serie con una asignación múltiple
while a < 10:   # Bucle para imprimir una cierta cantidad de valores, en este caso 7 numeros
    print(a)
    a, b = b, a+b
# 0
# 1
# 2
# 3
# 5
# 8
# Finaliza con el valor 8 ya que luego a = 13 y no cumple la condición del bucle while


# Función print
print("")
print(a,b,"print() agrega un espacio en blanco entre elementos")
print(5) # 5
print("texto") # Las cadenas de texto son impresas sin comillas
print(True) # True


# Evitar salto de línea al imprimir en bucle
c, d = 0, 1

while c < 10:
    print(c , end= ' ') # Parámetro end= ',' se utiliza para evitar el salto de línea al final de la salida
    c, d = d, c+d       # o para terminar la salida con una cadena en particular
# 0 1 1 2 3 5 8