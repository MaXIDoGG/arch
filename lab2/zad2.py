import csv
import numpy as np
arr = []
with open('table.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar=' ')
    for row in reader:
        b = []
        for i in row:
            b.append(float(i))
        arr.append(b)

inverseArr = np.linalg.inv(arr)

print(inverseArr)


with open('table1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar=' ')
    for i in inverseArr:
        writer.writerow(i)
