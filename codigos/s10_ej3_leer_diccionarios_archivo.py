f = open("datos/usuarios.txt")

estudiantes = []

for linea in f:
    # print(linea) # "<nombre> <edad> <correo>\n"
    print(linea.strip().split(" ")) # ["<nombre>", "<edad>", "<correo>"]
    
    partes = linea.strip().split(" ")
    
    nombre = partes[0]
    edad = int(partes[1]) # float(partes[1])
    correo = partes[2]
    
    persona = {
        "nombre": nombre,
        "edad": edad,
        "correo": correo,
    }
    
    print(persona)
    
    estudiantes.append(persona)

f.close()