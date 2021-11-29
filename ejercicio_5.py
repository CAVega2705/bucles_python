# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicio de secuencias numéricas

# Pedir por consola dos números que representen el principio y fin de una
# secuencia numérica.
# Realizar un bucle "for" que recorra esa secuencia armada con "range"
# y calcule a sumatoria total de todos los números dentro de esa secuencia
# Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
# sino que va hasta el anterior

inicio = int(input('Ingrese el primer número de la secuencia\n'))
fin = int(input('Ingrese el último número de la secuencia\n'))
sumatoria = 0  # Inicializo el contador en 0

# for ... in range(....)

# Imprimir el valor de la sumatoria
fin = fin + 1
rango = range(inicio,fin)
for numero in rango:
    if inicio < fin:
        print("Uno de los números dentro de la secuencia es: {}".format (numero))
    else:
        print("El último número de la secuencia es {}".format(fin))
    sumatoria += inicio
    inicio = inicio + 1
    
print("La sumatoria es {}".format(sumatoria))

print("terminamos!")
