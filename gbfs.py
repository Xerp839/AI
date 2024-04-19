from queue import PriorityQueue

def greedy_best_first_search(start_node, stop_node):
    open_set = PriorityQueue()
    open_set.put((heuristic(start_node), start_node))
    closed_set = set()
    parents = {}
    parents[start_node] = start_node
    
    while not open_set.empty():
        _, n = open_set.get()
        
        if n == stop_node or Graph_nodes[n] == None:
            break
        
        for (m, weight) in get_neighbors(n):
            if m not in closed_set:
                parents[m] = n
                open_set.put((heuristic(m), m))
        
        closed_set.add(n)
    
    if n == stop_node:
        path = []
        while parents[n] != n:
            path.append(n)
            n = parents[n]
        path.append(start_node)
        path.reverse()
        print('Path found: {}'.format(path))
        return path
    else:
        print('Path does not exist!')
        return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
    H_dist = {
        'A': 9,
        'B': 8,
        'C': 5,
        'D': 13,
        'E': 8,
        'F': 20,
    }
    return H_dist[n]

Graph_nodes = {
    'A': [('B', 6), ('C', 2)],
    'B': [('D', 10)],
    'F': None,
    'E': [('D', 4)],
    'D': [('F', 11)],
    'C': [('E', 3)]   
}

# Example usage:
print("Sequence of Greedy Best-First Search: ")
greedy_best_first_search('A', 'F')
