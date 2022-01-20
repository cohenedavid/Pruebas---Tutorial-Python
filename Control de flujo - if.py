"""CONTROL DE FLUJO: SENTENCIA if
"""
n1 = 8
n2 = 11
n3 = 11

if n3 < n1:
    print(n3, "es menor a", n1)
    if n3 < n2:                     # Puede haber 0 más bloques if anidados
        print(n3, "también es menor a", n2)     
elif n3 > n1:                       # Puede haber 0 más bloques elif
    print(n3, "es mayor a", n1)
    if n3 > n2:                                 
        print(n3, "también es mayor a", n2)
    elif n3 < n2:
        print("Pero es menor a", n2)
    elif n3 == n2:                  # Una secuencia if … elif … elif … 
                                    # sustituye las sentencias switch o case encontradas en otros lenguajes.
        print("Y",n3, "es igual a", n2)
else:                               # Puede haber 0 o 1 bloque else
    print(n3, "es igual a", n1)
