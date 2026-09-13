# ライブラリの読み込み
import pandas as pd
# CSVファイルを読み込む
df = pd.read_csv("data/juyo-2022.csv", 
    encoding="shift_jis",
    skiprows=3, parse_dates=[0], names=["date", "kw"], 
    usecols=[0, 2])
# データフレームの先頭を返す
print(df.head())
