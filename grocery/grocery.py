dict = {}
try:
    list = []

    while True:
        list.append(input())
        list.sort()

except EOFError:
    for item in list:
        dict[item] = dict.get(item, 0) + 1

for item in dict:
    print(f"{dict[item]} {item}".upper())