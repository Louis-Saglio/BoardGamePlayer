import pickle
from string import digits, ascii_lowercase


def pickle_dump_tictactoe_tree(tree):
    with open("data/saved_tictactoe_tree", "wb") as f:
        pickle.dump(tree, f)


def pickle_load_tictactoe_tree():
    with open("data/saved_tictactoe_tree", "rb") as f:
        return pickle.load(f)


def convert(number: str, from_base: int, to_base: int, chars=digits + ascii_lowercase) -> str:
    value_by_figure = {figure: i for i, figure in enumerate(chars)}
    decimal = 0
    for i, figure in enumerate(number[::-1]):
        decimal += value_by_figure[figure] * from_base ** i
    destination = ""
    while decimal:
        destination += chars[decimal % to_base]
        decimal //= to_base
    return destination[::-1] or "0"
