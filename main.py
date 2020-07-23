import csv


# print('Schools sorted by URL:\n')
# with open('hbcu.csv', newline='') as csvfile:
# 	schools = csv.reader(csvfile, delimiter=',')
# 	# sortedSchools = sorted(books, key=operator.itemgetter(1), reverse=True)
# 	# for title, year, author in sortedBooks:
# print(schools)

with open('schools.csv','r') as csvfile:
    reader= csv.reader(csvfile)
    for row in reader:
        print(row)
