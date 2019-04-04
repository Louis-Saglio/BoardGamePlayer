from copy import deepcopy
from typing import Tuple, FrozenSet, Any

from game import Game


def reverse_dict_get(dico, value):
    for key, v in dico.items():
        if value == v:
            return key


class TicTacToe(Game):
    def __init__(self):
        self._players = (0, 1)
        self.symbols = {0: "x", 1: "o", None: "."}
        self.state = []
        for x in range(3):
            self.state.append([self.symbols[None] for _ in range(3)])
        self._playing_player_index = 0

    def __str__(self):
        return "\n".join([" ".join(line) for line in self.state])

    @property
    def playing_player_index(self):
        return self._playing_player_index

    @property
    def players(self):
        return self._players

    def play(self, action: Tuple[int, int]):
        self.state[action[0]][action[1]] = self.symbols[self.playing_player]
        if self._playing_player_index == len(self.players) - 1:
            self._playing_player_index = 0
        else:
            self._playing_player_index += 1

    def get_possible_actions(self) -> FrozenSet[Tuple[Any, Any]]:
        actions = set()
        for x in range(len(self.state)):
            for y in range(len(self.state[x])):
                cell = self.state[x][y]
                if cell != self.symbols[None]:
                    continue
                actions.add((self.playing_player, (x, y)))
        return frozenset(actions)

    def get_result_for(self, player) -> Game.Result:
        winner, is_draw, potential_winner = None, True, None
        for line in (
                ((0, 0), (0, 1), (0, 2)),
                ((1, 0), (1, 1), (1, 2)),
                ((2, 0), (2, 1), (2, 2)),
                ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)),
                ((0, 2), (1, 2), (2, 2)),
                ((0, 0), (1, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)),
        ):
            winning_line = True
            for x, y in line:
                if is_draw and self.state[x][y] == self.symbols[None]:
                    is_draw = False
                actual_player = reverse_dict_get(self.symbols, self.state[x][y])
                if potential_winner is None:
                    potential_winner = actual_player
                elif actual_player != potential_winner:
                    winning_line = False
            if winning_line:
                winner = potential_winner
                is_draw = False
                break
        return (
            Game.Result.DRAW
            if is_draw
            else Game.Result.NOT_ENDED
            if winner is None
            else Game.Result.WON
            if winner is player
            else Game.Result.LOST
        )
