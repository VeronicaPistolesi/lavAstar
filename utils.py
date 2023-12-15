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