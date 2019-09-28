import matplotlib as plt
from datetime import datetime
import csv

# Creates a path to the filename
filename = 'data/'

# Opens the csv file with a reader object. Each column is found in header_row
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, lows, dates = [], [], []
    # Iterates through each row and takes the data necessary from each row corresponding with each column
    for row in reader:
        high = int(row[5])
        low = int(row[6])
        date = datetime.strptime(row[2], '%Y-%m-%d')

        highs.append(high)
        lows.append(low)
        dates.append(date)

fig, ax = plt.subplots()
plt.style.use('seaborn')

# Plots the data
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.plt.fill(dates, highs, lows, facecolor='blue', alpha=0.1)

# Labels the data
plt.xlabel('', fontsize=14)
fig.autofmt_xdata()
plt.title("Selden, NY Highs and Lows - 2018", fontsize=24)
plt.ylabel("Temperature (F)", fontsize=14)

# Shows the plot
plt.show()
