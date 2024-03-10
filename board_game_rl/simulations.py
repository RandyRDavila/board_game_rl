
__all__ = ["simulate_game"]

def simulate_game(env, player1, player2):
    # Play the game until it's over.
    while not env.is_game_over():
        current_player = env.players[env.current_player_index]
        valid_moves = env.get_valid_moves()
        selected_move = current_player.choose_move(env.board_state, valid_moves)
        env.play_turn(selected_move)
        env.render()

    # After the game is over, determine the outcome.
    winner = env.get_winner()
    if winner == 0:
        print("The game is a draw.")
    elif winner is not None:
        print(f"Player {winner} wins!")
    else:
        print("Unexpected outcome.")