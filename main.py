import requests
year = input('Me de o ano que você quer checar')
url_link = f'https://download.inep.gov.br/educacao_superior/indicadores/resultados/{year}'
url_link_enade = f'{url_link}/conceito_enade_{year}.ods'
url_link_idd = f'{url_link}/IDD_{year}.ods'
conceito_enade = requests.get(url_link_enade, verify=False)
conceito_idd = requests.get(url_link_idd, verify=False)
open("conceito_enade.ods", "wb").write(conceito_enade.content)
open("conceito_idd.ods", "wb").write(conceito_idd.content)