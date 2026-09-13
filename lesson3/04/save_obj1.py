# オブジェクトをファイルに書き出す
import os.path
import pickle # pickleモジュールをインポート

# リストweekdaysを生成し、曜日を要素としている
weekdays = ['月', '火', '水', '木', '金', '土', '日']

# days.pickleのパス変数file_pathに代入
filename = "days.pickle"
file_path = os.path.join(os.path.dirname(__file__) , filename)

# open関数でファイルオープンし、ファイルオブジェクトout_fileに代入
# 第2引数のwbは、バイナリモード(b)で書き出す(w)ことを示します。
out_file = open(file_path, "wb")

# dump関数でリストweekdaysをout_fileに書き出す
pickle.dump(weekdays, out_file)
