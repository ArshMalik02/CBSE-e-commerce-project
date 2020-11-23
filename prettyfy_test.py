import csv
import prettyfy

new_file = prettyfy.pretty_file('db/stock/stockItems.csv', header=False, border=False, delimiter="|")
with open(new_file, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0])
