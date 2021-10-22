#!/usr/bin/env python

"""
Name : ${NAME}.py
Author : Jose Francisco Ruvalcaba Castaneda
 Contect : fruvalc@gmail.com
Time    : ${DATE} ${TIME}
Desc: TODO
"""

from datetime import date
import re
import pathlib
import matplotlib.pyplot as plt

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check(email):
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False


def capturaParticipantes():
    nomEquipo = str(input("¿Cual es el nombre de tu equipo? : ")).title()
    teamFile = nomEquipo + ".csv"
    f = open(teamFile, "w")

    numParticipantes = int(input("¿Cuantos participantes tiene tu equipo? (minimo 3, maximo 5) : "))
    for n in range(numParticipantes):
        print("\033c")
        pNombre = str(input("¿Cual es tu nombre? : ")).title()
        pApellido = str(input("¿Cual es tu apellido? : ")).title()
        pEstatura = int(input("¿Cual es tu estatura? (en centimetros) : "))
        pPeso = float(input("¿Cual es tu peso? (en kilogramos) : "))
        pEmail = str(input("¿Cual es tu correo electronico? : ")).lower()
        pIMC = pPeso / ((pEstatura/100)**2)
        participanFile = nomEquipo + "_" + pNombre + pApellido + ".csv"
        part = open(participanFile, "w")
        f.write("{}, {}, {}, {}, {}, {:.2f}\n".format(pNombre, pApellido, pEmail, pPeso, pEstatura, pIMC))
        part.write(("{}, {}, {}, {:.2f}\n".format(today, pPeso, pEstatura, pIMC)))
        part.close()

    f.close()


def agregaPesoSemanal():
    print("\033c")
    nomEquipo = str(input("¿Cual es el nombre de tu equipo? : ")).title()
    pNombre = str(input("¿Cual es tu nombre? : ")).title()
    pApellido = str(input("¿Cual es tu apellido? : ")).title()
    teamFile = nomEquipo + ".csv"
    participanFile = nomEquipo + "_" + pNombre + pApellido + ".csv"
    file1 = pathlib.Path(teamFile)
    file2 = pathlib.Path(participanFile)
    if file1.exists() and file2.exists():
        with open(teamFile, 'r') as read_obj:
            for line in read_obj:
                if pNombre + ", " + pApellido in line:
                    parts = line.strip().split(",")
                    pEstatura = float(parts[4])
        pFecha = str(input("¿A que fecha corresponde la medicion? (en el formato MM/DD/AAAA): "))
        pPeso = float(input("¿Cual es tu peso? (en kilogramos) : "))
        pIMC = pPeso / ((pEstatura / 100) ** 2)
        part = open(participanFile, "a")
        part.write(("{}, {}, {}, {}\n".format(pFecha, pPeso, pEstatura, pIMC)))
        part.close()
    else:
        print("Verifica el nombre del equipo o del participante, no tenemos registros con esos datos.")


def calculosFinales():
    print("\033c")
    nomEquipo = str(input("¿Cual es el nombre de tu equipo? : ")).title()
    teamFile = nomEquipo + ".csv"
    file1 = pathlib.Path(teamFile)
    if file1.exists():
        with open(teamFile, 'r') as read_obj:
            for line in read_obj:
                parts = line.lstrip().split(",")
                cfNombre = str(parts[0]).title()
                cfApellido = str(parts[1]).strip().title()
                cfEmail= str(parts[2]).strip().lower()
                cfPesoInicial= float(parts[3])
                cfEstatura= int(parts[4])
                cfIMCinicial= float(parts[5])
                participanFile = nomEquipo + "_" + cfNombre + cfApellido + ".csv"
                file2 = pathlib.Path(participanFile)
                pIMCs = []
                pDates = []
                if file1.exists() and file2.exists():
                    with open(participanFile, 'r') as read_obj:
                        for l in read_obj:
                            p = l.strip().split(",")
                            pDates.append(p[0])
                            pIMCs.append(float(p[3]))
                        plt.plot(pDates, pIMCs, "green")
                        plt.show()
                        plt.savefig(nomEquipo + "_" + cfNombre + cfApellido + ".png")


def menu():
    while True:

        print("\033c")

        opcion = str(
            input(
                'Selecciona una opcion:\n\n1. Agrega participante\n2. Agrega actualizacion de peso semanal\n3. Calculos Finales\nS. Salir\n\nOpcion: '))

        if opcion == '1':
            capturaParticipantes()
        elif opcion == '2':
            agregaPesoSemanal()
        elif opcion == '3':
            calculosFinales()
        elif opcion == 's' or opcion == 'S':
            break
        else:
            print("Opcion no valida.")
        input("Pulsa una tecla para continuar...\n\n")


def main():

    global today

    today = date.today()

    menu()


if __name__ == "__main__":
    main()