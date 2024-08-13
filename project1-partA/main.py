import pandas as pd

# Assume consolidated_data is already loaded and formatted correctly
consolidated_data = pd.read_csv('../data_bloomberg_clean/consolidated_data.csv').copy()
consolidated_data.set_index('Date', inplace=True)

#Calculate the market value for each asset
consolidated_data['Market_Value'] = consolidated_data['PX_LAST'] * consolidated_data['CUR_MKT_CAP']

# Group by date and calculate the total market value for each day
total_market_value = consolidated_data.groupby(consolidated_data.index)['Market_Value'].sum()
# Calculate weights for each asset
consolidated_data['Weight'] = consolidated_data.groupby(consolidated_data.index)['Market_Value'].transform(lambda x: x / total_market_value)

# # Calculate daily returns
# consolidated_data['Daily_Return'] = consolidated_data.groupby('Symbol')['PX_LAST'].pct_change()

# # Calculate portfolio returns
# portfolio_returns = (consolidated_data['Weight'] * consolidated_data['Daily_Return']).groupby(consolidated_data.index).sum()

# print(portfolio_returns)
#save the data to a new csv file
consolidated_data.to_csv('project1_data.csv')