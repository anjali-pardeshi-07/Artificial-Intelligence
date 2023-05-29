import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start node to current node
        self.h = 0  # Heuristic cost from current node to goal node
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

def heuristic_cost(position, goal):
    return abs(goal[0] - position[0]) + abs(goal[1] - position[1])

def get_neighbours(position, grid):
    neighbours = []
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

    for direction in directions:
        new_row = position[0] + direction[0]
        new_col = position[1] + direction[1]

        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != 1:
            neighbours.append((new_row, new_col))

    return neighbours

def a_star(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start)
    goal_node = Node(goal)
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to get it from start to goal

        neighbours = get_neighbours(current_node.position, grid)
        for neighbour in neighbours:
            if neighbour in closed_set:
                continue

            neighbour_node = Node(neighbour, current_node)
            neighbour_node.g = current_node.g + 1
            neighbour_node.h = heuristic_cost(neighbour, goal)
            neighbour_node.f = neighbour_node.g + neighbour_node.h

            if neighbour_node in open_list:
                # If the neighbour is already in the open list with a lower cost, skip it
                continue

            heapq.heappush(open_list, neighbour_node)

    return None  # No path found

# Get user input for grid size
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Get user input for the grid
print("Enter the grid values:")
grid = []
for _ in range(rows):
    row = list(map(int, input().split()))
    grid.append(row)

# Get user input for start and goal positions
start_row, start_col = map(int, input("Enter the start position (row column): ").split())
goal_row, goal_col = map(int, input("Enter the goal position (row column): ").split())

start = (start_row, start_col)
goal = (goal_row, goal_col)

path = a_star(grid, start, goal)

if path:
    print("Path found:")
    for position in path:
        print(position)
else:
    print("No path found.")
