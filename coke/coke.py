due = 50
change = 0
insert = 0

while due > 0:
    print("Amount due: ", due)
    insert = int(input("Insert coin: "))

    if insert == 25 or insert == 10 or insert == 5:
        due = due - insert

if due <= 0:
    print("Change owed: ", abs(due))