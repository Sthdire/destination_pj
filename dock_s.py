import gspread

sa = gspread.service_account()
sh = sa.open("testy")
hs = sh.worksheet("com")

print(hs.acell('B11').value)