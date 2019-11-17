from decision_tree import get_best_action
from tictactoe import TicTacToe


def main():
    game = TicTacToe()
    while game.get_possible_actions():
        action = get_best_action(game, game.get_current_player(), True)
        game.play_action(action)
        print("-" * 30)
        print(game)


if __name__ == '__main__':
    main()
