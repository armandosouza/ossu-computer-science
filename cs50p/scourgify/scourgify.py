from sys import exit, argv
from csv import DictReader, DictWriter

if len(argv) < 3:
    exit("Too few command-line arguments")
elif len(argv) > 3:
    exit("Too many command-line arguments")
else:
    try:
        with open(argv[2], 'w', newline='') as csvfile:
            fieldnames = ["first", "last", "house"]
            writer = DictWriter(csvfile, fieldnames=fieldnames)
            with open(argv[1]) as file:
                reader = DictReader(file)
                writer.writeheader()
                for row in reader:
                    surname, name = row['name'].split(',')
                    writer.writerow({'first': name.lstrip(), 'last': surname, 'house': row['house']})
    except FileNotFoundError:
        exit(f"Could not read {argv[0]}")