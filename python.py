import pandas as pd
from xbbg import blp

DATA_DIR = 'random_stocks.csv'

# Load the tickers from the CSV file
stocks = pd.read_csv(DATA_DIR)
ticker = stocks['Symbol'].tolist()

# Define the fields you want to retrieve
fields = ['PX_LAST', 'PX_OPEN', 'PX_HIGH', 'PX_LOW', 'PX_VOLUME', 'CUR_MKT_CAP']
start_date = '2014-01-01'
end_date = '2024-12-31'

# Retrieve data for each ticker and save it to a CSV file
for i in ticker:
    hist = blp.bdh(f"{i} US Equity", fields, start_date, end_date)
    filename = f'{i}_data.csv'  # Save each ticker's data in a separate CSV file
    hist.to_csv(filename)