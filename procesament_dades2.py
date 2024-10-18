import xml.etree.ElementTree as ET
from datetime import datetime


# Función para validar fechas
def es_fecha_valida(fecha_str):
    try:
        # Intenta convertir la fecha en formato correcto (dd/mm/yyyy)
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        # Define una fecha mínima válida (en este caso, 1 de enero de 2020)
        fecha_limite = datetime(2024, 10, 18)
        return fecha >= fecha_limite
    except ValueError:
        # Si no puede convertir la fecha, se considera no válida
        return False


# Cargar el archivo XML
ruta_archivo = "Incidencias2.0.xml"  # Cambia esto por la ruta real
arbol = ET.parse(ruta_archivo)
raiz = arbol.getroot()

# Crear una nueva raíz para almacenar las incidencias válidas
nueva_raiz = ET.Element("root")

# Procesar cada fila
for row in raiz.findall('row'):
    # Obtener la fecha de la incidencia
    fecha_incidencia = row.find('DATA_DE_LA_INCIDÈNCIA').text

    # Verificar si la fecha es válida
    if es_fecha_valida(fecha_incidencia):
        # Si es válida, añadir la incidencia a la nueva raíz
        nueva_raiz.append(row)

# Crear el nuevo árbol XML con las incidencias filtradas
nuevo_arbol = ET.ElementTree(nueva_raiz)

# Guardar el nuevo archivo XML
nuevo_arbol.write("Incidencias_filtradas.xml", encoding="utf-8", xml_declaration=True)

print("Incidencias filtradas guardadas en 'Incidencias_filtradas.xml'")
