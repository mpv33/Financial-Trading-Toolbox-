import pandas as pd
import numpy as np


df = pd.read_csv('ACC_Historicaldata-1M.csv')
df1 = df[['CLOSE']]

n = 14

def rma(x, n, y0):
    a = (n-1) / n
    ak = a**np.arange(len(x)-1, -1, -1)
    return np.append(y0, np.cumsum(ak * x) / ak / n + y0 * a**np.arange(1, len(x)+1))

df['CHANGE'] = df1.diff()
df['GAIN'] = df.CHANGE.mask(df.CHANGE < 0, 0.0)
df['LOSS'] = -df.CHANGE.mask(df.CHANGE > 0, -0.0)
df.loc[n:, 'AVG_GAIN'] = rma( df.GAIN[n+1:].values, n, df.loc[:n, 'GAIN'].mean())
df.loc[n:, 'AVG_LOSS'] = rma( df.LOSS[n+1:].values, n, df.loc[:n, 'LOSS'].mean())
df['RS'] = df.AVG_GAIN / df.AVG_LOSS
df['RSI_14'] = 100 - (100 / (1 + df.RS))
df.to_csv('RSI_output.csv',index=False)
