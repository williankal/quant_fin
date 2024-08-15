import pandas as pd

stocks = pd.read_csv('../data/companies.csv')
tickers = stocks['Symbol'].tolist()

cleaned_data_list = []

for ticker in tickers:

    print(f'Cleaning data for {ticker}')
    
    # Load the CSV file with proper handling for headers
    data = pd.read_csv(f'../data/raw/{ticker}_data.csv', header=[0, 1], index_col=0, parse_dates=True).copy()

    # Identify and drop any extra header rows or misaligned data
    # Assuming the extra header row is in index 0
    data.columns = data.columns.get_level_values(1)
    data.index.name = 'Date'

    # Reset the index to get 'Date' as a column if it is not correctly set
    data.reset_index(inplace=True)
    data.set_index('Date', inplace=True)

    # Rename columns if necessary and add Ticker column
    data.rename(columns={
        f'{ticker} US Equity.1': 'PX_LAST',
        f'{ticker} US Equity.3': 'PX_HIGH',
        f'{ticker} US Equity.2': 'PX_OPEN',
        f'{ticker} US Equity.4': 'PX_LOW',
        f'{ticker} US Equity.5': 'PX_VOLUME',
        f'{ticker} US Equity': 'CUR_MKT_CAP'
    }, inplace=True)

    # Add Ticker column
    data['Ticker'] = f'{ticker}'

    # Print the cleaned DataFrame
    cleaned_data_list.append(data)

    # Save the cleaned DataFrame to a new CSV file
    data.to_csv(f'../{ticker}_data.csv')

# Conslidate the data in one
consolidated_data = pd.concat(cleaned_data_list)

# Save the consolidated DataFrame to a CSV file
consolidated_data.to_csv('../consolidated_data.csv')

print('Consolidation complete. All data saved to consolidated_data.csv.')