from pyfiglet import Figlet
from sys import argv, exit
figlet = Figlet()
list_fonts = figlet.getFonts()

def set_text(arguments):
    print(argv)
    if arguments == 1:
        text = input("Input: ")
        print(figlet.renderText(text))
    elif arguments == 3 and argv[2] in list_fonts and (argv[1] == '-f' or argv[1] == '--font'):
        text = input("Input: ")
        figlet.setFont(font=argv[2])
        print(figlet.renderText(text))
    else:
        exit("Invalid usage")

set_text(len(argv))