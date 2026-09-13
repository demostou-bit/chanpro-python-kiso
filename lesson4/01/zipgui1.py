# 郵便番号検索をGUI化する
import requests #1 requestsモジュールをインポート
import tkinter as tk

class ZipSearch(tk.Frame):
    #2 郵便番号APIのエンドポイントを変数にzipapiに代入
    zipapi = "https://zipcloud.ibsnet.co.jp/api/search"

    #3 初期化メソッドで各ウィジットの初期化を行っている
    def __init__(self, master=None):
        super().__init__(master, bg="lightblue", padx=20, pady=20)
        self.pack(fill=tk.BOTH)

        # 検索用フレーム
        self.search_frame = tk.Frame(self, pady=10, padx=5)
        self.search_frame.pack()

        # 入力テキスト（郵便番号）用変数
        self.zip_entry_var = tk.StringVar() #4 ウィジット変数を用意

        # 入力テキスト用Entry
        self.zip_entry = tk.Entry(self.search_frame,
                              textvariable=self.zip_entry_var)
        self.zip_entry.pack(side='left')

        # 検索ボタン
        #5 commandオプションでクリックされたsearchメソッドを呼び出す
        self.search_button = tk.Button(self.search_frame,
                                       text="検索",
                                       command=self.search)
        self.search_button.pack(side='left')

        # 結果表示用のラベル
        self.result_label = tk.Label(self, bg="lightblue", font=("", 10))
        self.result_label.pack(fill=tk.X)

    #6 searchメソッドの定義
    def search(self):
        zipcode = self.zip_entry_var.get()

        # 郵便番号APIを呼び出してJSONデータを取得する
        params = {"zipcode": zipcode}
        #7 GETメソッドで郵便番号APIにリクエストを送り、受け取ったJSONデータ
        #  をPythonオブジェクトに変換し、変数resultに代入
        result = requests.get(ZipSearch.zipapi, params=params).json()

        #8 ステータスをチェックし、結果をラベルに表示
        if result["status"] != 200:
            self.result_label["text"] = result["message"]
        else:
           # 住所が見つかったかどうかをチェック
           if result["results"]:
               # 結果をラベルに表示
               self.result_label["text"] = result["results"][0]["address1"] + result["results"][0]["address2"] + result["results"][0]["address3"]
           else:
               self.result_label["text"] = "見つかりません"

if __name__ == '__main__':
    root = tk.Tk()
    root.title("郵便番号検索API")
    root.geometry("480x150")
    root["bg"] = "lightblue"
    app = ZipSearch(master=root)
    root.mainloop()


