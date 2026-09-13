import tkinter as tk
import tkinter.messagebox

# メインウィンドウ
root =tk.Tk()
# タイトル
root.title("初めてのtkinter")
# ウィンドウサイズ
root.geometry("400x100")

# エラーを表示する
tk.messagebox.showerror("エラー", "エラーが発生しました")

# メインループ
root.mainloop()
