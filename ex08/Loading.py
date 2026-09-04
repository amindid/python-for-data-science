import os


def ft_tqdm(lst: range) -> None:
    """Display a progress bar while iterating over a range."""
    total = len(lst)
    current = 0

    terminal_width = os.get_terminal_size().columns

    for elem in lst:
        current += 1

        percent = int(current / total * 100)

        bar_length = terminal_width - 20
        filled = int(bar_length * current / total)

        bar = "=" * filled + ">" + " " * (bar_length - filled)

        print(
            f"\r{percent:3d}%|[{bar}]| {current}/{total}",
            end="",
            flush=True
        )

        yield elem
