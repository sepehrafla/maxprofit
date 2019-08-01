import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import yfinance as yf
from lists import *

prices = []

def maxProfit (prices):
    sell1 = 0
    sell2 = 0
    buy1 = float ('inf')
    buy2 = float ('inf')
    for p in prices:
        buy1 = min(buy1, p)
        sell1 = max(sell1, p-buy1)
        buy2 = min(buy2, p- sell1)
        sell2 = max(sell2,p-buy2)
    return sell2

for name in fname:
    satas = yf.download (name, '2008-01-01', '2019-01-01')
    df = pd.DataFrame(satas)
    prices = df ['Close']
    solution = maxProfit(prices)
    print (name, solution)
    df= pd.DataFrame(solution)
    df.to_csv(index=False)

