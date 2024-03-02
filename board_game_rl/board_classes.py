import enum
import numpy as np

class Player(enum.Enum):
    """
    A player is an enum class that contains the values of the players in the game.
    """
    A = 1.0
    B = -1.0
    none = 0.0

class Agent:
    """
    An agent is a player (class) with a policy (callable). The policy is a function
    that takes a board and returns a move. The agent is a callable that takes a board
    and returns a move.

    Args:
    player: Player
    policy: callable

    Methods:
    __call__(self, board: np.ndarray) -> tuple
    __repr__(self) -> Player

    Example:
    ```python
    >>> from policies import random_policy
    >>> from board_classes import Agent, Player
    >>> agentA = Agent(Player.A, random_policy)
    >>> move = agentA(board)
    ```
    """
    def __init__(self, player: Player, policy: callable):
        self.player = player
        self.policy = policy

    def __call__(self, board: np.ndarray) -> tuple:
        return self.policy(board, self.player)

    def __repr__(self) -> Player:
        return self.player

class GameBoard:
    """
    A game board is a class that contains the logic of a game. The logic is a dictionary
    of functions that define the game. The game board is a callable that takes a player
    and a move and returns the new board.

    Args:
    logic: dict[str, callable]

    Methods:
    reset(self) -> tuple
    render(self) -> None
    winner(self) -> Player
    valid_moves(self, player=None) -> list[tuple[int, int]]
    draw(self) -> bool
    game_over(self) -> bool
    play(self, player, move, mutate=True) -> np.ndarray
    __call__(self, player, move) -> np.ndarray
    __repr__(self) -> str

    Example:
    ```python
    >>> from tictactoe_logic import tictactoe_logic
    >>> board = GameBoard(tictactoe_logic)
    >>> board.reset()
    >>> board.render()
    >>> board.winner()
    >>> board.valid_moves()
    >>> board.draw()
    >>> board.game_over()
    >>> board.play(Player.A, (0, 0))
    >>> board(Player.B, (1, 1))
    >>> board
    ```
    """
    def __init__(self, logic: dict[str, callable]):
        self.logic = logic

    ########################### Logic Methods ###########################
    def reset(self) -> tuple:
        self.board = self.logic["board"].copy()
        return self.board, False

    def render(self) -> None:
        return self.logic["render"](self.board)

    def winner(self) -> Player:
        return self.logic["winner"](self.board)

    def valid_moves(self, player=None) -> list[tuple[int, int]]:
        return self.logic["valid_moves"](self.board, player=player)

    def play(self, player, move, mutate=True) -> np.ndarray:
        return self.logic["play"](self.board, player, move, mutate=mutate)

    ########################### Derived Game Methods ###########################

    def draw(self) -> bool:
        return len(self.valid_moves()) == 0 and self.winner() == Player.none

    def game_over(self) -> bool:
        return self.winner() != Player.none or self.draw()

    ############################# Magic Methods ###########################

    def __call__(self, player, move) -> np.ndarray:
        return self.play(player, move, mutate=True)

    def __repr__(self) -> str:
        return self.board.__repr__()

class BoardGameEnv:
    def __init__(self, game_logic):
        """
        Initialize the board game environment with the specific game logic.

        Args:
        game_logic (dict): A dictionary containing the game logic functions.
        """
        self.game_board = GameBoard(game_logic)
        self.done = False
        self.winner = Player.none

    def reset(self):
        """
        Reset the environment to the initial state and returns the initial board state.

        Returns:
        np.ndarray: The initial state of the board.
        """
        self.game_board.reset()
        self.done = False
        self.winner = Player.none
        return self.game_board.board

    def step(self, player, move):
        """
        Take a step in the environment by executing the move for the given player.

        Args:
        player (Player): The player making the move.
        move (tuple): The move being made.

        Returns:
        tuple: A tuple containing the new state of the board, the reward, and a boolean indicating if the game is over.
        """
        if self.done:
            raise ValueError("The game is over. Please reset the environment.")

        new_state = self.game_board.play(player, move)

        # Check if the game is over and update the winner
        if self.game_board.game_over():
            self.done = True
            self.winner = self.game_board.winner()

        # Define the reward mechanism
        reward = self.calculate_reward(player)

        return new_state, reward, self.done

    def calculate_reward(self, player):
        """
        Calculate the reward for the given player.

        Args:
        player (Player): The player for whom to calculate the reward.

        Returns:
        float: The calculated reward.
        """
        if not self.done:
            return 0  # No reward if the game is not over.
        if self.winner == player:
            return 1  # Reward for winning.
        elif self.winner == Player.none:
            return 0.5  # Reward for a draw.
        else:
            return -1  # Penalty for losing.

    def render(self):
        """
        Render the current state of the board.
        """
        self.game_board.render()
