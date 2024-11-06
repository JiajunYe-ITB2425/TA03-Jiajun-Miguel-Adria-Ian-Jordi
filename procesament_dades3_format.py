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
archivo_xml = 'incidencies.xml'
lista = []

# Ens hem inventat una llista d'aules
lista_aulas = ["200", "201", "202", "203", "204", "205", "206", "207", "208", "209", "210"]

# Códigos de color
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"

# Declaración del archivo XML
tree = ET.parse(archivo_xml)
root = tree.getroot()

# Función para validar la fecha (que sea del mismo año, mismo mes o anterior, que no sea ni julio ni agosto i que sea el mismo dia o anterior)
def validar_fecha(fecha_incidencia):
    return (int(fecha_incidencia[6:10]) == datetime.now().year and
            int(fecha_incidencia[3:5]) <= datetime.now().month and
            int(fecha_incidencia[3:5]) != 7 and
            int(fecha_incidencia[3:5]) != 8 and
            int(fecha_incidencia[0:2]) <= datetime.now().day)

# Función para validar que el aula esté en la lista de aulas
def validar_aula(aula):
    return aula in lista_aulas

# Bucle para hacer la lista
for fila in root.findall('row'):

    # Variables para las funciones
    fecha_incidencia = fila.find('DATA_DE_LA_INCIDÈNCIA').text
    aula = fila.find('AULA_SALAConsulteu_cartell_d_entrada_a_l_aula_o_l_espai_També_disposeu_d_aquesta_informació_a_trainers_itb_cat_espais').text

    # Uso de las funciones para validar los formularios
    if validar_fecha(fecha_incidencia) and validar_aula(aula):
        fila_info = {
            'Marca de temps': fila.find('Marca_de_temps').text,
            'Adreça electrònica': fila.find('Adreça_electrònica').text,
            'Informació sobre la protecció de dades': fila.find('Informació_relativa_sobre_la_protecció_de_dades').text,
            'Formador': fila.find('NOM_i_COGNOMS_Formador_a_que_obre_incidència').text,
            'Data de la incidència': fila.find('DATA_DE_LA_INCIDÈNCIA').text,
            'Tipus d\'incidència': fila.find('TIPUS_INCIDÈNCIA').text,
            'Aula/Sala': fila.find('AULA_SALAConsulteu_cartell_d_entrada_a_l_aula_o_l_espai_També_disposeu_d_aquesta_informació_a_trainers_itb_cat_espais').text,
            'Equips/Serveis afectats (SACE)': fila.find('EQUIPS_i_o_SERVEIS_AFECTATSNúmero_SACE_seregrafiat_si_disposa_').text,
            'Equips/Serveis afectats (Etiqueta blanca)': fila.find('EQUIPS_i_o_SERVEIS_AFECTATSNúmero_etiqueta_blanca').text,
            'Descripció proposta de solució': fila.find('DESCRIPCIÓ_PROPOSTA_DE_SOLUCIOLa_vostra_resposta').text,
            'Nivell urgència de solució': fila.find('NIVELL_URGENCIA_DE_SOLUCIÓ').text
        }

        # Añade los datos de la fila a la lista
        lista.append(fila_info)

# Output con formato (etiquetas, colores...)
for i, incidencia in enumerate(lista, start=1):
    print(f"{RED}Incidència {i}:{RESET}")
    for k, v in incidencia.items():
        print(f"{GREEN}{k}: {RESET}{v}")
    print(f"{BLUE}{'-' * 50}{RESET}")
