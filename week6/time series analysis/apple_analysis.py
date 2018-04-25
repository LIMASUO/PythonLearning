# -*- coding:utf-8 -*-

import pandas as pd

def quarter_volume():
    data = pd.read_csv('apple.csv', header=0)
    ds = pd.Series(list(data['Volume']), index=pd.to_datetime(list(data['Date'])))
    dsr = ds.resample('Q').sum()
    dsrr = dsr.sort_values(ascending=False)
    print(dsr[0:-1])
    print(dsrr[0:-1])
    second_volume = dsrr[1]
   
    return second_volume

if __name__ == '__main__':
    quarter_volume()
