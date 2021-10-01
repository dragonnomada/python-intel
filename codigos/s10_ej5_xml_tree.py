# <root>
#   <node id="1" color="red">
#       <node id="1.1">
#       <node id="1.2">
#   </node>
#   <node id="2" color="red">
#       <node id="2.1">
#       <node id="2.2">
#       <node id="2.3">
#   </node>
# </root>

# Importación DESDE-PARTES `from <libreria.submodulo> import <parte>`
from xml.etree import ElementTree

f = open("datos/catalogo.xml", "r")

tree = ElementTree.parse(f)

f.close()

nodoCATALOGO = tree.getroot()

print(nodoCATALOGO)

# Nivel 1

catalog = []

for nodoCD in nodoCATALOGO.iter("CD"):
    print(nodoCD)
    cd = {}
    for nodoTITLE in nodoCD.iter("TITLE"):
        print(nodoTITLE.text)
        cd["title"] = nodoTITLE.text
    for nodoARTIST in nodoCD.iter("ARTIST"):
        print(nodoARTIST.text)
        cd["artist"] = nodoARTIST.text
    catalog.append(cd)
    
print(catalog)