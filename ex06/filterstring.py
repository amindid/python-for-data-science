import sys
from ft_filter import ft_filter


def main():
    """Filter words according to their length."""
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        if not isinstance(sys.argv[1], str) or not sys.argv[2].isdigit():
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        number = int(sys.argv[2])

        words = text.split(" ")

        result = list(ft_filter(lambda word: len(word) > number, words))

        print(result)

    except AssertionError as error:
        print("AssertionError:", error)


if __name__ == "__main__":
    main()
