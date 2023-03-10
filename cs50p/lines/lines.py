import sys

def main():
    check_args(sys.argv)


def check_args(args):
    if len(args) == 1:
        sys.exit("Too few command-line arguments")
    elif len(args) > 2:
        sys.exit("Too many command-line arguments")
    elif not args[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        print(open_file(args[1]))


def open_file(f):
    lines = 0
    try:
        with open(f) as file:
            for row in file:
                if not row.lstrip().startswith("#") and not row.isspace():
                    lines += 1
            return lines
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()