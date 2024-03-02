import board_game_rl as bgrl

# Create a game board.
board = bgrl.GameBoard(bgrl.tictactoe_logic)

# Simulate a random game.
bgrl.play_simulated_random_game(board, render=True)

