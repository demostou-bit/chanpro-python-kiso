# name（名前）とpref（出身地）を引数に、
# 私は～です。生まれは～です。と表示する
def say_hello(name, pref):
  print(f"私は{name}です。生まれは{pref}です。")

say_hello("中田厳", "東京")

# キーワード指定して呼び出す
say_hello(name="佐藤敦", pref="仙台")

# 引数の順番は変えられる
# 以下の記述はエラー
# say_hello(name="中田厳", "東京")