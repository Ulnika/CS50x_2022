import sys

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line argument")
elif sys.argv[1].find(".py") == -1:
    sys.exit("Not a Python file")

try:
    n = 0
    with open(sys.argv[1]) as file:
        for line in file:
            if not (line.strip().startswith("#") or line.strip() == ""):
                n += 1
    print(n)

except FileNotFoundError:
    sys.exit("File does not exist")