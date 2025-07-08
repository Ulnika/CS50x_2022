import random

def main():
    level = get_level()

    k = 0
    while k < 10:

        X = generate_integer(level)
        Y = generate_integer(level)
        n = 0
        while n < 3:
            try:
                sum = int(input(f"{X} + {Y} = "))
                if sum == X + Y:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("EEE")
                n += 1
                continue

        if n == 3:
            print(f"{X} + {Y} = {X + Y}")
        k+=1



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if not (level == 1 or level == 2 or level == 3):
                continue
            return level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
    elif level == 2 or level == 3:
        n = random.randint(10**(level-1), 10**level-1)
    return n

if __name__ == "__main__":
    main()