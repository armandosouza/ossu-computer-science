def main():
    amount = 50
    while amount > 0:
        print(f"Amount Due: {amount}")
        coin = int(input("Insert Coin: "))
        coin_verified = verify_coin(coin)
        amount -= coin_verified
    print(f"Change Owed: {amount * -1}")


def verify_coin(c):
    accepted_coins = [5, 10, 25]
    if c in accepted_coins:
        return c
    else:
        return 0


main()