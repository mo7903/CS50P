import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Tries to parse and returns none if a problem arises
    try:

        # Raises an error if no iframe attribute is present
        if "<iframe" not in s:
            raise IndexError

        # Finds the match for a youtube embed link
        matches = re.findall(r"https?://(?:www\.)?youtube\.com/embed/\w+", s)

        # Replaces the link with the watch link depending on its format
        if "www." not in matches[0]:
            link = re.sub(r"https?://youtube\.com/embed", "https://youtu.be", matches[0])
        else:
            link = re.sub(r"https?://www.youtube\.com/embed", "https://youtu.be", matches[0])
    except IndexError:
        link = None
    return link



if __name__ == "__main__":
    main()