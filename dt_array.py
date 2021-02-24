import numpy as np
import csv

with open('AAPL-2017.csv') as file:
    reader = csv.DictReader(file)
    stocks = np.empty((0, 6))
    for row in reader:
        aRow = np.array([[row['Open'], row['High'], row['Low'],
                          row['Close'], row['Adj Close'], row['Volume']]])
        stocks = np.append(stocks, aRow, axis=0)

    print(stocks.shape)