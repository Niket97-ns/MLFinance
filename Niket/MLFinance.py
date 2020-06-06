import os
import pandas as pd

def symbol_to_path(symbol, base_dir="data"):
	return os.path.join(base_dir,"{}.csv".format(str(symbol)))

def get_data(symbols, dates):
	df = pd.Dataframe(index=dates)
	if 'SPY' not in symbols:
		symbols.insert(0,'SPY')

	for symbol in symbols:
		df_tmp = pd.read_csv(symbol_to_path(symbol), index_col='Date', parse_dates=True, usecols=['Date','Adj Close'], na_values=['nan'])
		df_tmp = df_tmp.rename(columns = {'Adj Close':symbol})
		df = df.join(df_tmp)
		if symbol == 'SPY':
			df = df.dropna(subset=["SPY"])

	return df

tickers = ['AAPL','HCP']
startD = "2017-01-01" 
endD = "2017-09-28"
dates = pd.date_range(startD,endD)
d = get_data(tickers,dates)
print d