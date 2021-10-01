from copy import deepcopy
from string import digits, ascii_letters
from typing import Tuple, FrozenSet, Any, Set

from decision_tree import GameInterface, Player
from game import Game
from utils import convert


def reverse_dict_get(dico, value):
    for key, v in dico.items():
        if value == v:
            return key


class TicTacToe(Game[Tuple[int, int], int]):
    def __init__(self):
        self._players = (0, 1)
        self.symbols = {0: "x", 1: "o", None: "."}
        self.state = []
        for x in range(3):
            self.state.append([self.symbols[None] for _ in range(3)])
        self._playing_player_index = 0

    def __str__(self):
        return "\n".join([" ".join(line) for line in self.state])

    def revert(self, action):
        self.state[action[0]][action[1]] = self.symbols[None]
        if self._playing_player_index == len(self.players) - 1:
            self._playing_player_index = 0
        else:
            self._playing_player_index += 1

    def get_current_winners(self) -> Set[Player]:
        return {player for player in self.players if self.get_result_for(player) == Game.Result.WON}

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
                actions.add((x, y))
        return frozenset(actions)

    def get_result_for(self, player) -> Game.Result:
        is_draw = True
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
            old_value = self.state[line[0][0]][line[0][1]]
            if is_draw and old_value == self.symbols[None]:
                is_draw = False
            for x, y in line[1:]:
                if is_draw and self.state[x][y] == self.symbols[None]:
                    is_draw = False
                if self.state[x][y] != old_value:
                    break
            else:
                if old_value != self.symbols[None]:
                    return Game.Result.WON if reverse_dict_get(self.symbols, old_value) == player else Game.Result.LOST
        return Game.Result.DRAW if is_draw else Game.Result.NOT_ENDED

    def deepcopy(self) -> Game:
        new_game = TicTacToe()
        new_game.state = deepcopy(self.state)
        new_game._playing_player_index = self._playing_player_index
        return new_game

    def get_state_id_old(self):
        value_by_cell_state = {".": "0", "x": "1", "o": "2"}
        state_id = ""
        for row in self.state:
            for cell in row:
                state_id += value_by_cell_state[cell]
        chars = digits + ascii_letters
        return convert(state_id, len(value_by_cell_state), len(chars), chars)

    def get_state_id(self):
        return str(self).replace("\n", "\\n")
