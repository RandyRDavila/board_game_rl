def initialize_board_state_logic():
    return [[0 for _ in range(3)] for _ in range(3)]

def game_over_logic(board_state):
    # Check for a win
    for player_id in [1, 2]:
        # Check rows, columns, and diagonals for a win
        if any(all(cell == player_id for cell in row) for row in board_state) or \
           any(all(row[i] == player_id for row in board_state) for i in range(3)) or \
           all(board_state[i][i] == player_id for i in range(3)) or \
           all(board_state[i][2-i] == player_id for i in range(3)):
            return True
    # Check for a draw (board is full)
    return all(cell != 0 for row in board_state for cell in row)

def make_move_logic(board_state, move, player_id):
    if board_state[move[0]][move[1]] == 0:
        board_state[move[0]][move[1]] = player_id
    return board_state

def get_winner_logic(board_state):
    for player_id in [1, 2]:
        # Check rows, columns, and diagonals for a win
        if any(all(cell == player_id for cell in row) for row in board_state) or \
           any(all(row[i] == player_id for row in board_state) for i in range(3)) or \
           all(board_state[i][i] == player_id for i in range(3)) or \
           all(board_state[i][2-i] == player_id for i in range(3)):
            return player_id
    # If no winner, check for a draw
    if all(cell != 0 for row in board_state for cell in row):
        return 0  # 0 can indicate a draw
    return None  # Game is not over yet

def valid_moves_logic(board_state, _):
    return [(i, j) for i in range(3) for j in range(3) if board_state[i][j] == 0]
