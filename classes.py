import time
from utils import *

class GridWorldProblem: #Each cell in the grid is a state in the problem, and movements between cells are possible actions
    def init(self, grid, initial_state, goal_state, grid_colors):
        self.grid = grid # matrix
        self.grid_colors = grid_colors
        self.width = len(grid[0]) # rows
        self.height = len(grid) # columns
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.obstacles = {ord('-'), ord('|'), ord('}'), ord('d')}
    
    def valid_next(self, state): #Returns a list of all valid next states
        x, y = state
        possible_next_states = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] #E W S N
        return [next for next in possible_next_states if self.is_valid(next)]
    
    def actions(self, state): # Returns a list of valid actions that can be executed in the given state
        x, y = state
        valid_next = self.valid_next(state)
        action_map = {
            (x, y-1): 0, #N
            (x+1, y): 1, #E
            (x, y+1): 2, #S
            (x-1, y): 3 #W
        }
        #possible_next_states = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] #E W S N
        #valid_next = [next for next in possible_next_states if self.is_valid(next)]
        valid_dirs = [action_map[next] for next in valid_next]
        return valid_dirs
    
#----------------------------------------------------------------------------
class Node: #We consider the grid as a graph for our search problem
    def init(self, state, parent, path_cost, heuristic=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
        self.heuristic = heuristic

    def path(self): #Returns the list of nodes to reach this node from the root
        node, path_back = self, []
        while node.parent is not None:
            path_back.append(node.state)
            node = node.parent
        return list(reversed(path_back))

    def lt(self, other): # Compare nodes in the queue based on their total cost (path cost + heuristic)
        return (self.path_cost + self.heuristic) < (other.path_cost + other.heuristic)