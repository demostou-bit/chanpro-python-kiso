# パディング（余白）を設定
import tkinter as tk

root = tk.Tk()

root.title("初めてのtkinter")

root.geometry("400x100")

# 余白を設定
label1 = tk.Label(root, text="ラベル1", bg="yellow")
label1.pack(side=tk.LEFT, padx=10) # 外側の横の余白を10ピクセル
label2 = tk.Label(root, text="ラベル2", bg="orange")
label2.pack(side=tk.LEFT, ipady=20) # 内側の縦の余白を20ピクセル
label3 = tk.Label(root, text="ラベル3", bg="pink")
label3.pack(side=tk.LEFT, ipadx=10, ipady=10) # 内側の横と縦の余白を10ピクセル

root.mainloop()
