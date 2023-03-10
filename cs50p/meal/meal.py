def main():
    time_converted = convert(input("What time is it? "))
    if 7 <= time_converted <= 8:
        print("breakfast time")
    elif 12 <= time_converted <= 13:
        print("lunch time")
    elif 18 <= time_converted <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    minutes = int(minutes) / 60
    return float(int(hours) + minutes)


if __name__ == "__main__":
    main()