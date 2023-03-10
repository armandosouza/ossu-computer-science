def main():
    print(shorten(input("Input: ")))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    tweet = ''
    for c in word:
        if(c.lower()) not in vowels:
            tweet += c
    return tweet


main()