# 1番目と3番目のラベルを横一杯に広げる
import tkinter as tk

root = tk.Tk()

root.title("初めてのtkinter")

root.geometry("200x100")

# ラベルの配置
label1 = tk.Label(root, text="ラベル1", bg="yellow")
label1.pack(fill=tk.X)
label2 = tk.Label(root, text="ラベル2", bg="orange")
label2.pack()
label3 = tk.Label(root, text="ラベル3", bg="pink")
label3.pack(fill=tk.X)

root.mainloop()

