f = open("datos/numeros.txt", "r")

for line in f:
    numero = int(line.strip()) # float(line)
    
    print(numero * 100)

f.close()