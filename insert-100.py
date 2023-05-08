# import libraries

import csv
from itertools import islice as slice
import sys

count = 1

# create an empty list
readings = []

mysql = "INSERT INTO `readings` values\n"

# open and read csv file
with open('clean.csv', 'r') as file:
    reader = slice(csv.DictReader(file, delimiter=','), 100)

    for row in reader:

        del row['Location']
        del row['geo_point_2d']

        readings = ["'" + str(x) + "'" for x in row.values()]
        readings = ",".join(readings)

        readings.replace("''", "NULL")
        readings.replace("'TRUE'", "TRUE")
        readings.replace("'FALSE'", "FALSE")

        mysql += str(count) + ',' + readings + '\n'
        count += 1


new_sql = mysql[:-1] + ';'
new_file = open("insert-100.sql", 'w')
new_file.write(new_sql + '\n')
print(new_sql)