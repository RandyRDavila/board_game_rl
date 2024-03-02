from .board_classes import Player, Agent
from .example_policies.random_policy import random_policy
import numpy as np

def play_simulated_random_game(board:np.ndarray, render=False) -> None:
    """
    Play a random game on the board.

    Args:
    board: np.ndarray
    render: bool

    Returns:
    None
    """
    # Reset the board to begin the game.
    board.reset()

    # Render the board if requested.
    if render:
        board.render()

    # Define the two agents.
    agentA = Agent(Player.A, random_policy)
    agentB = Agent(Player.B, random_policy)

    # Play the game.
    while True:
        # Agent A plays first.
        move = agentA(board)

        # Agent A plays the move.
        board(agentA.player, move)

        # Render the board if requested.
        if render:
            board.render()

        # Check if the game is over.
        if board.game_over():
            print("Game Over")
            if board.winner() == Player.none:
                print("Draw")
            else:
                print("Winner: ", board.winner())
            return None

        # Agent B plays second.
        move = agentB(board)

        # Agent B plays the move.
        board(agentB.player, move)

        # Render the board if requested.
        if render:
            board.render()

        # Check if the game is over.
        if board.game_over():
            print("Game Over")
            if board.winner() == Player.none:
                print("Draw")
            else:
                print("Winner: ", board.winner())
            return None

def play_against_random_agent(board:np.ndarray, agent:Agent, render=False, start=True) -> None:
    """
    Play a game on the board with two agents.

    Args:
    board: np.ndarray
    agentA: Agent
    agentB: Agent
    render: bool

    Returns:
    None
    """
    # Reset the board to begin the game.
    board.reset()

    # Render the board if requested.
    if render:
        board.render()

    # Assign the agents.
    if start:
        agentA = agent
        current_agent = agentA
        agentB = Agent(Player.B, random_policy)
    else:
        agentB = agent
        current_agent = agentB
        agentA = Agent(Player.A, random_policy)

    # Play the game.
    while True:
        # Current agent makes a move.
        move = current_agent(board)
        board(current_agent.player, move)

        # Render the board if requested.
        if render:
            board.render()

        # Check if the game is over.
        if board.game_over():
            print("Game Over")
            if board.winner() == Player.none:
                print("Draw")
            else:
                print("Winner: ", board.winner())
            break

        # Switch agents.
        current_agent = agentA if current_agent == agentB else agentB


def play_two_player_game(board: np.ndarray, agentA: Agent, agentB: Agent, render=False) -> None:
    """
    Play a game on the board with two agents.

    Args:
    board: np.ndarray
    agentA: Agent
    agentB: Agent
    render: bool

    Returns:
    None
    """
    # Reset the board to begin the game.
    board.reset()

    # Render the board if requested.
    if render:
        board.render()

    # Play the game.
    current_agent = agentA
    while True:
        # Current agent makes a move.
        move = current_agent(board)
        board(current_agent.player, move)

        # Render the board if requested.
        if render:
            board.render()

        # Check if the game is over.
        if board.game_over():
            print("Game Over")
            if board.winner() == Player.none:
                print("Draw")
            else:
                print("Winner: ", board.winner())
            break

        # Switch agents.
        current_agent = agentA if current_agent == agentB else agentB
