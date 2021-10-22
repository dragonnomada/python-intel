import pandas as pd
import matplotlib.pyplot as plt
#from toPDF import Topdf 
fileCsv = "C:/Users/errochan/OneDrive - Intel Corporation/Documents/PythonIntroduction/Ejercicios/Proyecto/data/dataVtas.csv"
class Reportes:

    def gananciaTotal(self,fila):
        resultado = fila["CantidadVendida"] * fila["Ganancia"]
        return resultado

    def ventasFecha(self,fechaInicio, fechaFinal):
        df = pd.read_csv(fileCsv)
        df["GananciaTotal"] = df.apply(self.gananciaTotal,axis=1)
        df_fechas = df[(df["FechaVta"] >= fechaInicio) & (df["FechaVta"] <= fechaFinal)]
        df_Cantidades = df_fechas.groupby("SKU",as_index=False).agg({"CantidadVendida":'sum',"GananciaTotal":'sum'})
        df_masVendida = df_Cantidades.sort_values("CantidadVendida",ascending=False)
        return df_masVendida

    def productoMasvendido(self,top = 0, fechaInicio = "", fechaFinal = ""):
        df = pd.read_csv(fileCsv)
        fecha_min = df["FechaVta"].min()
        fecha_max = df["FechaVta"].max()
        df["GananciaTotal"] = df.apply(self.gananciaTotal,axis=1)
        
        if top == 0:
            top = len(df.index)

        if fechaInicio == "" and fechaFinal =="":
            #print("Top {} de los productos mas vendidos del {} al {}".format(top,fecha_min,fecha_max))
            df_masVendida= self.ventasFecha(fecha_min,fecha_max)
            return(df_masVendida.head(top))
        
        elif fechaInicio != "" and fechaFinal != "":
            #print("Top {} de los productos mas vendidos del {} al {}".format(top,fechaInicio,fechaFinal))
            df_masVendida = self.ventasFecha(fechaInicio,fechaFinal)
            return(df_masVendida.head(top))

        elif fechaInicio != "" and fechaFinal == "":
            print("Falta Fecha Final")
        elif fechaInicio == "" and fechaFinal != "":
            print("Falta Fecha de Inicio")

    def reportePorPruductoDiario(self,SKU):
        df = pd.read_csv(fileCsv)
        fechas = df["FechaVta"].drop_duplicates()
        x_CantidadVendida = []
        print(type(fechas))
        for fecha in fechas:
            #df_fechas = df[(df["FechaVta"] == fecha)]
            df_fechas = self.ventasFecha(fecha,fecha)
            tempDF=df_fechas[(df_fechas["SKU"] == SKU)]
            #print(tempDF)
            tempValue = tempDF["CantidadVendida"].values
            if tempValue.size > 0 :
                x_CantidadVendida.append(int(tempValue))
            else:
                x_CantidadVendida.append(0)
        plt.plot(fechas.values, x_CantidadVendida)
        plt.title("SKU product: {}".format(SKU))
        plt.xlabel('Dias')
        plt.ylabel('Cantidades Vendidas')
        return plt
    
if __name__ == "__main__":
    reporte = Reportes()
    print(reporte.productoMasvendido(5))
    print()
    print(reporte.productoMasvendido(3,"10/12/2021", "10/14/2021"))
    print()
    a = reporte.reportePorPruductoDiario("C500D")
    a.show()
