import random


def main():
    try:
        level = get_level()
        tries = 3
        equations = 10
        points = 0
        while equations > 0:
            x = generate_integer(level)
            y = generate_integer(level)
            correct = x + y
            while True:
                answer = input(f"{x} + {y} = ")
                if answer == str(correct):
                    points += 1
                    equations -= 1
                    tries = 3
                    break
                else:
                    print("EEE")
                    if tries == 1:
                        print(f"{x} + {y} = {correct}")
                        equations -= 1
                        tries = 3
                        break
                    else:
                        tries -= 1
        print(f"Answers: {points}")
    except ValueError:
        pass


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                break
        except ValueError:
            pass
    return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()