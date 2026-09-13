import requests

#1 YouTube Data APIのベースURLを変数に代入
youtube_api = "https://www.googleapis.com/youtube/v3/search"
#2 APIキーを変数に代入（自身で取得したAPIキーを貼り付ける）
apikey = "xxxxxxxxxxxx APIキー xxxxxxxxxxxxxx"
#3 キーワードとして富士山を代入
keyword = "富士山"
#4 クエリパラメータを変数にセット
params = {"part": "snippet", "q": keyword, "type": "video",
            "maxResults": "5", "key": apikey}

#5 getメソッドを実行してJSONデータを取得し変数に格納
results = requests.get(youtube_api, params=params).json()

#6 変数resultsの内容を表示
for item in results["items"]:
	if "videoId" in item["id"]:
		print("■ id: ", item["id"]["videoId"])
		print("title:", item["snippet"]["title"])
		print("desc:", item["snippet"]["description"])
		print("thumbnail:",item["snippet"]["thumbnails"]["default"]["url"])
