input = input("Input: ")
output = ""

letters = ["a", "e", "i", "o", "u"]

for letter in input:
    if letter.lower() not in letters:
        output = output + letter

print("Output: ", output)