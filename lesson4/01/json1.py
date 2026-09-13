import os
# jsonモジュールをインポート
import json

dirname = os.path.dirname(__file__)
path = os.path.join(dirname, "customers.json")
# open関数で文字コードをUTF-8に設定してファイルを開く
in_file = open(path, "r", encoding="utf-8")

# jsonload関数でファイルを読み込み、Pythonオブジェクトに変換
json_obj = json.load(in_file)
# そのまま表示
print(json_obj)

# for文で読み込んだ顧客情報を1人ずつ表示
for customer in json_obj["customers"]:
    print(customer["name"], str(customer["age"]) + "歳",
       customer["gender"])
# プログラムを終了すると自動で閉じられるが、close関数を入れている
in_file.close()
