import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import yfinance as yf
from lists import *

prices = []
dates = []
initial_buyin = 1000
x = 0
y = 0
z = 0
t = 0

def get_data (filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))
    return

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
    print (buy1,sell1,buy2)
    return sell2


get_data('')
maxProfit(prices)
    

