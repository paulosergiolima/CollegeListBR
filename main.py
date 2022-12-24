import requests
import pyexcel as pe
import os
import json
from copy import copy
from string import ascii_uppercase as alc
from openpyxl import load_workbook, Workbook
#os.remove('nove_conceito_enade.xlsx')
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

try:
    os.remove('novo_conceito_enade.xlsx')
except:
    print('First time')

enade_wb = load_workbook(filename='conceito_enade.xlsx')
idd_wb = load_workbook(filename='conceito_idd.xlsx')
enade_ws = enade_wb.active
enade_array = []

new_enade = Workbook()
new_enade_ws = new_enade.active
#new_enade_ws
header_array = []
new_enade_ws.row_dimensions[1] = enade_ws.row_dimensions[1]
for i in alc:
    header_array.append(enade_ws[f'{i}1'].value)
    new_enade_ws.column_dimensions[i] = enade_ws.column_dimensions[i]
    print('test',i)

new_enade_ws.append(header_array)

for i in alc:
    new_enade_ws[f'{i}1'].font = copy(enade_ws[f'{i}1'].font)
    new_enade_ws[f'{i}1'].style = copy(enade_ws[f'{i}1'].style)
    new_enade_ws[f'{i}1'].border = copy(enade_ws[f'{i}1'].border)
    new_enade_ws[f'{i}1'].alignment = copy(enade_ws[f'{i}1'].alignment)
#print(enade_ws.rows)
for data in enade_ws['C']:
    #print(data.value)
    if data.value != None and data.value.strip() == "CIÊNCIA DA COMPUTAÇÃO":
        #print(data.row)
        enade_array.append(data.row)


for data in enade_array:
    cool_array = []
    for i in alc:
        #print(enade_ws[f'{i}{data}'].value)
        cool_array.append(enade_ws[f'{i}{data}'].value)
    #print(cool_array)
    new_enade_ws.append(cool_array)
new_enade.save(filename='novo_conceito_enade.xlsx')