from sys import exit, argv
from csv import reader
from tabulate import tabulate

if len(argv) == 1:
    exit("Too few command-line arguments")
elif len(argv) > 2:
    exit("Too many command-line arguments")
elif not argv[1].endswith(".csv"):
    exit("Not a CSV file")
else:
    try:
        table = []
        with open(argv[1]) as file:
            reader = reader(file)
            for row in reader:
                table.append(row)
        print(tabulate(table[1:], table[0], tablefmt="grid"))
    except FileNotFoundError:
        exit("File does not exist")