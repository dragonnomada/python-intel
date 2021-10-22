#from numpy.lib.financial import _ppmt_dispatcher
from numpy.core.arrayprint import _guarded_repr_or_str
from reporteVtas import Reportes
from matplotlib.backends.backend_pdf import PdfPages
import os
import pdfkit

reporte = Reportes()
class Topdf:
    
    def convertirHTML(self,Data_frame):
        df = Data_frame.to_html()
        return df
        #with PdfPages("data/reporte.pdf","a") as pdf:
    
    def guardarImagenes(self, listaFechas):
        sku_list=[]
        for fecha in listaFechas:
            temp = reporte.productoMasvendido(1,fecha,fecha)
            sku = temp["SKU"].values
            sku_list.append(sku[0])
        
        for sku in sku_list:
            temp = reporte.reportePorPruductoDiario(sku)
            name = sku + ".png"
            temp.savefig(name,bbox_inches='tight')
        

    def crearHTML(self,sku):
        dir = os.path.abspath(os.getcwd())
        dir = dir.replace("\\","/") + "/"
        #print(dir)
        #listaFechas = ["10/10/2021","10/11/2021","10/12/2021","10/13/2021","10/14/2021","10/15/2021","10/16/2021"]
        #self.guardarImagenes(listaFechas)
        
        nombreImagen = "data/"+sku+".png"
        temp = reporte.reportePorPruductoDiario(sku)
        temp.savefig(nombreImagen,bbox_inches='tight')
        html_template = """
        <html>
        <head>
        <title>Reporte Vtas</title>
        </head>
        <body>
        <h2><center>Reporte de Ventas de Productos</h2>
        <p>
        <center>Top {} productos vendidos del {} al {}<br/><br/>

        Se muestra los 5 productos mas Vendidos y la ganancia que Genero.<br/><br/>

        <center>{}

        </p>
        <p><br/><br/><br/>
            <p>Mejores Productos por dia del {} al {}</p>
            <table class="default">
                <tr>
                    <td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td>
                <tr>
            </table><br/><br/><br/>
            Historial del Producto mas vendido
            <br/><br/>
            <img src="{}">
        </p>
        </body>
        </html>
        """.format(
            5, "10/10/2021","10/16/2021",
            self.convertirHTML(reporte.productoMasvendido(5,"10/10/2021","10/16/2021")),
            "10/10/2021","10/16/2021",
            self.convertirHTML(reporte.productoMasvendido(1,"10/10/2021","10/10/2021")),
            self.convertirHTML(reporte.productoMasvendido(1,"10/11/2021","10/11/2021")),
            self.convertirHTML(reporte.productoMasvendido(1,"10/12/2021","10/12/2021")),
            self.convertirHTML(reporte.productoMasvendido(1,"10/13/2021","10/13/2021")),
            self.convertirHTML(reporte.productoMasvendido(1,"10/14/2021","10/14/2021")),
            self.convertirHTML(reporte.productoMasvendido(1,"10/15/2021","10/15/2021")),
            self.convertirHTML(reporte.productoMasvendido(1,"10/16/2021","10/16/2021")),
            dir+nombreImagen
        )

        f = open("data/ReporteVenta.html",'w')
        f.write(html_template)
        f.close()



if __name__ == "__main__":
    crearReporte = Topdf()
    #df = reporte.productoMasvendido(5)
    listaFechas = ["10/10/2021","10/11/2021","10/12/2021","10/13/2021","10/14/2021","10/15/2021","10/16/2021"]
    crearReporte.crearHTML("C500D")
    