# 数字以外の入力は許可しない
import tkinter as tk

# メインウインドウ
root = tk.Tk()
# タイトル
root.title("Entryの検証1")
# ウィンドウサイズ
root.geometry("400x100")

# 検証用の関数を定義。引数にユーザーが入力した文字を受け取る
def validate_entry(chr):
  if chr.isdigit():
    # 入力した文字が数字であればTrueを戻して入力を受け取る
    return True
  else:
    # 数字でなければFalseを戻して破棄する
    return False

# StringVarオブジェクトを生成
strVar = tk.StringVar()

# 定義した検証用の関数を登録し、val_cmdに代入
val_cmd = root.register(validate_entry)

# Entryウィジット。validatecommandオプションではタプルの2番目の値に
# パラメータに"%S"を指定し、ユーザー入力した1文字を検証用の関数に渡す
# ようにしています。
entry = tk.Entry(root, width=20, textvariable=strVar,
                 validatecommand=(val_cmd, "%S"),
                 validate="key")
entry.pack()

# メインループ
root.mainloop()