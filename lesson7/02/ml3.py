import pandas as pd
# matplotlibのpyplotモジュールをpltの名前でインポート
import matplotlib.pyplot as plt
df = pd.read_csv("data/juyo-2022.csv", 
    encoding="shift_jis",
    skiprows=3, parse_dates=[0], names=["date", "kw"], 
    usecols=[0, 2])

df_juyo = df.groupby("date").sum()
# plot関数にDataFrameを渡すとグラフが描画される
plt.plot(df_juyo)
# 実際にグラフが見えるようにする
plt.show()
