# Pillowを使用して「images/bird.jpg」をラベルに表示する例
import tkinter as tk
import os
from PIL import Image, ImageTk

# メインウィンドウ
root = tk.Tk()
# タイトル
root.title("Pillowのテスト")

file_path = os.path.join(os.path.dirname(__file__), "images/bird.jpg")
photo_pil = Image.open(file_path) #1 PIL Imageオブジェクトを生成
photo_tk = ImageTk.PhotoImage(photo_pil) #2 PhotoImageオブジェクトに変換
label = tk.Label(image=photo_tk) #3 photo_tkをラベルに表示
label.pack()

# メインループ
root.mainloop()
