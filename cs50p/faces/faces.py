def convert(facedText):
    newText = facedText.replace(":)", "🙂").replace(":(","🙁")
    return newText

def main():
    textUser = str(input("Type some text: "))
    print(convert(textUser))

main()