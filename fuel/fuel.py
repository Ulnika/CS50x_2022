while True:
    try:
        fraction = input('Fraction: ').split("/")
        X = int(fraction[0])
        Y = int(fraction[1])
        if X <= Y:
            answer = int((X / Y)*100)
            if answer <= 1:
                print("E")
            elif answer >= 99:
                print("F")
            else:
                print(f"{answer}%")
            break
    except (ValueError, ZeroDivisionError):
        pass
