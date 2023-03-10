while True:
    try:
        tank = input("Fraction: ")
        x, y = tank.split("/")
        fuel = int(x) / int(y)
        fuel_percentage = round(fuel * 100)
        if fuel > 1:
            pass
        else:
            if 0.99 <= fuel <= 1:
                print("F")
            elif fuel <= 0.01:
                print("E")
            else:
                print(f"{fuel_percentage}%")
            break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass