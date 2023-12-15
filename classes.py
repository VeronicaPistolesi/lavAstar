
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