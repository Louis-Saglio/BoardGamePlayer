# game.py module and the ones who depends on it were modified but this file was not updated to fit these changes
# last working commit : 9e4ddfb4931727e75b00dba4b934cdd302c644ef
from __future__ import annotations

import os
import pickle
from typing import Optional, List, Set, Any

from decision_tree import GameInterface, Player, Action


class Game(GameInterface):

    state = [".", ".", ".", "."]
    players = (0, 1)
    _playing_player_index = 0

    def do_action(self, action: Action):
        self.state[action] = str(self.playing_player_index)

    def revert(self, action):
        self.state[action] = "."

    def get_current_winners(self) -> Set[Player]:
        state_as_str = "".join(self.state)
        winners = set()
        range_half_state_length = range(len(self.state) // 2)
        for player in self.players:
            player_as_str = str(player)
            if "".join(player_as_str for _ in range_half_state_length) in state_as_str:
                winners.add(player)
        return winners

    def get_possible_actions(self):
        return {i for i, item in enumerate(self.state) if item == "."}

    @property
    def playing_player_index(self):
        self._playing_player_index = int(not self._playing_player_index)
        return self._playing_player_index

    @property
    def playing_player(self):
        return self.players[self.playing_player_index]

    def get_state_id(self):
        return "".join(self.state)


def write(content, file_path="data/digraph.dot", **kwargs):
    with open(file_path, "a") as f:
        print(content, file=f, **kwargs)


class Node:
    def __init__(self, state: Any, parent: Optional[Node]):
        self.state: Any = state
        self.parent: Optional[Node] = parent
        self.children: List[Node] = []


def build_tree(game: GameInterface, parent: Node = None):
    if parent is None:
        parent = Node(game.get_state_id(), None)
    if not game.get_current_winners():
        for action in game.get_possible_actions():
            game.do_action(action)
            node = Node(game.get_state_id(), parent)
            parent.children.append(node)
            build_tree(game, node)
            game.revert(action)
    return parent


def draw_tree(root: Node, relations=None):
    if relations is None:
        relations = set()
    for child in root.children:
        relations.add(f'"{root.state}" -> "{child.state}"')
        draw_tree(child, relations)
    return relations


def evaluate_actions(root):
    pass


if __name__ == "__main__":

    def main(load_from=None, save_to=None):
        if load_from:
            with open(load_from, "rb") as f:
                tree = pickle.load(f)
        else:
            tree = build_tree(Game())

        if save_to:
            with open(save_to, "wb") as f:
                pickle.dump(tree, f)

        with open("data/digraph.dot", "w") as f:
            f.write("digraph {")
            f.write("\n".join(draw_tree(tree)))
            f.write("}")
        return locals()

    # scope = main(None, "data/game_tree.pickle")
    # scope = main("data/game_tree.pickle", None)
    scope = main()
    os.system("dot -Tpng data/digraph.dot -o out.png")
