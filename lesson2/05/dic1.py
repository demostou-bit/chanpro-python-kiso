# for文の使用して辞書の要素を順に取得する
seasons = {"spring":"春", "summer":"夏", "autumn":"秋", "winter":"冬"}

for key in seasons.keys():
  print(f"キー： {key}, 値: {seasons[key]}")
  