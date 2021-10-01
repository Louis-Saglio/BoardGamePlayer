from typing import Set, TypeVar, Generic, Tuple

Action = TypeVar("Action")
Player = TypeVar("Player")


class GameInterface(Generic[Action, Player]):
    def play(self, action: Action) -> Tuple[Set[Player], Set[Action]]:
        self.do_action(action)
        return self.get_current_winners(), self.get_possible_actions()

    def do_action(self, action: Action):
        raise NotImplementedError

    def revert(self, action: Action):
        raise NotImplementedError

    def get_current_winners(self) -> Set[Player]:
        raise NotImplementedError

    def get_possible_actions(self) -> Set[Action]:
        raise NotImplementedError

    @property
    def playing_player_index(self):
        raise NotImplementedError

    @property
    def playing_player(self):
        raise NotImplementedError

    def get_state_id(self):
        raise NotImplementedError


def compare(action_result):
    return action_result[1]


def get_best_action(game: GameInterface, player: Player):
    score_by_action = {}
    for action in game.get_possible_actions():
        game.play(action)
        winners = game.get_current_winners()
        possible_actions = game.get_possible_actions()
        if game.playing_player is player:
            if player in winners:
                if len(winners) == 1:
                    score = 3
                else:
                    score = 2
            elif winners:
                score = 0
            else:
                if not possible_actions:
                    score = 1
                else:
                    score = get_best_action(game, player)
        else:
            if player not in winners:
                score = 0
            else:
                if not possible_actions:
                    score = 1
                else:
                    score = get_best_action(game, player)

        score_by_action[action] = score
        game.revert(action)
    return max(score_by_action.values())
