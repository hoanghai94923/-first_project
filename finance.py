import yfinance as yf
import numpy as np
import pandas as pd

tickers = ["EURVND=X", "EURAUD=X"]
df = yf.download(tickers, start='2018-01-01')
df.xs('EURVND=X', axis=1,level=1)
adj_close = df['Adj Close']
adj_close[adj_close['EURVND=X'] == max(adj_close['EURVND=X'])]
print(adj_close)
