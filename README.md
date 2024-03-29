# board_game_rl

`board_game_rl` is a Python package designed for creating and simulating reinforcement learning environments for board games. It provides a flexible framework for defining game logic, players, and agents, with a focus on ease of use and extensibility.

## Features

- Modular design for easy definition and simulation of board games.
- Includes example implementations, such as Tic-Tac-Toe, to get started quickly.
- Supports custom game logic and policies for advanced simulations.

## Installation

Clone or Download the Repository: First, you need to clone your repository or download the source code as a ZIP archive and extract it.

If cloning:

```bash
git clone https://github.com/RandyRDavila/board_game_rl.git
cd board_game_rl
```

Install Using pip: Inside the root directory of the project (where setup.py is located), run:

```bash
pip install .
```

This command tells `pip` to install the package from the current directory. It automatically manages the build and installation process.

Ensure you have Python 3.6 or newer installed.

## Quick Start

Here's a quick example to get you started with `board_game_rl`:
```python
from board_game_rl import GameBoard
from board_game_rl.example_logic import tictactoe_logic
from board_game_rl.example_policies import random_policy
from board_game_rl.board_classes import Agent, Player

# Initialize the game board with Tic-Tac-Toe logic
game_board = GameBoard(tictactoe_logic)

# Create two agents with random policies
agentA = Agent(Player.A, random_policy)
agentB = Agent(Player.B, random_policy)

# Play a game
game_board.play_game(agentA, agentB, render=True)
```

To play a game as if it were a reinforcement learning environment, see the following code:

```python
import board_game_rl as bgrl

# Create a game board.
env = bgrl.GameEnv(bgrl.tictactoe_logic)

# Simulate a random game with the GameEnv class.

# Create an agent with a random policy.
agentA = bgrl.Agent(bgrl.Player.A, bgrl.random_policy)
agentB = bgrl.Agent(bgrl.Player.B, bgrl.random_policy)

# Play a game between two agents.
state, done = env.reset()
env.render()

while not done:
    moveA = agentA(env.game_board)
    state, reward, done = env.step(agentA, moveA)
    print(f"agentA Reward: {reward}")
    env.render()
    if done:
        break
    moveB = agentB(env.game_board)
    state, reward, done = env.step(agentB, moveB)
    print(f"agentB Reward: {reward}")
    env.render()

print(f"The winner is {env.winner}")

```

## Features

* Flexible game board implementation.
* Example game logic for Tic-Tac-Toe.
* Support for custom policies and agents.

## Author
Randy R. Davila, PhD.

## License

`board_game_rl` is licensed under the MIT License.