import pandas as pd
df_raw = pd.read_csv('all_stocks_data.csv')
df = df_raw.copy()

df = df.groupby("index")
print(df.head(5))
