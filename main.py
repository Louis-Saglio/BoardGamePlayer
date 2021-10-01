# game.py module and the ones who depends on it were modified but this file was not updated to fit these changes
# last working commit : 9e4ddfb4931727e75b00dba4b934cdd302c644ef
from decision_tree import get_best_action
from tictactoe import TicTacToe


def main():
    game = TicTacToe()
    i = 0
    while game.get_possible_actions():
        with open(f"diagraph.{i}.dot", "w") as f:
            action = get_best_action(game, game.playing_player, True, file=f)
        game.play(action)
        print("-" * 30)
        print(game)
        i += 1


if __name__ == "__main__":
    main()
