import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):

    url = re.search(r'src=\"(.+?)\"', s)
    if not url:
        return
    else:
        url = url.group(1)

    matches = re.search("^(?:https?://)(?:www\.)?youtube\.com\/embed(\/.+)$", url)
    if matches:
        link = "https://youtu.be"+matches.group(1)
        return link


if __name__ == "__main__":
    main()