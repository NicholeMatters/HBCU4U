import csv
from hbcu.models import College

with open('schools.csv','r') as csvfile:
    reader= csv.reader(csvfile)
    for row in reader:
       College.objects.create(name=row[1],city=row[2],state=row[3])
    
print("Done!")
