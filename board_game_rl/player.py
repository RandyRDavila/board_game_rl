import random

__all__ = ["Player"]

class Player:
    def __init__(self, player_id, policy=None):
        self.player_id = player_id
        self.policy = policy

    def choose_move(self, board_state, valid_moves):
        """
        Selects a move based on the current policy.

        :param board_state: The current state of the board.
        :param valid_moves: A list of valid moves the player can make.
        :return: The move selected by the policy.
        """
        if self.policy is None:
            raise NotImplementedError("A policy function must be defined.")
        return self.policy(board_state, valid_moves)

    @staticmethod
    def default_policy(board_state, valid_moves):
        """
        Default policy function for a player, which can be overridden by setting self.policy_function.

        :param board_state: The current state of the board.
        :param valid_moves: A list of valid moves the player can make.
        :return: A selected move from the list of valid moves.
        """
        # Implement a basic or random selection strategy as a placeholder
        return random.choice(valid_moves) if valid_moves else None

    def set_policy(self, new_policy_function):
        """
        Updates the player's policy function.

        :param new_policy_function: The new policy function to be used for decision-making.
        """
        self.policy_function = new_policy_function
