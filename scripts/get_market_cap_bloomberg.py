import pandas as pd
from xbbg import blp

DATA_DIR = 'random_30_stocks.csv'

# Load the tickers from the CSV file
stocks = pd.read_csv(DATA_DIR)
tickers = stocks['Symbol'].tolist()

# Define the fields you want to retrieve
fields = ['PX_LAST', 'PX_OPEN', 'PX_HIGH', 'CUR_MKT_CAP', 'PX_VOLUME', 'PX_ADJ_LAST', 'SPX Index']
start_date = '2014-01-01'
end_date = '2023-12-31'

# Retrieve data for each ticker and save it to CSV files
for ticker in tickers:
    try:
        # Retrieve historical data
        hist = blp.bdh(f"{ticker} US Equity", fields, start_date, end_date)
        # Save to a CSV file
        filename = f'{ticker}_data.csv'
        hist.to_csv(filename)
        print(f"Data for {ticker} saved to {filename}.")
    except Exception as e:
        print(f"Failed to retrieve or save data for {ticker}: {e}")

# Optionally, consolidate all data into a single CSV file
consolidated_data = []
for ticker in tickers:
    try:
        # Read the saved CSV file for each ticker
        hist = pd.read_csv(f'{ticker}_data.csv', index_col=0, parse_dates=True)
        hist['Ticker'] = ticker  # Add ticker symbol to the DataFrame
        consolidated_data.append(hist)
    except Exception as e:
        print(f"Failed to read data for {ticker}: {e}")

if consolidated_data:
    # Combine all data into a single DataFrame
    all_data = pd.concat(consolidated_data)
    # Save the combined DataFrame to a CSV file
    all_data.to_csv('consolidated_data.csv')
    print("All data consolidated into 'consolidated_data.csv'.")
