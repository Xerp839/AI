from queue import PriorityQueue

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def find_path(start, goal, graph, heuristic):
    open_set = PriorityQueue()
    open_set.put(Node(start, None, 0, heuristic(start)))
    closed_set = set()

    while not open_set.empty():
        current_node = open_set.get()

        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            path.reverse()
            return path

        if current_node.state in closed_set:
            continue

        closed_set.add(current_node.state)

        for neighbor, cost in graph[current_node.state]:
            if neighbor not in closed_set:
                neighbor_node = Node(neighbor, current_node, current_node.cost + cost, heuristic(neighbor))
                open_set.put(neighbor_node)

    return None

# Example graph
graph = {
    'A': [('B', 6), ('C', 2)],
    'B': [('D', 10)],
    'C': [('E', 3)],
    'D': [('F', 11)],
    'E': [('D', 4)],
    'F': []
}

# Heuristic function (for A* algorithm)
def heuristic(node):
    H_dist = {
        'A': 9,
        'B': 8,
        'C': 5,
        'D': 13,
        'E': 8,
        'F': 20,
    }
    return H_dist[node]

# Main function
def main():
    start = 'A'
    goal = 'F'
    path = find_path(start, goal, graph, heuristic)
    if path:
        print(f"Path from {start} to {goal}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start} to {goal}")

if __name__ == "__main__":
    main()
