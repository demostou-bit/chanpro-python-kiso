# Textウィジットの使用例
import tkinter as tk

# メインウィンドウ
root = tk.Tk()
# タイトル
root.title("Textウィジットのテスト")

#1 Textウィジットを幅45、高さ3で生成
text = tk.Text(
    root,
    width=45,
    height=3
)
text.pack()

#2 表示する文字列を変数linesに代入
lines = """こんにちはPythonの世界へようこそ
tkinterでGUIプログラミング
WebAPIを使用する"""
#3 insertメソッドで、Textウィジットの最初の位置に変数linesの内容を表示
text.insert("1.0",lines)

# メインループ
root.mainloop()
