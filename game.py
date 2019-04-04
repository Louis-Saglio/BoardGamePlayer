from __future__ import annotations

from typing import FrozenSet, Any, Tuple


class Game:
    class Result:
        DRAW = "draw"
        NOT_ENDED = "not ended"
        WON = "won"
        LOST = "lost"

    playing_player_index = 0

    @property
    def players(self):
        raise NotImplementedError

    def _rotate_players(self):
        if self.playing_player_index == len(self.players) - 1:
            self.playing_player_index = 0
        else:
            self.playing_player_index += 1

    def process_action(self, action):
        raise NotImplementedError

    def play(self, action):
        self.process_action(action)
        self._rotate_players()

    def get_possible_actions(self) -> FrozenSet[Tuple[Any, Any]]:
        raise NotImplementedError

    def get_result_for(self, player) -> Game.Result:
        raise NotImplementedError
