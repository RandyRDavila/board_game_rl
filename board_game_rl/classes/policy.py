import random

# Before defining policies. We first need to define a callable V(s) table and Q(s, a) table class.
# These tables are used to store the value of a state and the value of a state-action pair.
# The following is a simple V(s) table that takes a state and returns the value of the state.
class Table:
    """
    A VTable is a callable that takes a state and returns the value of the state.
    """
    def __init__(self, value_dictionary):
        self.mapping = value_dictionary
        if len(self.mapping.keys()[0]) == 1:
            self.v = True
        elif len(self.mapping.keys()[0]) == 2:
            self.q = True
        else:
            raise ValueError("The table is neither a V-table nor a Q-table.")

    def __call__(self, state, action=None):
        return self.mapping[state] if action is None else self.mapping[state, action]

    def __repr__(self):
        return self.mapping.__name__

# In this script we implement a general policy class that can be used for
# simple random policies, tabular policies, minimax policies, mcts policies,
# and neural network policies. A policy is always a callable that takes a environment
# state (board) and returns a move.

# The following Policy is a superclass of all other policies.
class Policy:
    """
    A policy is a callable that takes a board and returns a move.
    """
    def __init__(self, mapping):
        self.mapping = mapping

    def __call__(self, board):
        return self.mapping(board)

    def __repr__(self):
        return self.mapping.__name__


# The following is a simple random policy that takes a board and returns a random move.
class RandomPolicy(Policy):
    """
    A tabular policy that takes a board and returns the greedy move with respect to a Q-table.
    """
    def __init__(self):
        super().__init__(self.random_policy)

    # The following is a simple random policy that takes a board and returns a random move.
    def random_policy(board):
        """
        A random policy that takes a board and returns a random move.

        Args:
        board (np.ndarray): The game board.

        Returns:
        tuple: A random move.
        """
        return random.choice(board.valid_moves())


# The following is a simple tabular policy that takes a board and returns the greedy move with
# respect to a Q-table. This is greedy with respect to state-action values.
class TabularPolicy(Policy):
    """
    A tabular policy that takes a board and returns the greedy move with respect to a Q-table.
    """
    def __init__(self, table, q_values=False):
        super().__init__(self.greedy)
        self.table = table
        self.q_values = q_values

    def greedy(self, board):
        """
        A greedy policy that takes a board and returns the greedy move with respect to a Q-table.

        Args:
        board (np.ndarray): The game board.

        Returns:
        tuple: The greedy move.
        """
        moves = board.valid_moves()
        if self.q_values:
            values = [self.table(board, move) for move in moves]
        else:
            values = [self.table(board) for move in moves]
        return moves[values.index(max(values))]









