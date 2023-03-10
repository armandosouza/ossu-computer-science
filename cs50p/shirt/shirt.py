from sys import exit, argv
from PIL import ImageOps, Image
from os import path

if len(argv) < 3:
    exit("Too few command-line arguments")
elif len(argv) > 3:
    exit("Too many command-line arguments")
else:
    allowed_ext = [".jpg", ".jpeg", ".png"]
    file_input, ext_input = path.splitext(argv[1])
    file_output, ext_output = path.splitext(argv[2])
    if ext_input != ext_output:
        exit("Input and output have different extensions")
    elif not ext_input:
        exit("Invalid input")
    elif not ext_output:
        exit("Invalid output")
    elif ext_input.lower() not in allowed_ext or ext_output.lower() not in allowed_ext:
        exit("File type not supported")
    else:
        try:
            with Image.open("shirt.png") as shirt:
                photo = Image.open(argv[1])
                size = shirt.size
                resize = ImageOps.fit(photo, size)
                resize.paste(shirt, shirt)
                resize.save(argv[2])
        except FileNotFoundError:
            exit("Input does not exist")