
##      Nombre: Rafael Anguiano
##      Proyecto: Reporte de Efficiencia
##
##      Descripcion:    El programa llamara el archivo csv que se le introdusca por medio de un input() (puede ser uno o mas archivos a la vez.)
##                      el documento contiene datos para graficar, los datos seran extraidos con la funcion read_csv  y almacenados para graficar con matplotlib,
##                      ademas se genera un reporte en PDF usnado fpdf.

##                      Para esto el programa cuenta con menu, busqueda de archivos, extraccion de datos, graficacion de datos, almacenamiento de imagen graficadas y generacion reportes en PDF.
##                      El progama utiliza "variables" (int, float, boolean), "Diccionario"  y "lista" para almacenar datos, Iterador "For" Para hacer barrido de los datos ,
##                      "while" para el menu, condicional "if" para el menu, "class report" para la generacion de reportesx, Libreria "matplotlib" para graficar, libreria numpy para el areglo de datos,
##                       librebria "pandas" para extrar datos del csv y libreria fpdf para crear archivo pdf.

##      Justificacion:  Revisar los resultados es tedioso y lento, esta herramieta ayudara
##                      a obtener una vista rapida de los puntos importantes, comparar resultados y almacenar en documento PDF


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from fpdf import FPDF

def menu():
    Salir = True
    Count = 0
    while Salir:
        print ('-'*15 + ' Programa ' + '-'*15)
        print ('| 1) Agregar documento para graficar' + '{:>4}'.format('|'))
        print ('| 2) Graficar y guardar' + '{:>17}'.format('|') )
        print ('| 3) Salir' + '{:>30}'.format('|'))
        print ('-'*40)

        x = input('Seleccione el numero para la opccion deseada >>: ')
        if x == "1":
            print ("Se ha seleccionado la opcion Agregar documento para graficar")
##          Pedir Nombre de Archivos
            dicc = SearchFiles()
##          Abrir csv y extrar los datos
            diccxy = DataGet(dicc)
##          Agregar datos a la grafica
            Nameplot = AddPlt(diccxy)
            print('\n'*100)
            print ('-'*40)
            print ('|  Datos agregados correctamente' + '{:>8}'.format('|'))
            print ('-'*40)
        elif x == "2":
            print ("Se ha seleccionado la opcion Graficar")

##          Guardar en pdf y graficar datos
            SaveImagen(Nameplot,diccxy,Count)
            plt.show()
            Count = Count + 1
            dicc = {}
            diccxy = {}
            Nameplot = {}
            print('\n'*100)
            print ('-'*40)
            print ('|  Datos Graficados             ' + '{:>8}'.format('|'))
            print ('-'*40)
        elif x == "3":
            print ("Se ha seleccionado la opcion Salir")
            Salir= False
        else:
            print ("No exite esta opcion")

def SearchFiles():
    paths = []
    print('Introduce el nombre del archivo a graficar: ')
    string = input('introdusca el nombre del archivo o archivos separados con una coma (,) : \n ')
##  Ordenar los archivos y borrar espacios
    string = string.replace(' ','')
    files = string.split(',')
##  iterador para barrer la lista de archivos
    for file in files:
        paths.append(f'C:/Users/ranguian/OneDrive - Intel Corporation/Documents/Projects/SDW/ps0_vrci Core/{file}')
    dicc = {}
##  Guardar en diccionario los Paths de cada archivo
    dicc['Paths'] = paths
    dicc['files'] = files
    return dicc

def DataGet(dPathFile):
    count = 0
    dDatos = {}
##  iterador for para abrir archivo por archivo y guardar los datos necesarios
    for path in dPathFile['Paths']:
        Data = pd.read_csv(path, error_bad_lines=False, header = 0)
        dicc = {}
        Current = Data['I_out_calc']
        Efficiency = Data['Efficiency__calc']
        dicc['Current'] = Current
        dicc['Efficiency'] = Efficiency
##      Guardar los datos en un diccionario
        dDatos[dPathFile['files'][count]] = dicc
        count = count + 1

    return dDatos

