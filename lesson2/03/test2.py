point = input("点数を入力してください：")

point = int(point)
if point >= 0: # 外側のif文
  if point < 40:
    print("不合格")
  elif point < 60:
    print("もう少し頑張りましょう")
  elif point < 80:
    print("なんとか合格")
  else:
    print("大変よくできました")
else:
  print("正の値を入力してください") # pointが負の値の場合
  