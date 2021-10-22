#Nombre: Delia Torres Muñoz
#Descripción: El siguiente codigo lee un archivo de ecxel toma los valores de columnas para realizar operaciones y calcula un parametro que se grafica con respecto al tiempo.
#Justificación: Al automatizar procesos es necesario que datos de salida sean manipulados para determinados y calculos y presentación de resultados.

import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
from fpdf import FPDF

df_hoja_1_datos = pd.read_excel("Libro2.xlsx", sheet_name="Hoja1", engine="openpyxl", usecols=['Voltaje','Corriente','Tiempo'])

hoja = df_hoja_1_datos.values.tolist()
column1 = df_hoja_1_datos.iloc[:, 0] 
x = column1.tolist()
column2 = df_hoja_1_datos.iloc[:, 1] 
y = column2.tolist()
column3 = df_hoja_1_datos.iloc[:, 2] 
t = column3.tolist()

Power=[]
for data1, data2, data3 in hoja:
  multi= data1 * data2
  Power.append(multi)

plt.plot(t,Power, 'bo--', color='red')
plt.show()
plt.savefig("figura1.png", dpi=5)
plt.xlabel("Tiempo")
plt.ylabel("Potencia")
# Guardar pdf
pdf= FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 15)
pdf.image("figura1.png", x=100, w=400)
pdf.output("reporte.pdf")