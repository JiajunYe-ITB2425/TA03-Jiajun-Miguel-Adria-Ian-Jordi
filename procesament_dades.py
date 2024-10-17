'''
Grup 3: Jiajun, Ian, Miguel, Adria, Jordi
Data: 25 d'octubre de 2024
Professor: Javier Amaya
Asignatura: ASIXcB MDS TA03
Descripció: llegueix les dades XML obtingudes per un fitxer i mostria per pantalla la informació obtinguda.
'''

import xml.etree.ElementTree as ET

# Cargar el archivo XML
archivo_xml = 'incidencies1.xml'

# Parsear el archivo
arbol = ET.parse(archivo_xml)

# Obtener el elemento raíz
raiz = arbol.getroot()

# Mostrar el contenido del archivo XML
for elemento in raiz:
    print(elemento.tag, elemento.attrib)
    for subelemento in elemento:
        print(f"  {subelemento.tag}: {subelemento.text}")
