from typing import Set


class Player:
    pass


class GameInterface:
    def play(self, action):
        raise NotImplementedError

    def revert(self, action):
        raise NotImplementedError

    def get_current_winners(self) -> Set[Player]:
        raise NotImplementedError

    def get_possible_actions(self):
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


def get_best_action(game: GameInterface, player: Player, return_action=False, file=None):
    score_by_action = {}
    it_is_player_turn = game.playing_player is player
    previous_state_id = str(game).replace("\n", "\\n")

    if return_action:
        print("digraph {", file=file)
    for action in game.get_possible_actions():
        game.play(action)

        replace = str(game).replace("\n", "\\n")
        print(f'"{previous_state_id}" -> "{replace}"', file=file)
        if it_is_player_turn:
            if player in game.get_current_winners():
                if len(game.get_current_winners()) == 1:
                    score = 3
                else:
                    score = 2
            elif game.get_current_winners():
                score = 0
            else:
                if not game.get_possible_actions():
                    score = 1
                else:
                    score = get_best_action(game, player, file=file)
        else:
            if game.get_current_winners() and player not in game.get_current_winners():
                score = 0
            else:
                if not game.get_possible_actions():
                    score = 1
                else:
                    score = get_best_action(game, player, file=file)

        score_by_action[action] = score
        game.revert(action)

    if return_action:
        print("}", file=file)
        return max(score_by_action, key=lambda x: score_by_action[x])
    return max(score_by_action.values())
