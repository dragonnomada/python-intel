real = float( input("Real: ") )
imaginaria = float( input("Imaginaria: ") )

valor = complex(real, imaginaria)

print("Valor: {}".format(valor))

real, imaginaria = tuple(map(float, input("Dame el complejo separado por espacio (real imaginario): ").split(" ")))

valor = complex(real, imaginaria)

print("Valor: {}".format(valor))