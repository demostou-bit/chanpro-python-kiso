# 為替レート
RATE = 160 # 160を代入し、定数として使用

# input関数によりキーボードからドルの金額を入力し、変数に代入
dollar_str = input("ドルの金額を入力してください：")
# float関数で数値に変換し、変数に代入
dollar = float(dollar_str)
# 変数dollarとRATEの値を掛け算して円の金額を計算し、yenに代入
yen = dollar * RATE
# フォーマット文字列を使用してdollarとyenの値を埋め込んで結果を表示
print(f"{dollar}ドルは{yen}円です")
