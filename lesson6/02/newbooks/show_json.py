# JSONファイルの中身をフォーマットして表示
# JSONファイルは同じディレクトリに配置しておく
import json
import os

file = input("ファイルを指定してください：")
in_file_path = os.path.join(os.path.dirname(
    __file__), file)
in_file = open(in_file_path, "r", encoding="utf-8")	
books = json.load(in_file) # load関数を読み込む
# dump関数を使用して内容をjson_strに書き出す
# 日本語をエンコードなしで表示するためにensure_asciiオプションをFalse
# indentオプションでインデントの文字数を指定
json_str = json.dumps(books, ensure_ascii=False, indent=4)
print(json_str)
