from __future__ import annotations


class Game:
    class Result:
        DRAW = "draw"
        NOT_ENDED = "not ended"
        WON = "won"
        LOST = "lost"

    def play(self, action):
        raise NotImplementedError

    def get_possible_actions(self) -> set:
        raise NotImplementedError

    def get_result_for(self, player) -> Game.Result:
        raise NotImplementedError
