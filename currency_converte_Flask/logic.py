import requests

def currency_converter(base,summa,to_currency):
    link = 'http://api.fixer.io/latest?base={}'.format(base)
    req = requests.get(link)
    data = req.json()
    for currency in data['rates'].keys():
        if to_currency == currency:
            result = data['rates'][currency] * summa
    return result
