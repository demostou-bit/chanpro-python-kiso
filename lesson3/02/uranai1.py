# おみくじを文字列で表示する
import tkinter as tk
import random

def uranau():
  # 占いを実行する
  show_kuji["text"] = random.choice(kujis) #1 要素をランダムに取り出す

def clear():
  # 占いをクリアする
  show_kuji["text"] = "" #2 空文字にする

# メインウィンドウ
root = tk.Tk()
# タイトル
root.title("おみくじ")

# geometryメソッドでウィンドウのサイズを「横×縦」で設定
root.geometry("300x200")

#3 リストの要素を代入
kujis = ["大吉", "中吉", "小吉", "凶"]

#4 ボタンを格納するフレームを作成
btn_frame = tk.Frame(root, padx=10, pady=20)
btn_frame.pack()
#5 フレーム内部に「占う」ボタンを配置
uranau_btn = tk.Button(btn_frame, text="占う", command=uranau, bg="lightblue")
uranau_btn.pack(side='left')
#6 フレーム内部に「クリア」ボタンを配置
clear_btn = tk.Button(btn_frame, text="クリア", command=clear, bg="yellow")
clear_btn.pack(side='left')

# 占い結果を表示するラベルの初期設定
show_kuji = tk.Label(root, image="", font=("Helvetica", 30, "bold"))
show_kuji.pack()

# メインループ
root.mainloop()