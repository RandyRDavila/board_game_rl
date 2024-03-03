import enum

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
    """
    def __init__(self, player: Player, policy: callable):
        self.player = player
        self.policy = policy
        self.value = self.player.value

    def __call__(self, env) -> tuple:
        return self.policy(env, self.player)

    def __repr__(self) -> Player:
        return self.player
