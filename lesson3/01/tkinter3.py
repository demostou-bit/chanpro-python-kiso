# 左から横一列に配置する
import tkinter as tk

root = tk.Tk()

root.title("初めてのtkinter")

root.geometry("400x100")

# ラベルの配置
label1 = tk.Label(root, text="ラベル1", bg="yellow")
label1.pack(side=tk.LEFT)
label2 = tk.Label(root, text="ラベル2", bg="orange")
label2.pack(side=tk.LEFT)
label3 = tk.Label(root, text="ラベル3", bg="pink")
label3.pack(side=tk.LEFT)

root.mainloop()
