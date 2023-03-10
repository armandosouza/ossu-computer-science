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

def verify_date(m, d, y):
    if m.isalpha() and d.endswith(","):
        day_formatted = d.rstrip(",")
        if int(day_formatted) <= 31:
            month_formatted = months.index(m)
            date_month = f"{y}-{month_formatted + 1:02}-{int(day_formatted):02}"
            return date_month
    elif m.isnumeric() and (int(d) <= 31 and int(m) <= 12):
        date = f"{y}-{int(m):02}-{int(d):02}"
        return date


while True:
    try:
        date = input("Date: ").replace("/", " ").strip()
        month, day, year = date.split(" ")
        verify = verify_date(month, day, year)
        if verify:
            print(verify)
            break
    except ValueError:
        pass