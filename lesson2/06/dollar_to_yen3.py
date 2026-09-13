# 為替レートをデフォルト値を160にする
def dollar_to_yen(dollar, rate=160):
  yen = dollar * rate
  return yen

dollar = 5
yen = dollar_to_yen(dollar, rate=150)
print(f"{dollar}ドルは{yen}です")

dollar = 10
yen = dollar_to_yen(dollar)
print(f"{dollar}ドルは{yen}円です")
