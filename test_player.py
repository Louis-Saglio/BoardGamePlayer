from player import analyse_node_for, get_game_tree, ActionNode
from tictactoe import TicTacToe


def test_analyse_node_for():
    game = TicTacToe()
    game.play((0, 0))
    game.play((1, 0))
    game.play((0, 1))
    game.play((1, 1))
    game.play((0, 2))

    analyse_node_for(get_game_tree(game), game.players[0])


def test_get_first_final_child():
    f = ActionNode(0, None, None, None)
    g = ActionNode(0, None, None, f)
    h = ActionNode(0, None, None, g)
    assert f.get_first_final_child() is h
