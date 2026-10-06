import requests
from datetime import datetime, timedelta, date
DATE_FORMAT = "%m-%d-%Y"

def cotar():
    dias = []
    dias.append(datetime.strftime(date.today(), DATE_FORMAT))
    for i in range(364):
        dia_anterior = datetime.strptime(dias[i], DATE_FORMAT) - timedelta(1)
        dia_anterior = datetime.strftime(dia_anterior, DATE_FORMAT)
        dias.append(dia_anterior)

    results = []
    for index, data in enumerate(dias):
        url = fr"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'&$top=100&$format=json&$select=cotacaoCompra"
        res = requests.get(url)
        res = res.json()
        
        if res['value']:
            results.append(res['value'][0]['cotacaoCompra'])
        else:
            results.append(results[index-1])

    return results

print(cotar)