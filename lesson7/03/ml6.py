import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures # scikit-learnで必要なモジュールをインポート
from sklearn.linear_model import LinearRegression

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

# 説明変数をXに代入
X = pd.DataFrame(df_ondo["ondo"])

# 目的変数をyに代入
y = df_juyo["kw"]

# モデルの作成と学習
quadratic = PolynomialFeatures(degree=2) # 多項式のオブジェクトを作成
X_quad = quadratic.fit_transform(X) # 説明変数を2次の多項式に変換
model = LinearRegression() # 線形回帰モデルを作成
model.fit(X_quad, y) # fitメソッドで学習

# 横軸用のデータを作成し、変数に代入
x_test = pd.DataFrame([x for x in range(-5, 40)], columns=["ondo"])

# モデルを使って予想
y_quad_fit = model.predict(quadratic.fit_transform(x_test))

# 機械学習で求めた曲線を描画
plt.plot(pd.DataFrame(x_test), y_quad_fit, color="red")

# 散布図を重ねて描画
plt.scatter(df_ondo["ondo"], df_juyo["kw"])
plt.show()