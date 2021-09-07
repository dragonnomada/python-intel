# 1. Sumar una lista de valores

pesos = [90, 67, 45, 34, 23]

suma_pesos = sum(pesos)

print("La suma de pesos es {}".format(suma_pesos))

s = 0

for peso in pesos:
    s = s + peso
    
print("La suma de pesos es {}".format(s))

# Variable: 
#   <nombre> = <valor>
# Condicionales: 
#   if <condición>: 
#       <bloque>
#   elif <condición 2>:
#       <bloque 2> 
#   ... 
#   else: 
#       <bloque falso>
# Iteradores: 
#   for <elemento> in <secuencia>:
#       <bloque>
# Rangos: 
#   range(N) 1, 2, ... N - 1
#   range(a, b) a, a + 1, ..., b - 1
#   range(a, b, s) a, a + 1s, a + 2s, ..., b - 1
# Ciclos Condicionales: 
#   while <condición>:
#       <bloque> 
#       (break -> rompe)
#       (continue -> salta y continua)
# Funciones:
#   def <nombre>(<parámetros>):
#       <bloque>
#       (return -> regresa el cómputo/resultado)
