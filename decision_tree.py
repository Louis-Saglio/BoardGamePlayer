from random import choice
from typing import Set


class Player:
    pass


class GameInterface:

    def play_action(self, action):
        raise NotImplementedError

    def revert_action(self, action):
        raise NotImplementedError

    def get_current_winners(self) -> Set[Player]:
        raise NotImplementedError

    def get_possible_actions(self):
        raise NotImplementedError

    def get_current_player(self) -> Player:
        raise NotImplementedError


def compare(action_result):
    return action_result[1]


def get_best_action(game: GameInterface, player: Player, return_action=False):
    result_by_action = {}
    for action in game.get_possible_actions():
        game.play_action(action)
        if player in game.get_current_winners() and len(game.get_current_winners()) == 1:
            # If player is the only winner
            result_by_action[action] = 3
        elif player in game.get_current_winners():
            # If player is in the winners
            result_by_action[action] = 2
        elif game.get_current_winners().difference({player}):
            # If there is at lest one winner and player is not in the winner list
            result_by_action[action] = 0
        elif not game.get_current_winners():
            # If no winner
            result_by_action[action] = get_best_action(game, player)
        else:
            raise RuntimeError
        game.revert_action(action)

    if not game.get_possible_actions():
        return 1
    elif return_action:
        action_by_result = {}
        for action, result in result_by_action.items():
            if result not in action_by_result:
                action_by_result[result] = []
            action_by_result[result].append(action)
        for i in range(0, 4):
            if i in action_by_result:
                return choice(action_by_result[i])
        raise RuntimeError
    else:
        return max(result_by_action.values())
