# ==========================
# Drone Delivery Navigation
# ==========================

import heapq
from collections import deque

# --------- Graph Definition ---------
graph = {
    'A': {'B': 2, 'C': 5, 'D': 1},
    'B': {'A': 2, 'D': 2, 'E': 3},
    'C': {'A': 5, 'D': 2, 'F': 3},
    'D': {'A': 1, 'B': 2, 'C': 2, 'E': 1, 'F': 4},
    'E': {'B': 3, 'D': 1, 'G': 2},
    'F': {'C': 3, 'D': 4, 'G': 1},
    'G': {'E': 2, 'F': 1, 'H': 3},
    'H': {'G': 3}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 6,
    'D': 4,
    'E': 2,
    'F': 2,
    'G': 1,
    'H': 0
}

start = 'A'
goal = 'H'

# ===================================
# Depth-First Search (DFS)
# ===================================
def dfs(graph, start, goal):
    visited = set()
    path = []
    nodes_expanded = [0]  # Use list to allow modification inside helper

    def dfs_helper(node):
       # Mark current node as visited and add to path
        visited.add(node)
        path.append(node)
        nodes_expanded[0] += 1  # Increment nodes expanded count

        # If goal is found, return True
        if node == goal:
            return True

        # Explore neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs_helper(neighbor):
                    return True

        # Backtrack if goal not found in this path
        path.pop()
        return False

    dfs_helper(start)
    return path, nodes_expanded[0]
# ===================================
# Breadth-First Search (BFS)
# ===================================
def bfs(graph, start, goal):
    visited = set()
    queue = deque()
    queue.append((start, [start]))
    nodes_expanded = 0

    while queue:
        node, path = queue.popleft()
        nodes_expanded += 1


        #Goal check
        if node == goal:
            return path, nodes_expanded
        
        #Explore neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, nodes_expanded  # Return None if no path is found

# ===================================
# Uniform Cost Search (UCS)
# ===================================
def ucs(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start, [start]))
    explored = set()
    nodes_expanded = 0

    # TODO: implement UCS logic
    while frontier:
        cost, node, path = heapq.heappop(frontier)
        nodes_expanded += 1

        #Skip if we have already found the cheaper path to this node
        if node in explored:
            continue
        explored.add(node)

        # Goal check
        if node == goal:
            return path, cost, nodes_expanded

        # Expand Neighbors
        for neighbor, edge_cost in graph[node].items():
            if neighbor not in explored:
                new_cost = cost + edge_cost
                heapq.heappush(frontier, (new_cost, neighbor, path + [neighbor]))
# ===================================
# A* Search
# ===================================
def a_star(graph, start, goal, heuristic):
    frontier = []
    heapq.heappush(frontier, (heuristic[start], 0, start, [start]))
    explored = set()
    nodes_expanded = 0

    # TODO: implement A* logic
    while frontier:
        f, g, node, path = heapq.heappop(frontier)
        nodes_expanded += 1

        # Skip if we have already found the cheaper path to this node
        if node in explored:
            continue
        explored.add(node)

        # Goal check
        if node == goal:
            return path, g, nodes_expanded

        # Expand neighbors
        for neighbor, edge_cost in graph[node].items():
            if neighbor not in explored:
                new_g = g + edge_cost
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(frontier, (new_f, new_g, neighbor, path + [neighbor]))

    return None, nodes_expanded  # Return None if no path is found
# Run and Compare
# ===================================
if __name__ == "__main__":
    
    dfs_path,   dfs_exp              = dfs(graph, start, goal)
    bfs_path,   bfs_exp              = bfs(graph, start, goal)
    ucs_path,   ucs_cost,  ucs_exp   = ucs(graph, start, goal)
    astar_path, astar_cost, astar_exp = a_star(graph, start, goal, heuristic)
 
    def path_cost(path):
        """Helper to compute total edge cost of any path."""
        return sum(graph[path[i]][path[i+1]] for i in range(len(path) - 1))
 
    print("=" * 55)
    print(f"  Search Results: {start} -> {goal}")
    print("=" * 55)
    print(f"DFS  path: {' -> '.join(dfs_path)}")
    print(f"     steps={len(dfs_path)-1}, nodes expanded={dfs_exp}")
    print()
    print(f"BFS  path: {' -> '.join(bfs_path)}")
    print(f"     steps={len(bfs_path)-1}, nodes expanded={bfs_exp}")
    print()
    print(f"UCS  path: {' -> '.join(ucs_path)}")
    print(f"     cost={ucs_cost}, nodes expanded={ucs_exp}")
    print()
    print(f"A*   path: {' -> '.join(astar_path)}")
    print(f"     cost={astar_cost}, nodes expanded={astar_exp}")
    print("=" * 55)