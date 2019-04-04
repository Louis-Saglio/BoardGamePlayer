from tictactoe import TicTacToe

game = TicTacToe()
game.play((0, 0))
game.play((2, 0))
game.play((0, 1))
game.play((1, 2))
game.play((0, 2))

result = game.get_result_for(0)
assert result == TicTacToe.Result.WON, result

result = game.get_result_for(1)
assert result == TicTacToe.Result.LOST, result


game = TicTacToe()
game.play((0, 0))
game.play((0, 2))
game.play((1, 2))

result = game.get_result_for(0)
assert result == TicTacToe.Result.NOT_ENDED, result

result = game.get_result_for(1)
assert result == TicTacToe.Result.NOT_ENDED, result


game = TicTacToe()
game.play((0, 0))
game.play((0, 1))
game.play((0, 2))
game.play((1, 1))
game.play((1, 0))
game.play((2, 0))
game.play((2, 1))
game.play((1, 2))
game.play((2, 2))

result = game.get_result_for(0)
assert result == TicTacToe.Result.DRAW, result

result = game.get_result_for(1)
assert result == TicTacToe.Result.DRAW, result


game = TicTacToe()
game.play((0, 0))
game.play((0, 2))
game.play((1, 0))
game.play((1, 2))
game.play((2, 0))
game.play((2, 1))

actions = game.get_possible_actions()
assert set(actions) == frozenset({(0, (2, 2)), (0, (0, 1)), (0, (1, 1))}), actions


game = TicTacToe()
game.play((0, 0))
game.play((0, 2))
game.play((1, 0))
game.play((1, 2))
game.play((2, 1))
game.play((2, 0))

actions = game.get_possible_actions()
assert set(actions) == frozenset({(0, (2, 2)), (0, (0, 1)), (0, (1, 1))}), actions


game = TicTacToe()
game.play((0, 0))
game.play((0, 2))
game.play((1, 0))
game.play((1, 2))
game.play((2, 1))
game.play((2, 0))
game.play((2, 2))
game.play((0, 1))
game.play((1, 1))

actions = game.get_possible_actions()
assert actions == frozenset(), actions
