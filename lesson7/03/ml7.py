import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
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
quadratic = PolynomialFeatures(degree=2)
X_quad = quadratic.fit_transform(X)
model = LinearRegression()
model.fit(X_quad, y)

# ユーザーの入力した気温から消費電力を予測
while True:
	t = input("温度を入力してください [改行の入力で終了] ") # 入力を受け取る
	if t == "":
		break
	t = float(t) # 数値に変換
	x = quadratic.fit_transform([[t]]) # 多項式に変換
	v = model.predict(x) # 値を予測する
	print(f"予想使用電力は{v}です") # 予想値を出力
