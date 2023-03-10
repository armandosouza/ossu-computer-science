def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    print(f'{calculate(x, y, z):.1f}')


def calculate(n1, op, n2):
    match op:
        case '+':
            return int(n1) + int(n2)
        case '-':
            return int(n1) - int(n2)
        case '*':
            return int(n1) * int(n2)
        case '/':
            return int(n1) / int(n2)


main()