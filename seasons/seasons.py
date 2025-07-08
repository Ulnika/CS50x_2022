from datetime import date
from datetime import timedelta
import sys

import inflect

p = inflect.engine()

def main():
    date_inp = get_date(input("Date of Birth: "))
    print(transform_date(date_inp))


def get_date(date_inp):
    try:
        date_inp = date.fromisoformat(date_inp)
        return date_inp
    except:
        sys.exit("Invalid date")

def transform_date(date_inp):
    date_today = date.today()
    delta = date_today.__sub__(date_inp)
    words = p.number_to_words(delta.days * 24 * 60)
    return f"{words} minutes".replace(" and ", " ").capitalize()


if __name__ == "__main__":
    main()