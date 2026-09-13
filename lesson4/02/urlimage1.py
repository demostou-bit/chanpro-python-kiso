# インターネットからJPEGイメージを取得して表示
# 実行できない場合、「Ctrl」+「Shift」+「P」を押してインタープリターを選択
# anaconda3～を選択してから実行する
import tkinter as tk
from PIL import Image, ImageTk
import requests

# メインウィンドウ
root = tk.Tk()
# タイトル
root.title("インターネット上のイメージを取得")

URL ="https://o2-m.com/lake1.jpg"
#1 requestsモジュールのget関数を使用して、イメージのURLにアクセス
#1 contentプロパティにはバイナリデータが格納されるので、それを変数imgに代入
img = requests.get(URL).content

#2 ImageTk.PhotoImageコンストラクタを使用してtkinterのPhotoImageオブジェクトに
#2 変換します。このとき、キーワード引数dataには#1で取得したimgを指定します。
photo = ImageTk.PhotoImage(data=img)

#3 取得したイメージをラベルに表示
label = tk.Label(image=photo)
label.pack()

# メインループ
root.mainloop()

