import tkinter as tk
import os
import random

def uranau():
  # 占いを実行する リストkujisからランダムに要素を取り出す
  show_kuji["image"] = random.choice(kujis)

def clear():
  # 占いをクリアする デフォルトのイメージを表示
  show_kuji["image"] = default_img

# メインウインドウ
root = tk.Tk()
# タイトル
root.title("おみくじ")

# ボタンを配置するフレーム
btn_frame = tk.Frame(root, padx=10, pady=20)
btn_frame.pack()
# 「占う」ボタン
uranau_btn = tk.Button(btn_frame, text="占う", command=uranau)
uranau_btn.pack(side='left')
# 「クリア」ボタン
clear_btn = tk.Button(btn_frame, text="クリア", command=clear)
clear_btn.pack(side='left')

# デフォルトのイメージを読み込み（パスの相違を吸収）
default_img = tk.PhotoImage(
  file=os.path.join(os.path.dirname(__file__), "kujis/empty.png")
)
# くじの4つのイメージファイルをPhotoImageオブジェクトとして代入
kujis = [tk.PhotoImage(file=os.path.join(
  os.path.dirname(__file__), "kujis/kyo.png")),
  tk.PhotoImage(file=os.path.join(
    os.path.dirname(__file__), "kujis/syoukiti.png")),
  tk.PhotoImage(file=os.path.join(
    os.path.dirname(__file__), "kujis/chukiti.png")),
  tk.PhotoImage(file=os.path.join(
    os.path.dirname(__file__), "kujis/daikiti.png"))]

# Labelコンストラクタのimageオプションで、ラベルの初期画像を設定
show_kuji = tk.Label(root, image=default_img)
show_kuji.pack()

# メインループ
root.mainloop()
