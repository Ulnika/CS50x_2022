import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if '.' in ip:
        ip_list = ip.split('.')

        if not len(ip_list) == 4: return False
        
        for number in ip_list:
            # print(number)
            if (re.search("^[0-9]$|^1?[0-9][0-9]$|^2[0-4][0-9]$|^[0-2][0-5][0-5]$", number)):
                continue
            else:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
