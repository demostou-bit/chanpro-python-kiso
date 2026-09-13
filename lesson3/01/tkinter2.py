# ラベルのテキストと背景色を設定
import tkinter as tk

root = tk.Tk()

root.title("初めてのtkinter")

root.geometry("400x100")

label1 = tk.Label(root, text="Pythonの世界へようこそ", bg="yellow")
label1.pack()

# ラベルのオプション変更
label1["text"] = "tkinterでGUIアプリ" # テキスト変更
label1["bg"] = "pink" # 背景色をピンクに変更

root.mainloop()
