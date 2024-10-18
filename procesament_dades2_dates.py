'''
Grup 3: Jiajun, Ian, Miguel, Adria, Jordi
Data: 25 d'octubre de 2024
Professor: Javier Amaya
Asignatura: ASIXcB MDS TA03
Descripció: llegueix les dades XML obtingudes per un fitxer i mostria per pantalla la informació obtinguda.
'''

# Módulos
import xml.etree.ElementTree as ET
from datetime import datetime

# Variables
archivo_xml = 'incidencia.xml'
lista = []

# Declaración del archivo XML
tree = ET.parse(archivo_xml)
root = tree.getroot()

def validar_fecha(fecha_incidencia):
    if int(fecha_incidencia[6:10]) <= datetime.now().year and int(fecha_incidencia[3:5]) <= datetime.now().month and int(fecha_incidencia[3:5]) != "07" and int(fecha_incidencia[3:5]) != "08":
        return True
    else:
        return False

# Bucle para hacer la lista
for fila in root.findall('row'):
    fecha_incidencia = fila.find('DATA_DE_LA_INCIDÈNCIA').text
    if validar_fecha(fecha_incidencia):
        fila_info = [
            fila.find('Marca_de_temps').text,
            fila.find('Adreça_electrònica').text,
            fila.find('Informació_relativa_sobre_la_protecció_de_dades').text,
            fila.find('NOM_i_COGNOMS_Formador_a_que_obre_incidència').text,
            fila.find('DATA_DE_LA_INCIDÈNCIA').text,
            fila.find('TIPUS_INCIDÈNCIA').text,
            fila.find('AULA_SALAConsulteu_cartell_d_entrada_a_l_aula_o_l_espai_També_disposeu_d_aquesta_informació_a_trainers_itb_cat_espais').text,
            fila.find('EQUIPS_i_o_SERVEIS_AFECTATSNúmero_SACE_seregrafiat_si_disposa_').text,
            fila.find('EQUIPS_i_o_SERVEIS_AFECTATSNúmero_etiqueta_blanca').text,
            fila.find('DESCRIPCIÓ_PROPOSTA_DE_SOLUCIOLa_vostra_resposta').text,
            fila.find('NIVELL_URGENCIA_DE_SOLUCIÓ').text
        ]
        # Añade los datos de la fila a la lista
        lista.append(fila_info)
print(lista)
