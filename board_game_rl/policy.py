import random

__all__ = ["random_policy"]

def random_policy(board_state, valid_moves):
    """
    Selects a move randomly from the list of valid moves.

    :param board_state: The current state of the board (not used in this policy).
    :param valid_moves: A list of valid moves the player can make.
    :return: A randomly selected move.
    """
    return random.choice(valid_moves)
