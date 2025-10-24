import requests
import json
import pandas as pd
from datetime import datetime, timedelta

#args
url_example = 'https://www.cbr-xml-daily.ru/archive/2025/09/25/daily_json.js'
url_main = 'https://www.cbr-xml-daily.ru/archive/'
url_postfix = '/daily_json.js'

#calendar
end_date = datetime.today()
start_date = end_date.replace(year=end_date.year - 5)
dates = pd.date_range(start=start_date, end=end_date, freq='MS')

def get_data(date, url_main, url_postfix):
    date_str = date.strftime('%Y/%m/%d')
    url = f'{url_main}{date_str}{url_postfix}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        usd_rate = data['Valute']['USD']['Value']
        result_dict = {}
        result_dict['date'] = date
        result_dict['usd_rate'] = usd_rate
        return result_dict
#main
records = []

for date in dates:
    records.append(get_data(date, url_main, url_postfix))

print(records)