import tkinter as tk

# メインウィンドウ
root = tk.Tk()
# タイトル
root.title("チェックボックス")
# ウィンドウサイズ
root.geometry("200x100")

def get_chk(): # get_chk関数の定義
  # bool_varのgetメソッドでチェックボックスの状態を取得し
  # str関数で文字列に変換しラベルに表示
  label["text"] = str(bool_var.get())

# BooleanVarクラスのウィジット変数を生成し、変数bool_varに代入
bool_var = tk.BooleanVar()
# 初期状態でオフ
bool_var.set(False)

# Checkbuttonコンストラクタのvariableオプションを変数bool_varに関連付けて
# チェックボックスを生成する
chkbox = tk.Checkbutton(root, variable=bool_var, text="チェックボックス", command=get_chk)
chkbox.pack()

# ラベル
label = tk.Label(root, text="False")
label.pack(side=tk.LEFT)
root.mainloop()

