# ドルから円の金額を求める関数を定義する
def dollar_to_yen(dollar, rate):
    yen = dollar * rate
    return yen

dollar = 5
rate = 160
yen = dollar_to_yen(dollar, rate)
print(f"{dollar}ドルは{yen}円です")

dollar = 10
yen = dollar_to_yen(dollar, rate)
print(f"{dollar}ドルは{yen}円です")
