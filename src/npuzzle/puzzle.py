from .solver import solve_puzzle

class NPuzzle:
    def __init__(self, initial_state):
        """
        Initialize the N-puzzle with the given initial state
        initial_state is a 2D list representing the puzzle
        """
        self.initial_state = initial_state
        self.n = len(initial_state)
        self.goal_state = self._create_goal_state()
        
    def _create_goal_state(self):
        """
        Create the goal state based on the puzzle size
        Numbers will be in ascending order, with blank space at the end
        """
        goal = []
        total_nums = self.n * self.n
        current_num = 1
        
        for i in range(self.n):
            row = []
            for j in range(self.n):
                if current_num < total_nums:
                    row.append(current_num)
                    current_num += 1
                else:
                    row.append(' ')
            goal.append(row)
        
        return goal

    def solve(self):
        """
        Solve the puzzle using A* search algorithm
        """
        return solve_puzzle(self.initial_state, self.goal_state, self.n)
