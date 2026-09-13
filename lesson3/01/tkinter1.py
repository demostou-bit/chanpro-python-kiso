# ウィンドウに3つのラベルを表示

#1 tkinterモジュールをtkとしてインポートすることでtkinterモジュールに「tk」としてアクセスできる
import tkinter as tk 

#2 Tkクラスのコンストラクタを実行してメインウィンドウを生成
root = tk.Tk()

#3 titleメソッドはウィンドウのタイトルバーに表示するタイトルを設定
root.title("初めてのtkinter")

#4 geometryメソッドでウィンドウのサイズを「横×縦」で設定
root.geometry("400x100")

# メインウィンドウ(root)にラベルを配置

#5 第1引数に親のウィジェット、第2引数に表示するテキストを設定
#5 bgオプションで背景色（黄色）を設定、fgオプションで文字色（緑）を設定
label1 = tk.Label(root, text="Pythonの世界へようこそ", bg="yellow", fg="green")
label1.pack()

#6 #5と同様に設定、bgオプションで背景色（オレンジ）に設定
label2 = tk.Label(root, text="Pythonはオブジェクト指向", bg="orange")
label2.pack()

#7 #5と同様に設定、bgオプションで背景色（ピンク）を設定
label3 = tk.Label(root, text="tkinterでGUIアプリ", bg="pink")
label3.pack()

#8 mainloopメソッドでイベントループを開始してイベント待ちの状態にする
root.mainloop()
