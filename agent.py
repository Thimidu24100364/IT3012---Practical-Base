# agent.py
class GreedyGridAgent:
    """A simple agent that tries to move around systematically to clear the grid."""

    def __init__(self):
        self.actions_pool = ['Up', 'Down', 'Left', 'Right']

    def sense_and_act(self, percept: dict) -> str:
        # If standing directly on food, or just wander / move towards coordinates
        pos = percept['agent_pos']
        # Simple heuristic or fallback random sweep
        return random.choice(self.actions_pool)

    #simple reflex agent 
    class SimpleReflexAgent:
        def sense_and_act(self, percept):

            #check whether the food is at the agent's current position
            if percept ['food_here']:
                return 'Up'

            #check whetther the wall directly inforn of the the agent
            if percept['wall_ahead']:
                return 'Right'

            return 'Up'