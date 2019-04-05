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

    @property
    def is_solvable(self):
        return all(child.outcome != Game.Result.NOT_ENDED for child in self.children)

    def get_first_final_child(self) -> ActionNode:
        node = self
        while node.children:
            node = node.children[0]
        return node


def build_game_tree_for(game: Game, player, precedent_node: ActionNode = None):
    assert player in game.players
    if precedent_node is None:
        precedent_node = ActionNode(player, None, game.get_result_for(player), None)
    for action in game.get_possible_actions():
        copied_game = game.deepcopy()
        copied_game.play(action)
        node = ActionNode(game.playing_player, action, copied_game.get_result_for(player), precedent_node)
        if node.outcome == Game.Result.NOT_ENDED:
            build_game_tree_for(copied_game, player, node)
    return precedent_node


def analyse_node_for(node: ActionNode, player):
    if node.outcome == Game.Result.NOT_ENDED:
        leads_to_draw = True
        for child in node.children:
            if leads_to_draw and child.outcome != Game.Result.DRAW:
                leads_to_draw = False
            if child.player == player and child.outcome == Game.Result.WON:
                node.outcome = Game.Result.WON
                break
            elif child.player != player and child.outcome == Game.Result.LOST:
                node.outcome = Game.Result.LOST
                break
        if leads_to_draw:
            node.outcome = Game.Result.DRAW
        if node.outcome != Game.Result.NOT_ENDED:
            for child in node.children[:]:
                if child.outcome == node.outcome:
                    # print("kill")
                    node.children.remove(child)
                    del child


def analyse_tree_for(node: ActionNode, player):
    if node.outcome != Game.Result.NOT_ENDED:
        # print(1)
        pass
    elif node.is_solvable:
        # print(2)
        analyse_node_for(node, player)
        assert node.outcome != Game.Result.NOT_ENDED
        # print(node.outcome)
    else:
        # print(3)
        for child in node.children:
            analyse_tree_for(child, player)


def get_game_tree(game) -> ActionNode:
    try:
        node = utils.pickle_load_tictactoe_tree()
    except Exception as e:
        print(e)
        node = build_game_tree_for(game, game.players[0])
    return node


def play(game: Game):
    node = get_game_tree(game)
    analyse_tree_for(node, game.players[0])
    while node.children:
        node: ActionNode = choice(node.children)
        game.play(node.action)
        print(game)
        print("result ", node.outcome)
        # analyse_node_for(node, game.players[0])
        # print("predict", node.outcome)
        print("-" * 30)


if __name__ == "__main__":
    play(TicTacToe())
