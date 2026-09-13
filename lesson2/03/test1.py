# 入力した点数に応じたメッセージを表示するプログラム
point = input("点数を入力してください：")

point = int(point)
if point < 40:
  print("Kiai Ga Tarinai")
elif point < 60:
  print("もう少し頑張りましょう")
elif point < 80:
  print("何とか合格")
else:
  print("Kiaiが十分です")

# elif文
# if 条件式A:
#   条件式Aが成立した場合のブロック
# elif 条件式B:
#   条件Aが成立せず、条件Bが成立した場合のブロック
# elif 条件式C:
#   条件AとBが成立せず、条件Cが成立した場合のブロック
# ...
# else:
#   いずれの条件も成立した場合のブロック
