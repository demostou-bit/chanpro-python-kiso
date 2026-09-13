import pandas as pd
import matplotlib.pyplot as plt

# 電力需要のCSV読込み
df = pd.read_csv("data/juyo-2022.csv", 
    encoding="shift_jis",
    skiprows=3, parse_dates=[0], names=["date", "kw"], 
    usecols=[0, 2])
df_juyo = df.groupby("date").sum()

# 気温のCSV読込み
df_ondo = pd.read_csv("data/ondo-2022.csv", 
    skiprows=5, parse_dates=[0], usecols=[0,1], 
    encoding="Shift_JIS", names=["date", "ondo"],
    index_col=0)

# 散布図の描画
plt.scatter(df_ondo["ondo"], df_juyo["kw"])
plt.xlabel("temp") # x軸のラベルを描画
plt.ylabel("kw") # y軸のラベルを描画
# 実際にグラフを表示
plt.show()

