# save_obj1.pyで書き出したファイルからデータを読み込む
import os.path
import pickle

weekdays = []
filename = "days.pickle"
file_path = os.path.join(os.path.dirname(__file__), filename)

# open関数を使用してファイルオープン。第2引数のrbは、バイナリモード
# (b)で読み込む(r)ことを表しています。
in_file = open(file_path, "rb")

days = pickle.load(in_file) # in_fileからデータを変数daysに読み込み
print(days) # 表示

