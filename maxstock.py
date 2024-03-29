import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import yfinance as yf
from lists import *

prices = []
initial_buyin = 1000
x = 0
y = 0
z = 0
t = 0

def maxProfit (prices):
    sell1 = 0
    sell2 = 0
    buy1 = float ('inf')
    buy2 = float ('inf')
    global x,y,z,t
    x = 0
    y = 0
    z = 0
    t = 0
    for p in prices:
        buy1 = min(buy1, p)
        sell1 = max(sell1, p-buy1)
        buy2 = min(buy2, p- sell1)
        sell2 = max(sell2,p-buy2)
    try:
        x = int(initial_buyin/buy1)
        y = (buy1+sell1)*x
        z= int(y/(sell1+buy2))
        t= z*(sell2+buy2)
    except: pass
    return sell2

for name in fname:
    satas = yf.download (name, '2019-07-01', '2019-08-01')
    df = pd.DataFrame(satas)
    prices = df ['Close']
    solution = maxProfit(prices)
    print (name)
    file1 = open("myfile.txt","a")#append mode 
    file1.write(str(t)+'\n') 
    file1.close() 
    

