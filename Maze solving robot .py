# Maze solving robot simulation using Left-Hand Rule

# Maze legend:
# 0 - open path
# 1 - wall
# S - start
# E - end

maze = [
    ['S', 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 'E'],
    [1, 1, 0, 1]
]

# Robot directions (North, East, South, West)
directions = ['N', 'E', 'S', 'W']

# Movement offsets for each direction
moves = {
    'N': (-1, 0),
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1)
}

# Function to find start position
def find_start(maze):
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if col == 'S':
                return (i, j)
    return None

# Check if cell is within maze and not a wall
def is_open(x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1

# Turn left
def turn_left(direction):
    return directions[(directions.index(direction) - 1) % 4]

# Turn right
def turn_right(direction):
    return directions[(directions.index(direction) + 1) % 4]

# Turn around
def turn_back(direction):
    return directions[(directions.index(direction) + 2) % 4]

# Simulate robot movement
def solve_maze():
    pos = find_start(maze)
    direction = 'E'  # Assume robot starts facing East
    path = [pos]

    while True:
        x, y = pos

        if maze[x][y] == 'E':
            print("Maze Solved! Path:", path)
            break

        # Check left side
        left_dir = turn_left(direction)
        lx, ly = x + moves[left_dir][0], y + moves[left_dir][1]

        if is_open(lx, ly):
            direction = left_dir
            pos = (lx, ly)
        else:
            # If front is open, go forward
            fx, fy = x + moves[direction][0], y + moves[direction][1]
            if is_open(fx, fy):
                pos = (fx, fy)
            else:
                # Otherwise turn right
                direction = turn_right(direction)

        path.append(pos)

# Run the simulation
solve_maze()


