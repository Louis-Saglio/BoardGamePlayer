import pickle

from player import build_game_tree_for
from tictactoe import TicTacToe


def pickle_dump_tictactoe_tree():
    with open("data/saved_tictactoe_tree", "wb") as f:
        pickle.dump(build_game_tree_for(TicTacToe(), 0), f)


def pickle_load_tictactoe_tree():
    with open("data/saved_tictactoe_tree", "rb") as f:
        return pickle.load(f)
