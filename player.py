from __future__ import annotations

from random import choice
from typing import Optional

import utils
from game import Game
from tictactoe import TicTacToe


class ActionNode:
    def __init__(self, player, action, outcome, father: Optional[ActionNode]):
        self.player = player
        self.action = action
        self.outcome = outcome
        self.father = father
        self.children = []
        if self.father is not None:
            self.father.children.append(self)


def build_game_tree_for(game: Game, player, precedent_node: ActionNode = None):
    assert player in game.players
    if precedent_node is None:
        precedent_node = ActionNode(player, None, game.get_result_for(player), None)
    for action in game.get_possible_actions():
        copied_game = game.deepcopy()
        copied_game.play(action)
        node = ActionNode(game.playing_player, action, copied_game.get_result_for(player), precedent_node)
        build_game_tree_for(copied_game, player, node)
    return precedent_node


def play():
    game = TicTacToe()
    try:
        node = utils.pickle_load_tictactoe_tree()
    except Exception as e:
        print(e)
        node = build_game_tree_for(game, 0)
    while True:
        node: ActionNode = choice(node.children)
        game.play(node.action)
        print(game)
        print("-" * 30)
        if not node.children:
            break


if __name__ == "__main__":
    play(TicTacToe())
