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
