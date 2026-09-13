# ラムダ式を変数に代入しておくと、defで定義した関数のように呼び出せます
dollar_to_yen = lambda dollar, rate=160: dollar * rate

dollar = 10
yen = dollar_to_yen(dollar)
print(f"{dollar}ドルは{yen}円です")
