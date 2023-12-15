from collections import deque
from queue import PriorityQueue
from classes import *
from utils import *

# -------------------------------------------------------------------------------------------------

def astar_search(problem, heuristic):
    frontier = PriorityQueue() # priority = g(n) + h(n)
    start_node = Node(problem.initial_state, None, 0, heuristic(problem.initial_state, problem.goal_state))
    frontier.put(start_node)
    explored = set()
    node_distances = {}  # Dictionary to store g(n) and heuristic values for each node
    node_solutions = {} # Dictionary to store path to reach each node from the starting node

    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.state

        g_n = current_node.path_cost  # Save the g(n) value
        h_n = current_node.heuristic  # Save the heuristic value

        
        if problem.goal_test(current_state):
            path = current_node.path()
            return path, node_solutions, node_distances
        

        if current_state not in explored:
            explored.add(current_state)

            node_distances[current_state] = {'g(n)': g_n, 'h(n)': h_n} # Save g(cost) and heuristic values for the current node in the dictionary
            node_solutions[current_state] = current_node.path() # Save path to reach that node inside dictionary

            for next in problem.valid_next(current_state): # iterate over possible next states from the current state
                cost = current_node.path_cost + problem.step_cost(next)
                print(problem.step_cost(next))
                heuristic_value = heuristic(next, problem.goal_state)
                next_node = Node(next, current_node, cost, heuristic_value)
                print(next_node.state, cost)
                frontier.put(next_node)

    return None