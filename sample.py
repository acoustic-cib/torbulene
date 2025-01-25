from pybroker import YFinance

yfinance = YFinance()
df = yfinance.query(['BTC-USD', 'USDAUD'], start_date='11/1/2024', end_date='25/1/2025')
print(df)