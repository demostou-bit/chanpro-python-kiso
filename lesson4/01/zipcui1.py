# コマンドラインで動作する郵便番号検索アプリ
import requests
zipapi = "https://zipcloud.ibsnet.co.jp/api/search"
zcode = input("郵便番号を入力してください")
params = {"zipcode": zcode}
r = requests.get(zipapi, params=params)
zip_json = r.json()

if zip_json["status"] != 200: #1 エラーがあるかどうかを調べる
    print(zip_json["message"]) #2 エラーがあればmessageの内容を表示
else:
    if zip_json["results"]: #3 エラーがない場合resultsに結果があるかどうかを調べる
        print(zip_json["results"][0]) #4 結果があれば表示
    else:
        print("見つかりません") #5 結果がない場合に表示
