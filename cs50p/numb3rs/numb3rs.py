import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.fullmatch(r'(([0-2][0-5][0-5]|[0-2][0-4][\d]|[0-1][\d][\d]|[\d\d?])\.){3}([0-2][0-5][0-5]|[0-2][0-4][\d]|[0-1][\d][\d]|[\d\d?])', ip)
    if matches:
        return True
    return False


if __name__ == "__main__":
    main()