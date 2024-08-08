import pandas as pd

selected_30_stocks = pd.read_csv('infos_30/30info_sp500_companies_selected.csv').copy()
sp500_stocks = pd.read_csv('archive/sp500_stocks.csv').copy()


selected_30_stock_prices = sp500_stocks[sp500_stocks['Symbol'].isin(selected_30_stocks["Symbol"])]
selected_30_stock_prices.to_csv('infos_30/sp500_selected_stocks.csv', index=False)