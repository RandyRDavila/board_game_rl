import random
from board_game_rl.policy import minimax_policy, random_policy
from board_game_rl.player import Player


# RandomPlayer class, leveraging the random policy for move selection
class RandomPlayer(Player):
    def __init__(self, player_id):
        super().__init__(player_id, policy=random_policy)


class MinimaxPlayer(Player):
    def __init__(self, player_id):
        super().__init__(player_id, policy=None)  # Policy will be set in choose_move directly

    def choose_move(self, board_state, valid_moves):
        return minimax_policy(board_state, valid_moves, self.player_id)