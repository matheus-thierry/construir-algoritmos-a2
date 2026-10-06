import requests
from datetime import datetime, timedelta, date
DATE_FORMAT = "%m-%d-%Y"

def cotar(data):
    url = fr"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json&$select=cotacaoCompra"
    res = requests.get(url)
    res = res.json()
    if res['value']: 
        return res['value'][0]['cotacaoCompra']
    else:
        dia_anterior = datetime.strptime(data, DATE_FORMAT) - timedelta(1)
        dia_anterior = datetime.strftime(dia_anterior, DATE_FORMAT)
        return cotar(dia_anterior)

lista = [cotar(i) for i in ["09-02-2024", "09-01-2024", "08-31-2024", "08-30-2024", "08-29-2024"]]
print(lista)