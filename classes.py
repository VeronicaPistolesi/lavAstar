import time
from utils import *

class GridWorldProblem: # each cell in the grid is a state in the problem, and movements between cells are possible actions
    def __init__(self, grid, initial_state, goal_state, grid_colors):
        self.grid = grid # matrix
        self.grid_colors = grid_colors
        self.width = len(grid[0]) # rows
        self.height = len(grid) # columns
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.obstacles = {ord('-'), ord('|'), ord('}'), ord('r')}
    
    def valid_next(self, state): # returns a list of all valid next states
        x, y = state # get the coordinates of the current state
        possible_next_states = [(x, y-1), (x+1, y), (x, y+1), (x-1, y), (x+1, y-1), (x+1, y+1), (x-1, y+1), (x-1, y-1)] # N, E, S, W, NE, SE, SW, NW
        return [next for next in possible_next_states if self.is_valid(next)]
    
    def actions(self, state): # returns a list of valid actions that can be executed in the given state
        x, y = state # coordinates of the current state
        valid_next = self.valid_next(state)
        action_map = {
            (x, y-1): 0, # N
            (x+1, y): 1, # E
            (x, y+1): 2, # S
            (x-1, y): 3, # W
            (x+1, y-1): 4, # NE
            (x+1, y+1): 5, # SE
            (x-1, y+1): 6, # SW
            (x-1, y-1): 7 # NW
        }
        valid_dirs = [action_map[next] for next in valid_next] # creates a list, by mapping each valid neighboring state 
        return valid_dirs
    
    def result(self, state, action): # returns the state that results from executing the action in the given state (=the transition model)
        x, y = state
        action_map = {
            0: (x, y-1),  # N
            1: (x+1, y),  # E
            2: (x, y+1),  # S
            3: (x-1, y),   # W
            4: (x+1, y-1), # NE
            5: (x+1, y+1), # SE
            6: (x-1, y+1), # SW
            7: (x-1, y-1) # NW
        }

        next = action_map.get(action, state) # retrieve the next state based on the action
        return next if self.is_valid(next) else state

    def goal_test(self, state) -> bool: # returns True if state is the goal
        return state == self.goal_state

    def is_valid(self, state) -> bool: # returns true if the state is valid to step on
        x, y = state
        return 0 <= x < self.width and 0 <= y < self.height and self.grid[y][x] not in self.obstacles
 
    def step_cost(self, state): # assigns cost 1 to based on the terrain type
        x, y = state
        terrain_type = self.grid[y][x]
        terrain_color = self.grid_colors[y][x]

        if terrain_type == ord('.') and terrain_color == 6:  # ice cell
            return 3
        if (terrain_type == ord('.') and terrain_color == 7) or terrain_type == ord('>'):  # normal cell
            return 1
        else:
            return float('inf')  # default cost for other terrain types
    
    def update_grid(self, new_grid): # reassigns grid (dynamic)
        self.grid = new_grid
     
    def key_test(self, state) -> bool: # returns True if state is the key
        return state == self.key
    
#----------------------------------------------------------------------------
class Node: # consider the grid as a graph for search problem
    def __init__(self, state, parent, path_cost, heuristic=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
        self.heuristic = heuristic

    def path(self): # returns the list of nodes to reach this node from the root
        node, path_back = self, []
        while node.parent is not None:
            path_back.append(node.state)
            node = node.parent
        return list(reversed(path_back)) 

    def __lt__(self, other): # compare nodes in the queue based on their total cost (path cost + heuristic)
        return (self.path_cost + self.heuristic) < (other.path_cost + other.heuristic)
    
#----------------------------------------------------------------------------
class SimpleSearchAgent:
    def __init__(self, problem):
        self.problem = problem
        self.state = problem.initial_state
        self.seq = []

    def execution_time(self):
        return round(self._execution_time, 6)

class UninformedSearchAgent(SimpleSearchAgent):
    def __init__(self, problem):
        super().__init__(problem)

    def search(self, search_algorithm): # performs the search to find a sequence of actions using the specified algorithm
        start_time = time.time()
        self.seq = search_algorithm(self.problem)
        self._execution_time = time.time() - start_time
        return self.seq

class InformedSearchAgent(SimpleSearchAgent):
    def __init__(self, problem):
        super().__init__(problem)

    def search(self, search_algorithm, heuristic):
        start_time = time.time()
        self.seq, node_solutions, node_distances = search_algorithm(self.problem, heuristic) 
        self._execution_time = time.time() - start_time
        return self.seq, node_solutions, node_distances

class OnlineSearchAgent(SimpleSearchAgent):
    def __init__(self, problem):
        super().__init__(problem)
    
    def online_search(self, onsearch_algorithm, current_state, m, mode, he_type):
        action, next_state = onsearch_algorithm(self.problem, self.seq, current_state, m, mode, he_type)
        self.seq.append(current_state)
        return action, next_state