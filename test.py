from tictactoe import TicTacToe


def test_result_0():
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


def test_result_1():
    game = TicTacToe()
    game.play((0, 0))
    game.play((0, 2))
    game.play((1, 2))

    result = game.get_result_for(0)
    assert result == TicTacToe.Result.NOT_ENDED, result

    result = game.get_result_for(1)
    assert result == TicTacToe.Result.NOT_ENDED, result


def test_result_2():
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


def test_result_3():
    game = TicTacToe()
    game.play((0, 2))

    result = game.get_result_for(0)
    assert result == TicTacToe.Result.NOT_ENDED, result

    result = game.get_result_for(1)
    assert result == TicTacToe.Result.NOT_ENDED, result


def test_result_4():
    game = TicTacToe()
    game.play((1, 1))
    game.play((1, 0))
    game.play((0, 2))

    result = game.get_result_for(0)
    assert result == TicTacToe.Result.NOT_ENDED, result

    result = game.get_result_for(1)
    assert result == TicTacToe.Result.NOT_ENDED, result


def test_result_5():
    game = TicTacToe()
    game.play((1, 2))
    game.play((1, 1))
    game.play((0, 0))
    game.play((1, 1))
    game.play((2, 0))
    game.play((0, 1))

    result = game.get_result_for(0)
    assert result == TicTacToe.Result.NOT_ENDED, result

    result = game.get_result_for(1)
    assert result == TicTacToe.Result.NOT_ENDED, result


def test_result_6():
    game = TicTacToe()
    game.play((2, 1))
    game.play((2, 2))
    game.play((1, 2))
    game.play((0, 2))

    result = game.get_result_for(0)
    assert result == TicTacToe.Result.NOT_ENDED, result

    result = game.get_result_for(1)
    assert result == TicTacToe.Result.NOT_ENDED, result


def test_result_7():
    game = TicTacToe()
    game.play((2, 1))
    game.play((2, 2))
    game.play((1, 0))
    game.play((0, 2))

    result = game.get_result_for(0)
    assert result == TicTacToe.Result.NOT_ENDED, result

    result = game.get_result_for(1)
    assert result == TicTacToe.Result.NOT_ENDED, result


def test_possible_actions_0():
    game = TicTacToe()
    game.play((0, 0))
    game.play((0, 2))
    game.play((1, 0))
    game.play((1, 2))
    game.play((2, 0))
    game.play((2, 1))

    actions = game.get_possible_actions()
    assert set(actions) == frozenset({(2, 2), (0, 1), (1, 1)}), actions


def test_possible_actions_1():
    game = TicTacToe()
    game.play((0, 0))
    game.play((0, 2))
    game.play((1, 0))
    game.play((1, 2))
    game.play((2, 1))
    game.play((2, 0))

    actions = game.get_possible_actions()
    assert set(actions) == frozenset({(2, 2), (0, 1), (1, 1)}), actions


def test_possible_actions_2():
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
