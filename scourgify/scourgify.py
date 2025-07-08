import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

try:

    after = []

    with open(sys.argv[1], newline='') as csvfile:

        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["name"].split(",")
            house = row["house"]
            last = name[0]
            first = name[1].strip()
            after.append({"first": first, "last": last, "house": house})

    with open(sys.argv[2], "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in after:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")