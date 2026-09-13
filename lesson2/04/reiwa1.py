# 令和の年を西暦に変換
#1 rangeコンストラクタで1から10までカウントアップしてreiwaに代入
for reiwa in range(1, 11):
  #2 フォーマット文字列を使用してreiwaと、それに2018を足した西暦の年を埋め込む
  print(f"令和{reiwa} 年は西暦{reiwa + 2018} 年")
  