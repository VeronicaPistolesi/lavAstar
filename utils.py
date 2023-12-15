import numpy as np
from typing import List, Tuple
import matplotlib.pyplot as plt
import networkx as nx
import math

def actions_from_path(start: Tuple[int, int], path: List[Tuple[int, int]]) -> List[int]:
    action_map = {
        "N": 2,
        "E": 3,
        "S": 0,
        "W": 1
    }
    actions = []
    x_s, y_s = start
    for (x, y) in path:
        if x_s == x:
            if y_s > y:
                actions.append(action_map["S"])
            else:
                actions.append(action_map["N"])
        elif y_s == y:
            if x_s < x:
                actions.append(action_map["W"])
            else:
                actions.append(action_map["E"])
        else:
            raise Exception("x and y can't change at the same time. Oblique moves not allowed!")
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

def find_state_coord(self, value):
        for y in range(len(self)):  # iteration over the rows of the 2-dimensional array, len(self) = number of rows
            for x in range(len(self[0])):   # iteration over columns; len(self[0]) = gives number of columns
                if self[y][x] == value:     # check current position in array equals to value
                    return (x, y)   # tuple containing the coordinates
        return None

def find_lava_coord(self, value):
        lava_pos = []
        for y in range(len(self)):
            for x in range(len(self[0])):
                if self[y][x] == value:
                    lava_pos.append((x, y))
        return lava_pos