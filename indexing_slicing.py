import numpy as np
import csv

with open('AAPL-2016.csv', 'r') as file:
    reader = csv.DictReader(file)
    stocks16 = np.empty((0, 6))
    for row in reader:
        aRow = np.array([[row['Open'], row['High'], row['Low'],
                          row['Close'], row['Adj Close'], row['Volume']]], dtype=float)
        stocks16 = np.append(stocks16, aRow, axis=0)
    # print(stocks16.sum(axis=0))

january = stocks16[:20]
np.set_printoptions(formatter={'float': '{: 6.2f}'.format})

january[0][5, ] = 100
# print(january)
# print(stocks16[19, 5])

# print(stocks16[0:5])
max16 = stocks16[:,3].max()
print(max16)

highLow = stocks16[:, [1, 2]]
print(highLow[0:5])