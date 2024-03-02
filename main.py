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
    state, reward, done = env.step(bgrl.Player.A, moveA)
    print(f"agentA Reward: {reward}")
    env.render()
    if done:
        break
    moveB = agentB(env.game_board)
    state, reward, done = env.step(bgrl.Player.B, moveB)
    print(f"agentB Reward: {reward}")
    env.render()

print(f"The winner is {env.winner}")
