import pandas as pd

sp500_raw = pd.read_csv('infos_30/random_30_stocks.csv')
sp500Random= sp500_raw.copy()

base = pd.read_csv('archive/sp500_companies.csv')

sp500Random = sp500Random.merge(base, on='Symbol', how='left')
sp500Random.to_csv('sp500_ciompanies_selected.csv', index=False)