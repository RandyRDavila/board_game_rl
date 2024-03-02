import board_game_rl as bgrl

# Create a game board.
board = bgrl.GameEnv(bgrl.tictactoe_logic)

# Simulate a random game with the GameEnv class.

# Create an agent with a random policy.
agentA = bgrl.Agent(bgrl.Player.A, bgrl.random_policy)
agentB = bgrl.Agent(bgrl.Player.B, bgrl.random_policy)

# Play a game between two agents.
state, done = board.reset()
board.render()

while not done:
    moveA = agentA(board.game_board)
    state, reward, done = board.step(bgrl.Player.A, moveA)
    print(f"agentA Reward: {reward}")
    board.render()
    if done:
        break
    moveB = agentB(board.game_board)
    state, reward, done = board.step(bgrl.Player.B, moveB)
    print(f"agentB Reward: {reward}")
    board.render()

print(f"The winner is {board.winner}.")


