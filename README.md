# Quantitative Finance

dataset: https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks?resource=download

## Project 1 - Part A
[X] Select 30 stocks in the S&P 500 universe
[X] Collect daily returns for the past 10 years (2014-2023)
[] Create both value-weighted and equally-weighted portfolio
[] Rebalance these portfolios in the first day of the month based on the information on the last day (1-day lag)
[] Which portfolio has the highest turnover?
[] Compute daily returns for both portfolios
[] Compute the following statistics for these portfolios: annualized average return, annualized standard deviation, Sharpe ratio, Information Ratio (vs. S&P 500)
[] Plot cumulative returns for both portfolios, S&P 500 and risk-free




## Setup

1. **Create an Archive Folder**:
   - Create a folder named `archive` to store the dataset.

2. **Script Descriptions**:
   - **`random_stocks.py`**: 
     - Randomly selects 30 stocks from the dataset for analysis.
   
   - **`sp500_get_infos.py`**: 
     - Retrieves information about the selected 30 companies, including their names and business summaries.
   
   - **`get_market_cap_bloomberg.py`**: 
     - Fetches the market capitalization of the 30 selected companies from Bloomberg.

## Instructions

1. Place the dataset in the `archive` folder.
2. Run `random_stocks.py` to select a random subset of 30 stocks.
3. Use `sp500_get_infos.py` to obtain detailed information about these stocks.
4. Execute `get_market_cap_bloomberg.py` to gather market capitalization data.