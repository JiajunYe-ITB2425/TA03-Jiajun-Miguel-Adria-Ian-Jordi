import xml.etree.ElementTree as ET
from datetime import datetime

archivo_xml = 'Incidencias2.0.xml'
lista = []

tree = ET.parse(archivo_xml)
root = tree.getroot()

for fila in root.findall('row'):
    fecha_incidencia = fila.find('DATA_DE_LA_INCIDÈNCIA').text
    fecha_incidencia_dt = datetime.strptime(fecha_incidencia, '%d/%m/%Y')

    # Verificar si la fecha de la incidencia es menor o igual a la fecha actual
    if fecha_incidencia_dt <= datetime.now():
        fila_info = [
            fila.find('Marca_de_temps').text,
            fila.find('Adreça_electrònica').text,
            fila.find('Informació_relativa_sobre_la_protecció_de_dades').text,
            fila.find('NOM_i_COGNOMS_Formador_a_que_obre_incidència').text,
            fecha_incidencia,
            fila.find('TIPUS_INCIDÈNCIA').text,
            fila.find(
                'AULA_SALAConsulteu_cartell_d_entrada_a_l_aula_o_l_espai_També_disposeu_d_aquesta_informació_a_trainers_itb_cat_espais').text,
            fila.find('EQUIPS_i_o_SERVEIS_AFECTATSNúmero_SACE_seregrafiat_si_disposa_').text,
            fila.find('EQUIPS_i_o_SERVEIS_AFECTATSNúmero_etiqueta_blanca').text,
            fila.find('DESCRIPCIÓ_PROPOSTA_DE_SOLUCIOLa_vostra_resposta').text,
            fila.find('NIVELL_URGENCIA_DE_SOLUCIÓ').text
        ]
        # Añadir los datos de la fila a la lista
        lista.append(fila_info)

# Imprimir la lista resultante
print(lista)
