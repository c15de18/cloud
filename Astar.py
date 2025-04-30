def heuristic(a, b):
    # Simple Manhattan Distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_search(grid, start, goal):
    open_list = [start]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_list:
        # Choose node with lowest f_score
        current = min(open_list, key=lambda x: f_score.get(x, float('inf')))

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        open_list.remove(current)

        # Neighboring cells (Up, Down, Left, Right)
        x, y = current
        neighbors = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

        for neighbor in neighbors:
            nx, ny = neighbor
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == 1:  # Obstacle
                    continue

                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + heuristic(neighbor, goal)
                    if neighbor not in open_list:
                        open_list.append(neighbor)

    return None  # No path found

def main():
    grid = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (4, 4)

    path = astar_search(grid, start, goal)

    if path:
        print("Path found:")
        for step in path:
            print(step)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
