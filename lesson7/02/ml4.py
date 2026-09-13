import pandas as pd
df_ondo = pd.read_csv("data/ondo-2022.csv", 
    skiprows=5, parse_dates=[0], usecols=[0,1], 
    encoding="Shift_JIS", names=["date", "ondo"],
    index_col=0)
print(df_ondo.head())

