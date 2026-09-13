# リストの内報表記の書式
# [式 for 変数 in イテレート可能なオブジェクト]

# 内包表記を使ってリストを作成
word = "赤青黄白"
colors = [c + "色" for c in word] # 内包表記
print(colors)
