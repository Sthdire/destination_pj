import csv
import io
import urllib.request
from db_methods import save_values
from db_methods import delete_values
from cb_rf_course import get_rub_value

# get values from google sheets and save it to database
def save_db_values():
    delete_values()

    url = 'https://docs.google.com/spreadsheets/d/11FkagmZbctyjr0QQRksIBKCIlN_vxY8BhHcniBG43OA/export?format=csv'

    response = urllib.request.urlopen(url)

    with io.TextIOWrapper(response, encoding='utf-8') as f:
        reader = csv.reader(f)

        for row in reader:
            if row[2] == 'стоимость,$':
                continue
            else:
                x = round(get_rub_value(int(row[2])), 2)
                save_values(row[0], row[1], row[2], row[3], x)
        print('successfully saved values')
    pass
