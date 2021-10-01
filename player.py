# game.py module and the ones who depends on it were modified but this file was not updated to fit these changes
# last working commit : 9e4ddfb4931727e75b00dba4b934cdd302c644ef


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
        self.cached_outcome = None

    @property
    def data(self):
        return f"{self.outcome}, {self.player}"

    @property
    def id(self):
        return str(id(self))[-4:]

    def __str__(self):
        return "\n".join(
            (
                f"father   : {getattr(self.father, 'id', None)}, {getattr(self.father, 'data', None)}",
                f"self     : {self.id}, {self.data}",
                "children\n\t",
            )
        ) + ("\n\t".join(f"{child.id}, {child.data}" for child in self.children) if self.children else " []")

    def predict_outcome_for(self, player):
        outcome = Game.Result.NOT_ENDED
        if self.outcome == Game.Result.NOT_ENDED:
            all_solved = True
            leads_to_draw = True
            for child in self.children:
                if child.outcome == Game.Result.NOT_ENDED:
                    all_solved = False
                if leads_to_draw and child.outcome != Game.Result.DRAW:
                    leads_to_draw = False
                if child.player == player and child.outcome == Game.Result.WON:
                    outcome = Game.Result.WON
                elif child.player != player and child.outcome == Game.Result.LOST:
                    outcome = Game.Result.LOST
            if leads_to_draw:
                outcome = Game.Result.DRAW
            elif all_solved:
                outcome = child.outcome
        if outcome != Game.Result.NOT_ENDED:
            for child in self.children[:]:
                if child.outcome == outcome:
                    print("kill")
                    self.children.remove(child)
                    del child
        self.cached_outcome = outcome
        return outcome
        # assert node.outcome != Game.Result.NOT_ENDED

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
        precedent_node = ActionNode(None, None, game.get_result_for(player), None)
    for action in game.get_possible_actions():
        copied_game = game.deepcopy()
        copied_game.play(action)
        node = ActionNode(game.playing_player, action, copied_game.get_result_for(player), precedent_node)
        if node.outcome == Game.Result.NOT_ENDED:
            build_game_tree_for(copied_game, player, node)
    return precedent_node


def analyse_tree_for(node: ActionNode, player):
    i = 0
    node = node.get_first_final_child()
    while True:
        # if i % 1_000_000 == 0:
        #     print(i)
        # print("-" * 30)
        # print(node)
        # input()
        if node.outcome != Game.Result.NOT_ENDED:
            if node.father is None:
                # print("last node solved")
                break
            # print("node is solved, go to father")
            node = node.father
        elif node.predict_outcome_for(player) != Game.Result.NOT_ENDED:
            node.outcome = node.cached_outcome
            i += 1
            # print("node is solvable, solve it")
        else:
            # print("choose child to solve")
            for child in node.children:
                if child.outcome == Game.Result.NOT_ENDED:
                    # print("solve child")
                    break
            node = child


def get_game_tree(game) -> ActionNode:
    try:
        node = utils.pickle_load_tictactoe_tree()
    except Exception as e:
        print(e)
        node = build_game_tree_for(game, game.players[0])
    return node


def play(game: Game):
    node = get_game_tree(game)
    print(node)
    return
    print("tree loaded")
    analyse_tree_for(node, game.players[0])
    while node.children:
        while True:
            action = tuple(map(int, input("choose position x,y").split(',')))
            found = False
            for child in node.children:
                if child.action == action:
                    found = True
                    break
            if found:
                node = child
                break
        node: ActionNode = choice([child for child in node.children if child.outcome != Game.Result.NOT_ENDED])

        game.play(node.action)
        print(game)
        print("result ", node.outcome)
        # print("predict", node.predict_outcome_for(game.players[0]))
        print("-" * 30)


if __name__ == "__main__":
    play(TicTacToe())
