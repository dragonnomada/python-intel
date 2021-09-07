# Programación funcional es añadir la primera capa de abstracción de código

# Tarea: Partir una lista en sublistas de 3 en 3
# 
# Ejemplo:
# 
# Entrada: [1, 2, 3, 4, 9, 8, 7, 5, 6]
# 
# Salida: [ [1, 2, 3], [4, 9, 8], [7, 5, 6] ]

entrada = [1, 2, 3, 4, 9, 8, 7, 5, 6]

salida = []

N = len(entrada) # 9

for i in range(0, N, 3): # [0], 1, 2, [3], 4, 5, [6], 7, 8
    print(i, entrada[i], entrada[i:i+3]) # 6, entrada[6], entrada[6:9]
    # 0 1 [1, 2, 3]
    # 3 4 [4, 9, 8]
    # 6 7 [7, 5, 6]
    parte = entrada[i:i+3]
    salida.append(parte)
    
print(salida)

# Cuándo definimos una función
# estamos abstrayendo el código para que
# se base en parámetros de entrada y produzca un retorno como salida
def partirLista3en3(entrada):
    salida = []
    for i in range(0, len(entrada), 3):
        parte = entrada[i:i+3]
        salida.append(parte)
    return salida

print([1, 2, 3, 4, 5, 6], partirLista3en3([1, 2, 3, 4, 5, 6]))

print([], partirLista3en3([]))

print([1], partirLista3en3([1]))

print(range(201, 217), partirLista3en3(range(201, 217)))

# range(201, 217)[0:3] -> range(201, 204)
