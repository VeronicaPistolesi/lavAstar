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

def uniform_cost_search(problem): 
    frontier = PriorityQueue() 
    start_node = Node(problem.initial_state, None, 0)
    frontier.put(start_node)  # add initial state of the problem with cost 0, [] is the path taken so far (beginning it is empty)
    explored = set()


    while not frontier.empty(): # explore path until frontier is empty (consider all possible paths)
        current_node = frontier.get()
        current_state = current_node.state

        if problem.goal_test(current_state): # check if current state is goal, if yes: return path
            path = current_node.path() 
            return path 

        if current_state not in explored:
            explored.add(current_state)

            for next in problem.valid_next(current_state):
                cost = current_node.path_cost + problem.step_cost(next)
                next_node = Node(next, current_node, cost) # update the path cost
                frontier.put(next_node)

    return None    # no solution found

# -------------------------------------------------------------------------------------------------

def astar_search(problem, heuristic):
    frontier = PriorityQueue() # priority = g(n) + h(n)
    start_node = Node(problem.initial_state, None, 0, heuristic(problem.initial_state, problem.goal_state))
    frontier.put(start_node)
    explored = set()
    node_distances = {} # dictionary to store g(n) and heuristic values for each node
    node_solutions = {} # dictionary to store path to reach each node from the starting node

    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.state

        g_n = current_node.path_cost  # save the g(n) value
        h_n = current_node.heuristic  # save the heuristic value

        
        if problem.goal_test(current_state):
            path = current_node.path()
            return path, node_solutions, node_distances
        

        if current_state not in explored:
            explored.add(current_state)

            node_distances[current_state] = {'g(n)': g_n, 'h(n)': h_n} # save g(cost) and heuristic values for the current node in the dictionary
            node_solutions[current_state] = current_node.path() # save path to reach that node inside dictionary

            for next in problem.valid_next(current_state): # iterate over possible next states from the current state
                cost = current_node.path_cost + problem.step_cost(next)
                heuristic_value = heuristic(next, problem.goal_state)
                next_node = Node(next, current_node, cost, heuristic_value)
                frontier.put(next_node)

    return None

# -------------------------------------------------------------------------------------------------

def greedy_best_first_search(problem, heuristic):
    frontier = PriorityQueue()
    start_node = Node(problem.initial_state, None, 0, heuristic(problem.initial_state, problem.goal_state))
    frontier.put(start_node)
    explored = set()
    node_distances = {} # dictionary to store g(n) and heuristic values for each node
    node_solutions = {} # dictionary to store path to reach each node from the starting node

    while not frontier.empty():
        current_node = frontier.get()
        current_state = current_node.state

        h_n = current_node.heuristic  # save the heuristic value

        if problem.goal_test(current_state):
            path = current_node.path()
            return path, node_solutions, node_distances

        if current_state not in explored:
            explored.add(current_state)

            node_distances[current_state] = {'h(n)': h_n} # save heuristic value for the current node in the dictionary
            node_solutions[current_state] = current_node.path() # save path to reach that node inside dictionary

            for next in problem.valid_next(current_state):
                heuristic_value = heuristic(next, problem.goal_state)
                next_node = Node(next, current_node, 0, heuristic_value)
                frontier.put(next_node)

    return None

# -------------------------------------------------------------------------------------------

def onlineMode(problem, seq, current_state, m, mode, he_type):

    if is_dead_end(problem, current_state, seq): # if it is dead end, backtrack
        valid_actions = problem.actions(current_state)
        best_action, next_state = backtrack(problem, current_state, valid_actions, seq)
        return best_action, next_state

    if current_state in seq: 
        valid_actions = [action for action in problem.actions(current_state) if problem.result(current_state, action) not in seq] # removes actions that lead to already visited states
        best_action, next_state = select_best_action(problem, current_state, valid_actions, m, mode, he_type)
        return best_action, next_state
        
    else: 
        valid_actions = problem.actions(current_state)
        best_action, next_state = select_best_action(problem, current_state, valid_actions, m, mode, he_type)
        return best_action, next_state
        

def select_best_action(problem, current_state, valid_actions, m, mode, he_type):
    H_local = {} # instantiate a set that stores the total costs associated with each valid action
    for action in valid_actions: # iterates over each valid action and calculates the total cost for each action based on the selected heuristic and search mode          
            next_state = problem.result(current_state, action)

            monster = find_state_coord(problem.grid, ord(m))
            if m == "r":
                heuristic_cost = heuristic_dyn(next_state, problem.goal_state, monster, 3, he_type) 
            elif m == "a":
                heuristic_cost = heuristic_dyn(next_state, problem.goal_state, monster, 4, he_type)

            if mode == "astar":
                cost_so_far = problem.step_cost(next_state)
                total_cost = cost_so_far + heuristic_cost
            elif mode == "greedy":
                total_cost = heuristic_cost

            H_local[action] = total_cost

    best_action = min(H_local, key=H_local.get) # finds most efficient action
    next_state = problem.result(current_state, best_action) # calculates next state
    print(f"Selected action: {best_action}, Total cost: {H_local[best_action]}")
    return best_action, next_state

def backtrack(problem, current_state, valid_actions, seq):
    H_local = {}
    for action in valid_actions:
            next_state = problem.result(current_state, action)
    
            H_local[action] = seq.index(next_state)

    best_action = min(H_local, key=H_local.get) # finds action that leads to furthest state from the dead end
    next_state = problem.result(current_state, best_action) # calculates next state
    print(f"Selected action: {best_action}, Total cost: {H_local[best_action]}")
    return best_action, next_state

def is_dead_end(problem, current_state, seq):
    valid_actions = [action for action in problem.actions(current_state) if problem.result(current_state, action) not in seq] # removes actions that lead to already visited states
    return not valid_actions # returns True if valid_actions is empty
