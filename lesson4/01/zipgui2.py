# 郵便番号検索をGUI化する
import requests #1 requestsモジュールをインポート
import tkinter as tk

class ZipSearch(tk.Frame):
    #2 郵便番号APIのエンドポイントを変数にzipapiに代入
    zipapi = "https://zipcloud.ibsnet.co.jp/api/search"

    def __init__(self, master=None):
        super().__init__(master, bg="lightblue", padx=20, pady=20)
        self.pack(fill=tk.BOTH)

        # 検索用フレーム
        self.search_frame = tk.Frame(self, pady=10, padx=5)
        self.search_frame.pack()

        # 入力テキスト（郵便番号）用変数
        self.zip_entry_var = tk.StringVar()
        # 数字以外は入力できないようにする
        val_cmd = master.register(self.validate_digit) #1検証用のメソッドをval_cmdとして登録

        #2 入力テキスト用Entryコンストラクタでは、validateオプションを"key"に設定し、
        #2 キーが押されるたびにvalidate_digitメソッドを呼び出す
        self.zip_entry = tk.Entry(self.search_frame,
                                validate="key",
                                #3 validatecommandオプションにパラメータとして"%P"と"%S"を設定し
                                #3 文字列全体と、挿入された文字の両方をvalidate_digitメソッドに渡す
                                validatecommand=(val_cmd, "%S","%P"),
                                textvariable=self.zip_entry_var)
        self.zip_entry.pack(side='left')

        # 検索ボタン
        self.search_button = tk.Button(self.search_frame,
                                        text="検索",
                                        command=self.search)
        #4 検索ボタンを初期状態で無効にしている
        self.search_button.pack(side='left')
        self.search_button["state"] = "disabled"

        # 結果表示用のラベル
        self.result_label = tk.Label(self, bg="lightblue", font=("", 10))
        self.result_label.pack(fill=tk.X)

    # searchメソッドの定義
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

    #5 検証用のvalidate_digitメソッドの定義。引数charにタイプした1文字が、引数
    #5 entry_strに文字列全体が渡される
    def validate_digit(self, char, entry_str):
        #6 外側のif文では、タイプした文字が数字かどうかをisdigitメソッドで調べる
        if char.isdigit():
            #7 内側のif文では、文字列の長さが7文字であるかどうかを調べる
            #7 ちょうど7文字であれば検索ボタンを有効にする
            if len(entry_str) == 7:
                self.search_button["state"] = "normal"
            #7 7文字でなければ無効にする
            else:
                self.search_button["state"] = "disabled"
            return True
        else:
            #8 数字でなければFalseを戻して入力を無効にする
            return False

if __name__ == '__main__':
    root = tk.Tk()
    root.title("郵便番号検索API")
    root.geometry("480x150")
    root["bg"] = "lightblue"
    app = ZipSearch(master=root)
    root.mainloop()
