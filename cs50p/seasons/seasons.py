from datetime import date
import inflect
import re
import sys

p = inflect.engine()

def main():
    print(convert_to_minutes(input("Date of Birth: ")))


def convert_to_minutes(s):
    try:
        matches = re.search(r"(\d\d\d\d)-(\d\d)-(\d\d)", s)
        year, month, day = matches.group().split("-")
        date_birth = date(int(year), int(month), int(day))
        diff = date.today() - date_birth
        minutes = diff.days * 24 * 60
        return f"{p.number_to_words(minutes, andword='').capitalize()} minutes"
    except AttributeError:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()