def AddPlt(dDatos):
    Nameplot = ''
##  iterador para agregar los datos a la grafica
    for files,diccxy in dDatos.items():
        name = files.split('.')
        x = np.array(diccxy['Current'])
        y = np.array(diccxy['Efficiency'])

        plt.plot(x,y, marker = 'o', label = name[0])
        Nameplot = Nameplot + f'[{name[0]}] '

        plt.legend (loc = "lower right")
        plt.grid()
    return Nameplot


def SaveImagen(name,dDatos,Count):
    PathImages = f"C:/Users/ranguian/OneDrive - Intel Corporation/Documents/Projects/SDW/ps0_vrci Core/images/{name}.png"
    plt.savefig(PathImages)
##  obtener MaxEffc
    MaxEff_Current = FineValues(dDatos)
    if Count == 3 :
        report4 = Report(PathImages,MaxEff_Current)
        report4.PDFReport()
    elif Count == 2:
        report3 = Report(PathImages,MaxEff_Current)
        report3.PDFReport()
    elif Count == 1:
        report2 = Report(PathImages,MaxEff_Current)
        report2.PDFReport()
    elif Count == 0:
        report1 = Report(PathImages,MaxEff_Current)
        report1.PDFReport()




def FineValues(dDatos):
    n = 0
    lista = []
    MaxEff = 0
    diccMaxEff = {}
##  Hacer barrido para cada archivo
    for files,diccxy in dDatos.items():
        name = files.split('.')
        ## Encontrar el valor maximo
        for i in range (len(diccxy['Current'])):
            if diccxy['Efficiency'][i] > MaxEff:
                MaxEff = diccxy['Efficiency'][i]
                n = i
##      limpiar variable
        MaxEff = 0
##      Guardar datos MaxEff en el diccionario
        lista.append(diccxy['Efficiency'][n])
        lista.append(diccxy['Current'][n])
##      Guardar en diccionario key = nombre de archivo :Value =  Datos
        diccMaxEff[name[0]] = lista
##      limpiar lista
        lista = []
    return diccMaxEff

class Report:

    def __init__(self,path,MaxEff_Current):
        self.path = path
        self.MaxEff_Current = MaxEff_Current
        self.name = []
        self.MaxEff = []
        self.Current = []
##      Iterador para guardar los valores de cada documento
        for name in self.MaxEff_Current:
            self.name.append(name)
            self.MaxEff.append(self.MaxEff_Current[name][0])
            self.Current.append(self.MaxEff_Current[name][1])


    def PDFReport(self):
##      Crear pdf
        pdf = FPDF("P", "pt", "A4")
        pdf.add_page()
##      Titulo
        pdf.set_font("Arial", "B", 24)
        pdf.cell(0, 24, "Efficiency report",0,2)
        pdf.ln()

##      Tabla
        pdf.set_font("Arial", "B", 15)
        pdf.cell(0,15,'|    {:^20}     |      {:^15}       |   {:^15}  |'.format('Name','Efficiency','Current'),0,2 )
##      Print los dactos de cada Documento
        for i in range(len(self.name)):
            pdf.cell (150,15,f'| {self.name[i][0:10]}',0,0)
            pdf.cell (150,15,'| {:<15.6}'.format(self.MaxEff[i]),0,0)
            pdf.cell (150,15,'|  {:<15.6}   |'.format(self.Current[i]),0,1)

##      Agregar imagen de la grafica
        pdf.image(self.path, x = 100, w = 400)
##      Guardar Documento PDF
        pdf.output(f'C:/Users/ranguian/OneDrive - Intel Corporation/Documents/Projects/SDW/ps0_vrci Core/PDF/{self.name}.pdf')



#Data4.csv, Data1.csv, Data2.csv, Data3.csv

plt.title("Efficiency")
plt.xlabel("Amperes")
plt.ylabel("Efficiency %")
##  linea de referencia
plt.axhline(.85, color = 'red' ,alpha = .3 , linestyle = 'dashed')

menu()

