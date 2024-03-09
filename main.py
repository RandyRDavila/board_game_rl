from board_game_rl.board import BoardGame
from board_game_rl.agent_players import RandomPlayer
from board_game_rl.policy import minimax_policy, random_policy
from board_game_rl.player import Player
from board_game_rl.simulations import simulate_game
from board_game_rl.tictactoe_logic import *
import copy

# Assuming the Player and BoardGame classes are already defined as previously discussed
# and TicTacToe logic functions are defined as per the last instructions

# Create two players with random policies
# player1 = RandomPlayer(player_id=1)
# player2 = RandomPlayer(player_id=2)


# Initialize the TicTacToe game with the defined logic functions and players
# env = BoardGame(
#     game_over_logic=game_over_tictactoe_logic,
#     make_move_logic=make_move_tictactoe_logic,
#     get_winner_logic=get_winner_tictactoe_logic,
#     initialize_board_state=initialize_tictactoe_board_state_logic,
#     valid_moves_logic=valid_moves_tictactoe_logic,
#     players=[player1, player2]
# )

#

# RandomPlayer class, leveraging the random policy for move selection
class RandomPlayer(Player):
    def __init__(self, player_id):
        super().__init__(player_id, policy=random_policy)

def minimax(board, depth, is_maximizing, player_id, opponent_id):
    winner_logic = get_winner_tictactoe_logic(board)
    if winner_logic == player_id:
        return 10
    elif winner_logic == opponent_id:
        return -10
    elif get_winner_tictactoe_logic(board):  # Assuming this checks for a draw
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in valid_moves_tictactoe_logic(board, player_id):
            # Simulate the move
            new_board = make_move_tictactoe_logic(board, move, player_id)
            score = minimax(new_board, depth + 1, False, player_id, opponent_id)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in valid_moves_tictactoe_logic(board, opponent_id):
            # Simulate the move
            new_board = make_move_tictactoe_logic(board, move, opponent_id)
            score = minimax(new_board, depth + 1, True, player_id, opponent_id)
            best_score = min(score, best_score)
        return best_score

def minimax_policy(board_state, valid_moves, player_id=1):
    opponent_id = 2 if player_id == 1 else 1
    best_score = -float('inf')
    best_move = None
    for move in valid_moves:
        # Simulate the move
        new_board = make_move_tictactoe_logic(copy.deepcopy(board_state), move, player_id)
        score = minimax(new_board, 0, False, player_id, opponent_id)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

class MinimaxPlayer(Player):
    def __init__(self, player_id):
        super().__init__(player_id, policy=None)  # Policy will be set in choose_move directly

    def choose_move(self, board_state, valid_moves):
        return minimax_policy(board_state, valid_moves, self.player_id)


# Set up the game
player1 = MinimaxPlayer(1)
player2 = RandomPlayer(2)  # Assuming RandomPlayer is defined as before
players = [player1, player2]


# Initialize and run the game as before
# Initialize the TicTacToe game with the defined logic functions and players
# Initialize the TicTacToe game with the defined logic functions and players
env = BoardGame(
    game_over_logic=game_over_tictactoe_logic,
    make_move_logic=make_move_tictactoe_logic,
    get_winner_logic=get_winner_tictactoe_logic,
    initialize_board_state=initialize_tictactoe_board_state_logic,
    valid_moves_logic=valid_moves_tictactoe_logic,
    players=[player1, player2]
)

env.reset()
simulate_game(env, player1, player2)

# # # Play the game until it's over
# while not env.is_game_over():
#     current_player = env.players[env.current_player_index]
#     valid_moves = env.get_valid_moves()
#     selected_move = current_player.choose_move(env.board_state, valid_moves)
#     env.play_turn(selected_move)
#     env.render()
# env.render()

# # After the game is over, determine the outcome
# winner = env.get_winner()
# if winner == 0:
#     print("The game is a draw.")
# elif winner is not None:
#     print(f"Player {winner} wins!")
# else:
#     print("Unexpected outcome.")


