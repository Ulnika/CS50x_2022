import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
    except ValueError:
        continue

    number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue

        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        elif guess == number:
            print("Just right!")
            break
    break