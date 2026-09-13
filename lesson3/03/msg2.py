import tkinter as tk
import tkinter.messagebox

# メインウィンドウ
root =tk.Tk()
# タイトル
root.title("初めてのtkinter")
# ウィンドウサイズ
root.geometry("400x100")

# はい、いいえの質問を表示する
yesno = tk.messagebox.askyesno("メッセージ", "ボタンがクリックされました")
print(yesno)

# メインループ
root.mainloop()
