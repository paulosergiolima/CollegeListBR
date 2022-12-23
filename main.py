import requests
import pyexcel as pe
import os
import json
from openpyxl import load_workbook, Workbook
#year = input('Me de o ano que você quer checar')
path_enade = '/home/paulolima/get_best_colleges/conceito_enade.xlsx'
path_idd = '/home/paulolima/get_best_colleges/conceito_idd.xlsx'
year = 2021
url_link = f'https://download.inep.gov.br/educacao_superior/indicadores/resultados/{year}'
url_link_enade = f'{url_link}/conceito_enade_{year}.xlsx'
url_link_idd = f'{url_link}/IDD_{year}.xlsx'
print(url_link_enade)
if not os.path.exists(path_enade):
    conceito_enade = requests.get(url_link_enade, verify=False)
    open("conceito_enade.xlsx", "wb").write(conceito_enade.content)
if not os.path.exists(path_idd):
    print("hallo")
    conceito_idd = requests.get(url_link_idd, verify=False)
    open("conceito_idd.xlsx", "wb").write(conceito_idd.content)


enade_wb = load_workbook(filename='conceito_enade.xlsx')
idd_wb = load_workbook(filename='conceito_idd.xlsx')

enade_ws = enade_wb.active
enade_array = []

new_enade = Workbook()
new_enade_ws = new_enade.active
new_enade_ws

#print(enade_ws.rows)
for data in enade_ws['C']:
    print(data.value)
    if data.value != None and data.value.strip() == "CIÊNCIA DA COMPUTAÇÃO":
        #print(data.row)
        enade_array.append(data.value)
