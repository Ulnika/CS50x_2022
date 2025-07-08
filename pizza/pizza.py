import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line argument")
elif sys.argv[1].find(".csv") == -1:
    sys.exit("Not a CSV file")

try:
    pizza = []

    with open(sys.argv[1], newline='') as csvfile:
        headers = csvfile.readline().strip().split(",")
        csvfile.seek(0)

        reader = csv.DictReader(csvfile)

        for row in reader:

            pizza.append({headers[0]: row[headers[0]], headers[1]: row[headers[1]],
            headers[2]: row[headers[2]]})

    print(tabulate(pizza, "keys", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")