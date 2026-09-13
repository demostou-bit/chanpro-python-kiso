# ラベルテキストのフォント設定
import tkinter as tk

root = tk.Tk()

root.title("初めてのtkinter")

root.geometry("300x300")

# ラベルの配置
label1 = tk.Label(root, text="ラベル1", bg="yellow", font=("Courier", 35))
label1.pack()
label2 = tk.Label(root, text="ラベル2", bg="orange", font=("Times", 35))
label2.pack()
label3 = tk.Label(root, text="ラベル3", bg="pink", font=("", 30, "bold", "overstrike"))
label3.pack()
label4 = tk.Label(root, text="ラベル4", bg="pink", font=("", 40, "normal", "italic", "underline"))
label4.pack()

root.mainloop()
