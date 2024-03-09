import copy

class BoardGame:
    def __init__(
            self,
            game_over_logic,
            make_move_logic,
            get_winner_logic,
            initialize_board_state,
            valid_moves_logic,
            players
        ):
        """
        Initializes the board game with necessary logic functions and player entities.

        :param game_over_logic: Function to determine if the game is over.
        :param make_move_logic: Function to apply a player's move to the board state.
        :param get_winner_logic: Function to determine the winner of the game.
        :param initialize_board_state: Function to initialize the board state.
        :param valid_moves_logic: Function to return the valid moves for the current player.
        :param players: List of Player instances representing the players of the game.
        """
        self.game_over_logic = game_over_logic
        self.make_move_logic = make_move_logic
        self.get_winner_logic = get_winner_logic
        self.initialize_board_state = initialize_board_state
        self.valid_moves_logic = valid_moves_logic
        self.players = players
        self.board_state = self.initialize_board_state()
        self.current_player_index = 0

    def is_game_over(self):
        """Checks if the game is over."""
        return self.game_over_logic(self.board_state)

    def play_turn(self, move):
        """Executes a turn for the current player."""
        self.board_state = self.make_move_logic(self.board_state, move, self.players[self.current_player_index].player_id)
        if self.is_game_over():
            return
        # Switch to the next player
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def get_winner(self):
        """Determines the winner of the game."""
        return self.get_winner_logic(self.board_state)

    def get_valid_moves(self):
        """Returns the valid moves for the current player."""
        return self.valid_moves_logic(self.board_state, self.players[self.current_player_index].player_id)

    def reset(self):
        """Resets the game to its initial state."""
        self.board_state = self.initialize_board_state()
        self.current_player_index = 0

    def simulate_move(self, move):
        """Simulates a move without altering the actual game state."""
        cloned_state = copy.deepcopy(self.board_state)
        simulated_state = self.make_move_logic(cloned_state, move, self.players[self.current_player_index].player_id)
        return simulated_state

    def clone_board_state(self, state):
        """Creates a deep copy of the board state."""
        return copy.deepcopy(state)

    def render(self):
        symbols = {0: '.', 1: 'X', 2: 'O'}
        for row in self.board_state:
            print(' '.join(symbols[cell] for cell in row))
        print()  # Add an empty line for better separation between moves
