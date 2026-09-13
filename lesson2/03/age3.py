# age2.pyを条件式で記述
age = input("年齢を入力してください：")
age = int(age)
print("成年です" if age >= 18 else "未成年です")

# 整数に変換できない文字列を入力すると、ValueError
