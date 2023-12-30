from collections import deque
from queue import PriorityQueue
from classes import *
from utils import *

def breadth_first_search(problem):
    frontier = PriorityQueue() 
    start_node = Node(problem.initial_state, None, 0)
    frontier.put(start_node)
    explored = set()

    while frontier: # until the frontier is not empty
        current_node = frontier.get() # remove and returns the first state in the queue 
        current_state = current_node.state

        if problem.goal_test(current_state):
            path = current_node.path() 
            return path

        if current_state not in explored:
            explored.add(current_state)
            
            for next in problem.valid_next(current_state): # iterate over possible next states from the current state
                next_node = Node(next, current_node, 0)
                frontier.put(next_node) # enques the next state and the updated path to the frontier
                
    return None

# -------------------------------------------------------------------------------------------------

def uniform_cost_search(problem): #dijkstra
    frontier = PriorityQueue() 
    start_node = Node(problem.initial_state, None, 0)
    frontier.put(start_node)  # add initial state of the problem with cost 0, [] is the path taken so far (beginning it is empty)
    explored = set()
    node_distances = {}  # Dictionary to store g(n) and heuristic values for each node

    while not frontier.empty():     # explore path until frontier is empty (consider all possible paths)
        current_node = frontier.get()
        current_state = current_node.state

        g_n = current_node.path_cost  # Save the g(n) value

        if problem.goal_test(current_state): # check if current state is goal, if yes: return path
            path = current_node.path() 
            return path, node_distances

        if current_state not in explored:
            #explore the neighbours of current state, calculate the cost of reaching each neighbour and add them to the frontier with updated cost 
            explored.add(current_state)

            node_distances[current_state] = {'g(n)': g_n} # Save g(cost) for the current node in the dictionary
            #print(node_distances, node_distances[current_state])

            for next in problem.valid_next(current_state):
                #next_state = problem.result(current_state, action)
                cost = current_node.path_cost + problem.step_cost(next)
                next_node = Node(next, current_node, cost)
                frontier.put(next_node)

    return None    # None, if no solution is found

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
                # print(problem.step_cost(next))
                heuristic_value = heuristic(next, problem.goal_state)
                next_node = Node(next, current_node, cost, heuristic_value)
                # print(next_node.state, cost)
                frontier.put(next_node)

    return None

# -------------------------------------------------------------------------------------------------

def greedy_best_first_search(problem, heuristic):
    frontier = PriorityQueue()
    start_node = Node(problem.initial_state, None, 0, heuristic(problem.initial_state, problem.goal_state))
    frontier.put(start_node)
    explored = set()
    node_distances = {}  # Dictionary to store g(n) and heuristic values for each node
    node_solutions = {} # Dictionary to store path to reach each node from the starting node

    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.state

        h_n = current_node.heuristic  # Save the heuristic value

        if problem.goal_test(current_state):
            path = current_node.path()
            return path, node_solutions, node_distances

        if current_state not in explored:
            explored.add(current_state)

            node_distances[current_state] = {'h(n)': h_n} # Save heuristic value for the current node in the dictionary
            node_solutions[current_state] = current_node.path() # Save path to reach that node inside dictionary

            for next in problem.valid_next(current_state):
                heuristic_value = heuristic(next, problem.goal_state)
                next_node = Node(next, current_node, 0, heuristic_value)
                frontier.put(next_node)

    return None

# -------------------------------------------------------------------------------------------

def onlineAStar(problem, current_state):
    H = {}
    if problem.goal_test(current_state):
        return
    else:
        valid_actions = problem.actions(current_state)

        for action in valid_actions:
            next_state = problem.result(current_state, action)
            cost_so_far = problem.step_cost(next_state)
            heuristic_cost = euclidean_distance(next_state, problem.goal_state)

            #monster = find_state_coord(problem.grid, ord('a'))
            #heuristic_cost = heuristic_dyn(next_state, problem.goal_state, monster) # TRIAL

            total_cost = cost_so_far + heuristic_cost
            H[action] = total_cost

        best_action = min(H, key=H.get) # Finds most efficient action
        next_state = problem.result(current_state, best_action) # Calculates next state

        print(f"Selected action: {best_action}, Total cost: {H[best_action]}")
        return best_action, next_state
    
# -------------------------------------------------------------------------------------------

def onlineGreedy(problem, current_state):
    H = {}
    if problem.goal_test(current_state):
        return
    else:
        valid_actions = problem.actions(current_state)

        for action in valid_actions:
            next_state = problem.result(current_state, action)
            #heuristic_cost = euclidean_distance(next_state, problem.goal_state)

            monster = find_state_coord(problem.grid, ord('a'))
            heuristic_cost = heuristic_dyn(next_state, problem.goal_state, monster)

            total_cost = heuristic_cost
            H[action] = total_cost

        best_action = min(H, key=H.get) # Finds most efficient action
        next_state = problem.result(current_state, best_action) # Calculates next state

        #print(f"Selected action: {best_action}, Total cost: {H[best_action]}")
        return best_action, next_state