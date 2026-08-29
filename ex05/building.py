import string
import sys


def couter(text: str) -> int:
    """count characters by type."""
    uppers = 0
    lowers = 0
    digits = 0
    spaces = 0
    punctuations = 0

    for char in text:
        if char.isupper():
            uppers += 1
        elif char.islower():
            lowers += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        elif char in string.punctuation:
            punctuations += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{uppers} upper letters")
    print(f"{lowers} lower letters")
    print(f"{punctuations} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """the main program."""
    try:
        if len(sys.argv) == 1:
            text = input("What is the text to count? ")
            text += '\n'
        elif len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            raise AssertionError("more than one argument is provided")
        couter(text)

    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()
