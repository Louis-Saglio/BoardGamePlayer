from __future__ import annotations

from typing import FrozenSet, Any, Tuple


class Game:
    class Result:
        DRAW = "draw"
        NOT_ENDED = "not ended"
        WON = "won"
        LOST = "lost"

    @property
    def players(self) -> Tuple:
        raise NotImplementedError

    @property
    def playing_player(self):
        return self.players[self.playing_player_index]

    @property
    def playing_player_index(self):
        raise NotImplementedError

    def play(self, action):
        raise NotImplementedError

    def get_possible_actions(self) -> FrozenSet[Tuple[Any, Any]]:
        raise NotImplementedError

    def get_result_for(self, player) -> Game.Result:
        raise NotImplementedError

    def deepcopy(self) -> Game:
        raise NotImplementedError
