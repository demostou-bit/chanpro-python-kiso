import sys #1 プログラムの途中で終了するためのモジュール

age = input("年齢を入力してください：")
#2 tryブロック
try:
  age = int(age) #3 ageを整数に変換
except ValueError: #4 ValueErrorが発生した
  print("年齢は整数で入力してください") #5 ValueErrorが発生した場合に表示
  sys.exit() #6 メッセージ表示後、プログラムを終了

if age >= 18:
  print("成年です")
else:
  print("未成年です")

# try~except文
# try:
#   例外が発生する可能性がある処理
# except 例外:
#   例外が発生した場合の処理
