import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        matches = re.search(r"(src=)\"http(s?)\:\/\/(www\.)?(youtube\.com\/embed/\w+)", s)
        url = matches.group(4)
        link, embed, id = url.split("/")
        link = link.replace("youtube.com", "youtu.be")
        return f"https://{link}/{id}"
    except AttributeError:
        return "None"


if __name__ == "__main__":
    main()