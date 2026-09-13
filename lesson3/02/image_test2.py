# image_test1.pyを任意のディレクトリから実行できるようにする
import tkinter as tk
 #1 OSによるパスの違いを吸収するためにインポート
import os.path

# メインウィンドウ
root = tk.Tk()
# フレーム
frame = tk.Frame(root)
frame.pack()

image_path = "images/radio1.png"
#2 dirname関数でディレクトリのパスを求める
dir_path = os.path.dirname(__file__)
#3 join関数でimage_pathと連結し絶対パスにしています
image_path = os.path.join(dir_path, image_path)

# PhotoImageオブジェクトを生成
my_image = tk.PhotoImage(file=image_path)
# ラベルに表示
label = tk.Label(frame, image=my_image)
label.pack()

root.mainloop()