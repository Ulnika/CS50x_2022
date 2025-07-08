def main():
    fraction = input('Fraction: ')
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    fraction = fraction.split("/")

    X = int(fraction[0])
    Y = int(fraction[1])

    if X <= Y and Y != 0:
        return round(int((X / Y)*100))
    elif Y == 0:
        raise ZeroDivisionError()
    elif X > Y:
        raise ValueError()

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (f"{percentage}%")


if __name__ == "__main__":
    main()