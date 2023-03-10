items = {}
while True:
    try:
        item = input().upper()
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    except EOFError:
        for i in sorted(items):
            print(f"{items[i]} {i}")
        break