from queue import PriorityQueue
import heapq

def memory_bounded_heuristic_search(start_node, stop_node, max_memory):
    open_set = []
    closed_set = set()
    parents = {}
    parents[start_node] = start_node
    heapq.heappush(open_set, (heuristic(start_node), start_node))
    current_memory = 1
    
    while open_set:
        _, n = heapq.heappop(open_set)
        current_memory -= 1
        
        if n == stop_node or Graph_nodes[n] == None:
            break
        
        if n in closed_set:
            continue
        
        for (m, weight) in get_neighbors(n):
            if m not in closed_set:
                parents[m] = n
                heapq.heappush(open_set, (heuristic(m), m))
                current_memory += 1
                
                if current_memory > max_memory:
                    print("Memory limit exceeded.")
                    return None
        
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
print("Sequence of Memory-Bounded Heuristic Search: ")
memory_bounded_heuristic_search('A', 'F', 5)  # Adjust max_memory as needed
