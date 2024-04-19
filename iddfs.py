graph = {
  'a' : ['b','d'],
  'b' : ['c', 'f'],
  'c' : ['e', 'g'],
  'd' : ['f'],
  'e' : ['f'],
  'f' : [],
  'g' : ['e']
}

def iddfs(graph, start, goal):
    depth_limit = 0
    while True:
        print("Searching with depth limit:", depth_limit)
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

        if dfs(start, 0):
            print("Goal found.")
            return
        else:
            depth_limit += 1

# Example usage:
print("Sequence of IDDFS: ")
iddfs(graph, 'a', 'f')
