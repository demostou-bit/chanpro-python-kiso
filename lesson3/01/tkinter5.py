# 3つのラベルを下寄せ、上寄せで配置する
import tkinter as tk

root = tk.Tk()

root.title("初めてのtkinter")

root.geometry("400x200")

# ラベルの配置
label1 = tk.Label(root, text="ラベル1", bg="yellow")
label1.pack(side=tk.LEFT, anchor=tk.S) # 下寄せ
label2 = tk.Label(root, text="ラベル2", bg="orange")
label2.pack(side=tk.LEFT, anchor=tk.N) # 上寄せ
label3 = tk.Label(root, text="ラベル3", bg="pink")
label3.pack(side=tk.LEFT, anchor=tk.S) # 下寄せ

root.mainloop()
