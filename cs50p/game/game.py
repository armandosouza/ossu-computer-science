from random import randint

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            pass
        number = randint(1, level)
        while True:
            try:
                guess = int(input("Guess: "))
                if guess < 1:
                    pass
                elif guess > number:
                    print("Too large!")
                elif guess < number:
                    print("Too small!")
                else:
                    print("Just right!")
                    break
            except ValueError:
                pass
        break
    except ValueError:
        pass