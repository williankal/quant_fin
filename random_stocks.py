import pandas as pd
import random
import os

sp500_raw = pd.read_csv('archive/sp500_companies.csv')
sp500 = sp500_raw.copy()

random_stocks = random.sample(list(sp500['Symbol']), 30)

print(random_stocks)
print(len(random_stocks))

random_stocks_df = pd.DataFrame(random_stocks)
directory = 'infos_30'
file_path = os.path.join(directory, 'random_30_stocks.csv')

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)
    
random_stocks_df.to_csv('infos_30/random_30_stocks.csv', index=False)