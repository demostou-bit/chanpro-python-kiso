# 文字列を出力
print("こんにちは、世界")

# + 演算子を使って文字列を連結
print("初めまして" + "Python")

# * 演算子を使って文字列を2回繰り返して連結
print("こんにちは" * 2 + "Python")

# 数値と文字列はそのまま連結できない
# print("昭和" + 56 + "年")
# TypeError: can only concatenate str (not "int") to str

# 数値と文字列を連結するために数字の前にstr関数を使う
print("令和" + str(8) + "年")
