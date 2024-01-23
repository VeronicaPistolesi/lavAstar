from utils import *
from classes import *
from algorithms import *
import time
import pandas as pd
import matplotlib.pyplot as plt
import IPython.display as display



algorithms = ['Breadth First Search (UA)', 'Uniform Cost Search (UA)', 'A* (IA)', 'Greedy Best First Search (IA)']

time_levels = [[], [], [], []]
path_levels = [[], [], [], []]
path_cost_levels = [[], [], [], []]

def generate_grid_problem(observation):
    game_map = process_matrix(observation['chars'])
    game_map_colors = process_matrix(observation['colors'])
    start_state = find_state_coord(game_map, ord('@'))
    goal_state = find_state_coord(game_map, ord('>'))
    grid_problem = GridWorldProblem(game_map, start_state, goal_state, game_map_colors)
    return grid_problem

def perform_search(level, search_agent, search_algorithm, distance_function=None):

    if distance_function: # Informed search
        solution_path, explored_nodes_paths, node_distances = search_agent.search(search_algorithm, distance_function)
    else: # Uninformed search
        solution_path = search_agent.search(search_algorithm)

    record_results(level, search_agent, solution_path)

    basic_graph = create_basic_graph(search_agent.problem, search_agent.state)
    explored_graph = highlight_explored_nodes(basic_graph, solution_path)

    if distance_function:
        plot_graph_distances(explored_graph, node_distances, f"plots/case{level}/{search_algorithm.__name__.lower()}.png")
    else:
        plot_graph(explored_graph, f"plots/case{level}/{search_algorithm.__name__.lower()}.png")

def record_results(level, search_agent, solution_path):
    time_levels[level - 1].append(search_agent.execution_time())
    path_levels[level - 1].append(len(solution_path))
    path_cost_levels[level - 1].append(cost_computation(search_agent.problem.grid, search_agent.problem.grid_colors, solution_path))

def generate_comparison_dataframe(level):
    df = pd.DataFrame()
    df['Algorithm'] = algorithms
    df['Execution Time'] = time_levels[level - 1]
    df['Path Length'] = path_levels[level - 1]
    df['Path Cost'] = path_cost_levels[level - 1]
    df.set_index('Algorithm', inplace=True)
    return df

# -----------------------------------------------------------------------------------------------
def perform_online_search(obs_lv, env_lv, monster_type, alg, heur_type):
    # Instantiate the game map
    game_map_lv = process_matrix(obs_lv['chars'])
    game_map_lv_colors = process_matrix(obs_lv['colors'])
    game_lv = obs_lv['pixel']

    # Instantiate a problem from class GridWorldProblem
    grid_problem = GridWorldProblem(game_map_lv, find_state_coord(game_map_lv, ord('@')), find_state_coord(game_map_lv, ord('>')), game_map_lv_colors)

    onlineSearchAgent = OnlineSearchAgent(grid_problem)

    # Plot the game map
    image = plt.imshow(game_lv[25:300, :250])
    
    agent = find_state_coord(grid_problem.grid, ord('@'))

    while agent!=None:
        
        print("Agent:", agent)

        valid_actions = grid_problem.actions(agent)
        #print("Valid directions:", valid_actions)

        action, next_state = onlineSearchAgent.online_search(onlineMode, agent, monster_type, alg, heur_type)

        grid, _, _, _ = env_lv.step(action) # Agent takes next step
        new_game_map_lv4_1 = process_matrix(grid['chars']) # Memorize and cuts out the new map
        grid_problem.update_grid(new_game_map_lv4_1) # Update grid
        agent = find_state_coord(grid_problem.grid, ord('@'))

        display.display(plt.gcf())
        display.clear_output(wait=True)
        image.set_data(grid['pixel'][25:300, :250])
        time.sleep(1.5)

    if agent==None:
        path = onlineSearchAgent.seq
        if grid_problem.goal_test(next_state):
            plt.close()
            print('Goal reached!')
            path = onlineSearchAgent.seq
            path_cost = cost_computation(game_map_lv, game_map_lv_colors, path)
            print(f"Path length: {len(path)}, Path cost: {path_cost}")
        
        else:
            print("You loose")