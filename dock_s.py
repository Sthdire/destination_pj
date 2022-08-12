import gspread
from db_methods import save_values

sa = gspread.service_account()
sh = sa.open("testy")
hs = sh.worksheet("com")

for i in range(hs.row_count):
    i += 2
    A = 'A' + str(i)
    B = 'B' + str(i)
    C = 'C' + str(i)
    D = 'D' + str(i)
    E = 0
    if not hs.acell(A).value:
        break
    else:
        save_values(int(hs.acell(A).value), int(hs.acell(B).value), int(hs.acell(C).value), hs.acell(D).value, E)
        print(i)

#код выше работает, но после прохождения части цикла, выдает ошибку

#print(hs.acell('B11').value)