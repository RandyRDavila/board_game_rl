from .board_classes import GameBoard, Player

class GameEnv:
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
        return self.game_board, self.done

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
