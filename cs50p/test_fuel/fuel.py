def main():
    while True:
        try:
            tank = convert(input("Fraction: "))
            tank_status = gauge(tank)
            print(tank_status)
            break
        except ValueError:
            pass
        except ZeroDivisionError:
            pass


def convert(fraction):
    x, y = fraction.split("/")
    if not x.isdigit() or not y.isdigit() and int(x) > int(y):
        raise ValueError
    if int(y) == 0:
        raise ZeroDivisionError
    fuel = int(x) / int(y)
    return int(round(fuel * 100))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()