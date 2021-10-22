import matplotlib.pyplot as plot
from csv import reader
from csv import writer
file=r'C:\Users\smparril\Downloads\Perdidas_Productos_K908HKL.csv'
outputfile=r'C:\Users\smparril\Downloads\outputfile.csv' #se genera automaticamente.
f=open(file, 'r')
b=f.readlines() #Aqui tienes todas las lineas de tu CSV
new_dato=[] #Lista vacia donde se guardaran los nuevos datos
lista_producto = []

for i in b[1:]:
    row=i.split(',') #Crea una serie de listas en forma de columnas
    eficiencia=row[6].replace('\n','') #Quito el salto de pagina de cada valor de la columna
    new_dato.append(float(eficiencia)*0.9 #Cada elemento de la columna efficency lo comnvierto en un flotante
    partes = row[0].replace('\n','') #Quito el salto de pagina de cada valor de la columna
    lista_producto.append(partes)

plot.bar(lista_producto ,new_dato)
plot.xlabel('Numero de parte')
plot.ylabel('Eficiencia')
plot.show()

with open(file, 'r') as read_obj, open(outputfile,'w',newline='') as write_obj: #Abro el primer archivo y reescribo en el que se creara
    csv_reader = reader(read_obj)
    csv_writer = writer(write_obj)
    n=0
    for row in csv_reader:
        if csv_reader.line_num==1: #En la primera linea agrega el nombre de la columna
            row.append('NewDato')
        else:
            row.append(float(new_dato[n])) #En las lineas subsecuentes agrega los nuevos datos correspondientes
            n=n+1
        csv_writer.writerow(row)  #Describe en el archivo generado