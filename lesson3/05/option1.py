# OptionMenuウィジットの作成
import tkinter as tk

# メインウィンドウ
root = tk.Tk()
root.geometry("300x200")
# タイトル
root.title("OptionMenuのテスト")

def change(value):
  #ラベルにvalueの値を表示
  label["text"] = value

nums = tk.IntVar()
items = (1, 2, 3, 4, 5, 6, 7, 8)
# OptionMenuを生成
option_menu = tk.OptionMenu(root, nums, *items, command=change)
option_menu.pack()
# OptionMenuで2を選択状態に
nums.set(2)

label = tk.Label(root, text=nums.get(), font=("", 20), width=15)
label.pack()

# メインループ
root.mainloop()
