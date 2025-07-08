def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        #print('not enought characters')
        return False
    if not s[0:2].isalpha():
        #print('first two are not letters')
        return False

    for i in range(len(s)):
        if not s[i].isalpha():
            if not s[i].isnumeric():
                #print('not characters')
                return False

    for i in range(len(s)):
        if (s[i] == "0" and s[i-1].isalpha()):
            #print('0 is first number')
            return False

    for i in range(len(s)):
        if s[i:len(s)].isalpha():
            #print('all letters')
            return True

        if s[i].isdigit():
            if s[i:len(s)].isnumeric():
                return True
            else:
                return False


main()