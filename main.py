from visualize import plot_grid
from collections import deque

def bfs(start, goal, grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = {start: None}

    while queue:
        node = queue.popleft()
        if node == goal:
            break
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            new = (node[0]+dx, node[1]+dy)
            if (0 <= new[0] < rows and 0 <= new[1] < cols and
                grid[new[0]][new[1]] == 0 and new not in visited):
                queue.append(new)
                visited[new] = node

    # Reconstruct path
    path = []
    node = goal
    while node:
        path.append(node)
        node = visited.get(node)
    path.reverse()
    return path

if __name__ == "__main__":
    grid = [
        [0,0,0,1,0],
        [1,0,0,1,0],
        [0,0,0,0,0],
        [0,1,1,0,1],
        [0,0,0,0,0],
    ]
    start = (0,0)
    goal = (4,4)

    path = bfs(start, goal, grid)
    plot_grid(grid, path, start, goal)
