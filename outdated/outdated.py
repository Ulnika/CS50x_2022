months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        inp = input("Date: ")
        if inp.find('/') != -1:
            date = inp.split('/')

            if len(date) == 3 and int(date[0]) <= 12 and int(date[1]) <= 31:
                print(f"{date[2]}-{int(date[0]):02}-{int(date[1]):02}")
                break

        elif inp.find(',') != -1:
            date = inp.split(',')
            month_day = date[0]
            month_day = month_day.split(" ")
            month = month_day[0]
            if int(month_day[1]) <= 31:
                if month in months:
                    m = months.index(month)+1
                    print(f"{date[1].strip()}-{int(m):02}-{int(month_day[1]):02}")
                    break

    except (IndexError, ValueError):
        pass