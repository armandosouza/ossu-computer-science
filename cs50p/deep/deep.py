answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
answer = answer.lower().strip().replace("-", " ")

match answer:
    case 'forty two' | '42':
        print('Yes')
    case _:
        print('No')
