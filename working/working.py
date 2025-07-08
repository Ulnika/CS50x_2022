import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    times = s.split(" to ")
    if len(times) != 2:
        raise ValueError

    working_hours = []

    for time in times:
        time = re.search("(?P<hours>[0-9][0-9]?):?(?P<minutes>([0-9][0-9])?) (?P<am_pm>(A|P)M)" , time)

        if not time:
            raise ValueError

        hours = int(time.group("hours"))
        if hours > 12:
            raise ValueError

        if (time.group("am_pm")) == "PM" and hours < 12:
            hours = hours + 12

        if (time.group("am_pm")) == "AM" and hours == 12:
            hours = 0

        if (time.group("minutes")):
            minutes = int(time.group("minutes"))
        else:
            minutes = 0

        if minutes >=60:
            raise ValueError

        time = (f"{hours:02}:{minutes:02}")
        working_hours.append(time)

    return (f"{working_hours[0]} to {working_hours[1]}")




if __name__ == "__main__":
    main()