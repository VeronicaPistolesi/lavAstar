import numpy as np
from typing import List, Tuple
import matplotlib.pyplot as plt
import networkx as nx
import math

# useful for offline search
def actions_from_path(start: Tuple[int, int], path: List[Tuple[int, int]]) -> List[int]:
    action_map = {
        "N": 0,
        "E": 1,
        "S": 2,
        "W": 3,
        "NE": 4,
        "SE": 5,
        "SW": 6,
        "NW": 7
    }
    actions = []
    # x_s, y_s = start
    x_s, y_s = start
    for (x, y) in path:
        if x_s > x:
            if y_s > y:
                actions.append(action_map["NW"])
            elif y_s == y:
                actions.append(action_map["W"])
            elif y_s < y:
                actions.append(action_map["SW"])
        elif x_s < x:
            if y_s > y:
                actions.append(action_map["NE"])
            elif y_s == y:
                actions.append(action_map["E"])
            elif y_s < y:
                actions.append(action_map["SE"])
        elif x_s == x:
            if y_s > y:
                actions.append(action_map["N"])
            elif y_s < y:
                actions.append(action_map["S"])
            
        x_s = x
        y_s = y
    
    return actions

# ------------------------------------------------------------------------------------------------------------

def process_matrix(matrix):
    chars = {32, 0}
    new_matrix = [[element for element in row if element not in chars] for row in matrix] #Removes 32 values from the matrix
    new_matrix = [row for row in new_matrix if row]  #Removes empty rows    
    new_matrix = np.array(new_matrix) #Convert to NumPy array
    
    return new_matrix

def find_state_coord(grid, value):
    for y in range(len(grid)):  # iteration over the rows of the 2-dimensional array, len(grid) = number of rows
        for x in range(len(grid[0])):   # iteration over columns; len(grid[0]) = gives number of columns
            if grid[y][x] == value:     # check current position in array equals to value
                return (x, y)   # tuple containing the coordinates
    return None

def find_cells_coord(grid, value):
    cell_pos = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == value:
                cell_pos.append((x, y))
    return cell_pos

def cost_computation(grid, grid_colors, solution_path):
    cost = 0
    for state in solution_path:
        x, y = state
        terrain_type = grid[y][x]
        terrain_color = grid_colors[y][x]

        if terrain_type == ord('.') and terrain_color == 6:  #Ice cell
            cost += 3
        else:
            cost += 1
    return cost


# -----------------------------------------------------------------------------------------------

# Heuristic function: Manhatten Distance
def manhattan_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> int: 
    x1, y1 = point1     
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

def euclidean_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    x1, y1 = point1
    x2, y2 = point2
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

def enemy_heuristic(state, enemy_position):
    # to adapt
    distance_to_enemy = manhattan_distance(state, enemy_position)
    return - distance_to_enemy


"""
def heuristic(state, goal_state, moving_obstacle_position):
    # Calculate the Manhattan distance between the current state and the goal state
    h = manhattan_distance(state, goal_state)

    # Penalize the heuristic if the agent's position overlaps with the moving obstacle
    if state == moving_obstacle_position:
        h += 100  # Adjust the penalty value as needed

    return h
"""

# -----------------------------------------------------------------------------------------------

def create_basic_graph(problem, agent_pos):
    G = nx.Graph()

    for y in range(problem.height):
        for x in range(problem.width):
            state = (x, y)
            terrain_color = problem.grid_colors[y][x]

            if problem.grid[x][y] not in {ord('-'), ord('|')}:  # Excludes walls
                actions = problem.actions(state)
                for action in actions:
                    result_state = problem.result(state, action)
                    G.add_edge(state, result_state, cost=1)
                    G.add_node(state, color='purple' if state == agent_pos
                                            else 'yellow' if state == find_state_coord(problem.grid, ord('>'))
                                            else 'red' if state in find_cells_coord(problem.grid, ord('}'))
                                            else 'gray' if state in find_cells_coord(problem.grid, ord('.')) and terrain_color==6 # ice coordinates 
                                            else 'orange' if state in find_cells_coord(problem.grid, ord('d'))
                                            else 'blue' if state in find_cells_coord(problem.grid, ord('a'))
                                            else 'lightblue')

    return G

def highlight_explored_nodes(G, explored_nodes):
    if G is not None:
        for node, data in G.nodes(data=True):
            G.nodes[node]['color'] = 'green' if node in explored_nodes else data['color']

    return G

def highlight_explored_nodes_by_enemy(G, explored_nodes):
    if G is not None:
        for node, data in G.nodes(data=True):
            G.nodes[node]['color'] = 'blue' if node in explored_nodes else data['color']

    return G

def plot_graph(G):
    if G is not None:
        pos = {node: (node[0], -node[1]) for node in G.nodes()}
        labels = {node: node for node in G.nodes()}
        node_colors = [data['color'] for node, data in G.nodes(data=True)]

        subtitle = 'Each node is labeled with its coordinates inside the grid'

        plt.figure(figsize=(10, 10))
        nx.draw(G, pos, with_labels=True, labels=labels, font_size=6, font_color='black', node_size=800,
                node_color=node_colors, font_weight='bold', edge_color='gray')

        plt.title('Two-Dimensional State Space Graph with state coordinates')
        plt.suptitle(subtitle, fontsize=12, color='blue')  # Add a subtitle above the plot title
        plt.show()

def plot_graph_distances(G, distances_dict):
    if G is not None:
        pos = {node: (node[0], -node[1]) for node in G.nodes()}
        
        labels = {}
        subtitle = 'Each explored node is labeled (g(n), h(n)). NA means the value is \"Not Available\"'
        
        for node in G.nodes():
            node_dict = distances_dict.get(node, {})
            if 'g(n)' in node_dict and 'h(n)' in node_dict:
                labels[node] = f"({node_dict['g(n)']}, {node_dict['h(n)']})"
            elif 'g(n)' in node_dict:
                labels[node] = (f"({node_dict['g(n)']}, NA)")
            elif 'h(n)' in node_dict:
                labels[node] = (f"(NA, {node_dict['h(n)']})")
            else:
                labels[node] = ""  # Use an empty string for both g(n) and h(n) if neither is present
        
        node_colors = [data['color'] for node, data in G.nodes(data=True)]

        plt.figure(figsize=(10, 10))
        nx.draw(G, pos, with_labels=True, labels=labels, font_size=6, font_color='black', node_size=800,
                node_color=node_colors, font_weight='bold', edge_color='gray')

        plt.title('Two-Dimensional State Space Graph with node distances')
        plt.suptitle(subtitle, fontsize=12, color='blue')  # Add a subtitle above the plot title
        plt.show()

# -----------------------------------------------------------------------------------------------

"""
def modify_env(original_matrix):
    value_mapping = {
    (2, 5, 0): 124, # wall
    (1, 0, 0): 46, # floor
    (10, 0, 0): 64, # agent
    (6, 2, 0): 68, # monster/ball 
    (8, 1, 0): 62, # stairs
    (9, 0, 0): 125 # lava
}
    
    # new 2D matrix with the mapped values
    mapped_matrix = np.zeros((original_matrix.shape[0], original_matrix.shape[1]))

    for i in range(original_matrix.shape[0]):
        for j in range(original_matrix.shape[1]):
            # Get the tuple representing the row in the original matrix
            row_tuple = tuple(original_matrix[i, j, :])

            # Map the value using the value_mapping dictionary
            mapped_value = value_mapping.get(row_tuple, 0)

            # Assign the mapped value to the corresponding position in the new matrix
            mapped_matrix[i, j] = mapped_value

    # Resulting 2D matrix
    return mapped_matrix
"""