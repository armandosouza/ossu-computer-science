import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(s):
    matches = re.search(r"((?:[12]?[0-9]):?(?:[0-5][0-9])?) ([AP]M) to ((?:[12]?[0-9]):?(?:[0-5][0-9])?) ([AP]M)", s.strip())
    if matches:
        h1, p1, to, h2, p2 = matches.group().split(" ")
        time1 = convert_to_24(h1, p1)
        time2 = convert_to_24(h2, p2)
        return f"{time1} to {time2}"
    else:
        raise ValueError


def convert_to_24(hour, period):
    if len(hour) <= 2:
        if (period == "AM" and hour != "12") or (period == "PM" and hour == "12"):
            return f"{int(hour):02}:00"
        elif period == "PM" and hour != "12":
            return f"{(int(hour) + 12):02}:00"
        elif period == "AM" and hour == "12":
            return f"00:00"
    hours, minutes = hour.split(":")
    if (period == "AM" and hours != "12") or (period == "PM" and hours == "12"):
        return f"{int(hours):02}:{minutes}"
    elif period == "AM" and hours == "12":
        return f"00:{minutes}"
    elif period == "PM" and int(hours) < 12:
        return f"{int(hours) + 12}:{minutes}"
    else:
        raise ValueError


if __name__ == "__main__":
    main()