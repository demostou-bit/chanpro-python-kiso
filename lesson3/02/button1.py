import tkinter as tk

# メインウインドウ
root = tk.Tk()
# タイトル
root.title("ボタンテスト")

# コールバック関数(クリックしたときのアクションとして実行する関数)の定義
def clicked():
  print("ボタンがクリックされました")

# Buttonウィジットを生成。commandオプションでクリックされたらclicked関数を呼び出す
btn1 = tk.Button(root, text="押してください", command=clicked, bg="yellow")
btn1.pack()

# メインループ
root.mainloop()
