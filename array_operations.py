import numpy as np
import csv

with open('AAPL-2016.csv', 'r') as file:
    reader = csv.DictReader(file)
    stocks16 = np.empty((0, 6))
    for row in reader:
        aRow = np.array([[row['Open'], row['High'], row['Low'],
                          row['Close'], row['Adj Close'], row['Volume']]], dtype=float)
        stocks16 = np.append(stocks16, aRow, axis=0)
    print("axis 0", stocks16.sum(axis=1))
    totalVol16 = stocks16[:, 5].sum()

with open('AAPL-2017.csv') as file:
    reader = csv.DictReader(file)
    stocks17 = np.empty((0, 6))
    for row in reader:
        aRow = np.array([[row['Open'], row['High'], row['Low'],
                          row['Close'], row['Adj Close'], row['Volume']]], dtype=float)
        stocks17 = np.append(stocks17, aRow, axis=0)

    totalVol17 = stocks17[:, 5].sum()

    # print(stocks17.sum(axis=1))

print("Difference between 2017 & 2016: ", totalVol17, totalVol16, totalVol16 - totalVol17)

change = np.empty((250, 6))
np.subtract(stocks16, stocks17, out=change)
np.set_printoptions(formatter={'float': '{: 6.2f}'.format})

print("Change", change)

sumChange = change.sum(axis=1)
print("change sum column", sumChange, sumChange.shape)
totalVolChange = change[:, 5].sum()
print("Volume from change", totalVolChange)

combined_years = np.concatenate((stocks16, stocks17), axis=0)
print(combined_years)
save_file = open("combined_years.txt", 'w')
np.savetxt(save_file, combined_years, fmt='%10.2f', delimiter=',', newline='\n')
