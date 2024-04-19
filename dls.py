graph={
    'a': ['b','c','d'],
    'b': ['e','f'],
    'c': ['f'],
    'd': [],
    'e': [],
    'f': []
}


def dls(graph, start, goal, depth_limit):
    visited = set()

    def dfs(node, depth):
        if depth > depth_limit:
            return False  # Exceeds depth limit
        if node == goal:
            print(node)
            return True  # Goal found
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbour in graph[node]:
                if dfs(neighbour, depth + 1):
                    return True
        return False

    print("Sequence of DLS: ")
    if dfs(start, 0):
        print("Goal found within depth limit.")
    else:
        print("Goal not found within depth limit.")

# Example usage:
dls(graph, 'a', 'f', 2)  # Limiting depth to 2
