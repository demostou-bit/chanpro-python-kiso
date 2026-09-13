import tkinter as tk
import os.path
import random

# Uranaiクラスの定義
class Uranai(tk.Frame):
  # 初期化メソッド__init__ 親フレームをmasterという引数で受け取る
  def __init__(self, master):
    # スーパークラスであるFrameクラスの初期化メソッドを呼び出す
    super().__init__(master, padx=10, pady=10)
    self.pack()
    # ボタンを配置するフレーム
    self.btn_frame = tk.Frame(self, padx=10, pady=20)
    self.btn_frame.pack()
    # 占うボタン
    self.uranau_btn = tk.Button(self.btn_frame, text="占う", command=self.uranau)
    self.uranau_btn.pack(side='left')
    # クリアボタン
    self.clear_btn = tk.Button(self.btn_frame, text="クリア", command=self.clear)
    self.clear_btn.pack(side='left')

    # デフォルトのイメージを読み込み（ディレクトリの相違を吸収）
    self.default_img = tk.PhotoImage(
      file=os.path.join(os.path.dirname(__file__), "kujis/empty.png")
    )
    # くじの4つのイメージファイル
    self.kujis = [tk.PhotoImage(file=os.path.join(
      os.path.dirname(__file__), "kujis/kyo.png")),
      tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "kujis/syoukiti.png")),
      tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "kujis/chukiti.png")),
      tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "kujis/daikiti.png"))]
    
    # 占い結果を表示するラベル
    self.show_kuji = tk.Label(self, image=self.default_img)
    self.show_kuji.pack()

  # uranauメソッド、自分自身を示すselfを引数に
  def uranau(self):
    # 占いを実行する
    self.show_kuji["image"] = random.choice(self.kujis)
  
  # clearメソッド、自分自身を示すselfを引数に
  def clear(self):
    # 占いをクリアする
    self.show_kuji["image"] = self.default_img

if __name__ == '__main__':
  # メインウィンドウを生成してrootに代入
  root = tk.Tk()
  # タイトル
  root.title("おみくじ")
  #rootを引数に、Uranaiコンストラクタを呼び出す
  app = Uranai(root)
  # メインループ
  root.mainloop()
