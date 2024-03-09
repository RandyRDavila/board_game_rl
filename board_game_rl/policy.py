import random
import copy


def random_policy(board_state, valid_moves):
    """
    Selects a move randomly from the list of valid moves.

    :param board_state: The current state of the board (not used in this policy).
    :param valid_moves: A list of valid moves the player can make.
    :return: A randomly selected move.
    """
    return random.choice(valid_moves)


def minimax(board, depth, is_maximizing, player_id, opponent_id):
    winner_logic = board.get_winner_logic(board)
    if winner_logic == player_id:
        return 10
    elif winner_logic == opponent_id:
        return -10
    elif board.game_over_logic(board):  # Assuming this checks for a draw
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in board.valid_moves_logic(board, player_id):
            # Simulate the move
            new_board = board.make_move_logic(board, move, player_id)
            score = minimax(new_board, depth + 1, False, player_id, opponent_id)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for move in board.valid_moves_logic(board, opponent_id):
            # Simulate the move
            new_board = board.make_move_logic(board, move, opponent_id)
            score = minimax(new_board, depth + 1, True, player_id, opponent_id)
            best_score = min(score, best_score)
        return best_score

def minimax_policy(board_state, valid_moves, player_id=1):
    opponent_id = 2 if player_id == 1 else 1
    best_score = -float('inf')
    best_move = None
    for move in valid_moves:
        # Simulate the move
        new_board = board_state.make_move_logic(copy.deepcopy(board_state), move, player_id)
        score = minimax(new_board, 0, False, player_id, opponent_id)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move
