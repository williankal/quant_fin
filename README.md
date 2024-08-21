# Quantitative Finance

dataset: https://www.kaggle.com/datasets/andrewmvd/sp-500-stocks?resource=download

## Project 1 - Part A
- [X] Select 30 stocks in the S&P 500 universe
- [X] Collect daily returns for the past 10 years (2014-2023)
- [X] Create both value-weighted and equally-weighted portfolio
- [X] Rebalance these portfolios in the first day of the month based on the information on the last day (1-day lag)
- [ ] Which portfolio has the highest turnover?
- [X] Compute daily returns for both portfolios
- [ ] Compute the following statistics for these portfolios: annualized average return, annualized standard deviation, Sharpe ratio, Information Ratio (vs. S&P 500)
- [ ] Plot cumulative returns for both portfolios, S&P 500 and risk-free

## Project 1 - Part B
- [ ] (a) Choose n stocks at random.
- [ ] (b) Compute ex post returns on an equal-weighted portfolio (Wi = 1/n) over some historical period.
- [ ] (c) Compute the variance of return from the data.
- [ ] (d) Repeat (a) – (c), say, 10 times.
- [ ] (e) Repeat (a) – (d) for n = 1,2,3….

## Project 1 - Part C
- [ ] Find the optimum portfolio of these risky assets assuming that risk premium for each asset is given by past 10-year excess return. Make a reasonable assumption for the risk-free rate.
- [ ] Find the Minimum Variance Portfolio.
- [ ] Draw the mean-variance frontier.
- [ ] Draw the mean-variance frontier, but now play with two assets only and analyze the effect of varying correlation from -1 to 1.

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
