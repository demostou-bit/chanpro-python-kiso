# プログラムを保存したディレクトリの下の「images」ディレクトリの
# 「radio1.png」をラベルに表示する例
# ただし、no such file directoryエラーになる

import tkinter as tk

# メインウィンドウ
root = tk.Tk()
# フレーム
frame = tk.Frame(root)
frame.pack()

# PhotoImageオブジェクトを生成
my_image = tk.PhotoImage(file="images/radio1.png")
# ラベルに表示
label = tk.Label(frame, image=my_image)
label.pack()

root.mainloop()
