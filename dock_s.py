import time
import gspread
from db_methods import save_values
from cb_rf_course import get_rub_value




sa = gspread.service_account()
sh = sa.open("testy")
hs = sh.worksheet("com")

for i in range(hs.row_count):
    i += 2
    A = 'A' + str(i)
    B = 'B' + str(i)
    C = 'C' + str(i)
    D = 'D' + str(i)

    if not hs.acell(A).value:
        break
    else:
        if(i % 10 == 0):
            time.sleep(50)
        save_values(int(hs.acell(A).value), int(hs.acell(B).value), int(hs.acell(C).value), hs.acell(D).value, get_rub_value(int(hs.acell(C).value)))
        print(i)
