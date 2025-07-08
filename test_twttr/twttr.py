def main():
    word = input("Input: ")
    print(shorten(word))


def shorten(word):
    letters = ["a", "e", "i", "o", "u"]
    output = ""

    for letter in word:
        if letter.lower() not in letters:
            output = output + letter
    return output


if __name__ == "__main__":
    main()