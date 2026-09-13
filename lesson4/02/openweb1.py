# WebページのリンクをWebブラウザで開く
import tkinter as tk
import webbrowser

# メインウィンドウ
root = tk.Tk()
root.geometry("200x100")
# タイトル
root.title("Webブラウザでリンクを開く")

url ="https://google.co.jp/"
#1 Buttonのコンストラクタのcommandオプションでクリックされたらopen関数を
#1 呼び出すようにしています。このとき、open関数に引数を渡しているためラム
#1 ダ式にする必要があります
button = tk.Button(root, text="オープンWeb", command=lambda: webbrowser.open(url))
button.pack()

# メインループ
root.mainloop()
