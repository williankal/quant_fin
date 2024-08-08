import pandas as pd
import random

sp500_raw = pd.read_csv('archive/sp500_companies.csv')
sp500= sp500_raw.copy()

random_stocks = random.sample(list(sp500['Symbol']), 30)

print(random_stocks)
print(len(random_stocks))

random_stocks_df = pd.DataFrame(random_stocks)
random_stocks_df.to_csv('random_stocks.csv', index=False)