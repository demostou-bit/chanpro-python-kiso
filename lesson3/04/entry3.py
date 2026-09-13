# 4文字以上入力したらボタンを有効にする
import tkinter as tk

# メインウインドウ
root = tk.Tk()
# タイトル
root.title("Entryの検証1")
# ウィンドウサイズ
root.geometry("400x100")

# 検証用の関数
def validate_entry(strings):
  # 入力した文字列が4文字未満
  if len(strings) < 4:
    add_button["state"] = "disabled"
  # 入力した文字列が4文字以上
  else:
    add_button["state"] = "normal"
  # 入力はすべて受け入れるため、常にTrueを返す
  return True

# StringVarオブジェクトを生成
strVar = tk.StringVar()

# 検証用の関数を登録
val_cmd = root.register(validate_entry)

# Entryコンストラクタのvalidatecommandオプションでは、パラメータに
# "%P"を指定して、入力されている文字列を検証用の関数に渡しています。
entry = tk.Entry(root, width=20, textvariable=strVar,
                 validatecommand=(val_cmd, "%P"),
                 validate="key")
entry.pack()

# ボタンが押されたときに呼び出すprint関数に引数を渡す場合、
# ラムダ式で指定する必要があります。
add_button = tk.Button(root, text="追加", command=lambda:print(strVar.get()))
add_button.pack()
add_button["state"] = "disabled"

#以下のようにprint関数を直接渡すことはできません。
# add_button = tk.Button(root, text="追加", command=print(strVar.get()))

# メインループ
root.mainloop()
