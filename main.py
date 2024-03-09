from board_game_rl.board import BoardGame
from board_game_rl.agent_players import RandomPlayer
from board_game_rl.policy import minimax_policy
from board_game_rl.player import Player
from board_game_rl.simulations import simulate_game
from board_game_rl.tictactoe_logic import *

# Assuming the Player and BoardGame classes are already defined as previously discussed
# and TicTacToe logic functions are defined as per the last instructions

# Create two players with random policies
player1 = RandomPlayer(player_id=1)
player2 = RandomPlayer(player_id=2)


# Initialize the TicTacToe game with the defined logic functions and players
env = BoardGame(
    game_over_logic=game_over_tictactoe_logic,
    make_move_logic=make_move_tictactoe_logic,
    get_winner_logic=get_winner_tictactoe_logic,
    initialize_board_state=initialize_tictactoe_board_state_logic,
    valid_moves_logic=valid_moves_tictactoe_logic,
    players=[player1, player2]
)



simulate_game(env, player1, player2)



