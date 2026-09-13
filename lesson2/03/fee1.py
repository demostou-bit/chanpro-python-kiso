age = input("年齢を入力してください：")
age = int(age)

if age <= 7 or age >= 60: #年齢が7歳以下もしくは60歳以上
  print("入場料は無料です")
elif age <= 12:
  print("入場料は1,000円です")
else:
  print("入場料は2,000円です")

