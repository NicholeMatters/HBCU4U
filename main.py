import csv

with open('schools.csv','r') as csvfile:
    reader= csv.reader(csvfile)
    for row in reader:
        print(row)
