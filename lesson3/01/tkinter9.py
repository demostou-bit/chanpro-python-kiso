# フレームを2つ用意し、それぞれのフレームにラベルを2つ横並びで配置
import tkinter as tk

root = tk.Tk()

root.title("初めてのtkinter")

root.geometry("300x200")

# 最初のフレーム
frame1 = tk.Frame(root, bg="gray", padx=10, pady=20)
frame1.pack()

# 1つ目のラベルの配置
label1 = tk.Label(frame1, text="ラベル1", bg="yellow")
label1.pack(side=tk.LEFT)
label2 = tk.Label(frame1, text="ラベル2", bg="orange")
label2.pack(side=tk.LEFT)

# 2番目のフレーム
frame2 = tk.Frame(root, bg="lightblue", padx=10, pady=20)
frame2.pack()

# 2つ目のラベルの配置
label3 = tk.Label(frame2, text="ラベル3", bg="pink")
label3.pack(side=tk.LEFT)
label4 = tk.Label(frame2, text="ラベル4", bg="darkgray")
label4.pack(side=tk.LEFT)

root.mainloop()
