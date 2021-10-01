from __future__ import annotations

from typing import FrozenSet, Tuple, Generic, TypeVar, Dict

Action = TypeVar("Action")
Player = TypeVar("Player")


class Game(Generic[Action, Player]):
    class Result:
        DRAW = "draw"
        NOT_ENDED = "not ended"
        WON = "won"
        LOST = "lost"

    @property
    def players(self) -> Tuple[Player, ...]:
        raise NotImplementedError

    @property
    def playing_player(self) -> Player:
        return self.players[self.playing_player_index]

    @property
    def playing_player_index(self) -> int:
        raise NotImplementedError

    def play(self, action: Action) -> Dict[Player, Result]:
        raise NotImplementedError

    def get_possible_actions(self) -> FrozenSet[Tuple[Action, ...]]:
        raise NotImplementedError

    def deepcopy(self) -> Game:
        raise NotImplementedError
