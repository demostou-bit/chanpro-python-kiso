# ラベルの幅と高さを指定する
import tkinter as tk

root = tk.Tk()

root.title("初めてのtkinter")

root.geometry("400x200")

# ラベルの配置
label1 = tk.Label(root, text="ラベル1", bg="yellow", width=15)
label1.pack(side=tk.LEFT)
label2 = tk.Label(root, text="ラベル2", bg="orange", width=10, height=5)
label2.pack(side=tk.LEFT)
label3 = tk.Label(root, text="ラベル3", bg="pink", width=20, height=3)
label3.pack(side=tk.LEFT)

root.mainloop()
