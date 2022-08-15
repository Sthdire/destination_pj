import requests

path = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

def get_rub_value(usd_value):
    return path['Valute']['USD']['Value'] * usd_value







