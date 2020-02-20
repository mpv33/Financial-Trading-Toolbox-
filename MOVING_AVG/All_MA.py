import pandas as pd
import numpy as np

df=pd.read_csv('ACC_Historicaldata-1M.csv', index_col='DATE')
#print(df)
close = df['CLOSE']

# convert index str to datetime of pandas
close.index = pd.to_datetime(close.index)

# calculate SMA for N window like here : 5
df['SMA_5'] = close.rolling(window=5).mean()
#print(df)
#print(df['SMA_5'].iloc[3:16])      #specific row and col accessing

# calculating 5 day WMA like
weight = np.arange(1,6)
df['WMA_5'] = close.rolling(5).apply(lambda price: np.dot(weight, price)/weight.sum(), raw = True)

# calculating 5 day EMA like:
#df['EMA_5'] = close.ewm( span=5).mean()
print(df)
df.to_csv('MOVING_AVG _OUTPUT.csv')
