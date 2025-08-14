from collections import deque
from time import sleep
import sys

maze = []

# Read maze from .txt file
with open('maze.txt') as file:
    for line in file.readlines():
        line = line.replace('.', '█').strip()
        maze.append(line)

def find_start_position(maze: list[str]) -> tuple[int, int]:
    '''
    Finds and returns the starting position in the maze.
    '''
    for row_idx, row in enumerate(maze):
        for col_idx, col in enumerate(row):
            if maze[row_idx][col_idx] == 'S':
                return (row_idx, col_idx)

def get_legal_moves(maze: list[str], current_position:tuple[int, int]) -> list[tuple[int, int]]:
    '''
    Returns all moves that can be made from the current position. A player can move up, down, left, or right.
    '''

    possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    legal_moves = []

    for move in possible_moves:
        x, y = move 
        x_cur, y_cur = current_position
        x_new, y_new = x + x_cur, y + y_cur

        if maze[x_new][y_new] != '█':
            legal_moves.append((x_new, y_new))

    return legal_moves

def solve_maze(maze: list[str]) -> list[tuple[int, int]]:
    '''
    Returns the path that solves the maze. Implements BFS algorithm.
    '''
    start = find_start_position(maze)
    queue = deque([start])
    visited = {start}
    previous_node = {}

    while queue:
        node = queue.popleft()
        row, col = node 

        if maze[row][col] == 'E':
            break

        visited.add(node)

        for move in get_legal_moves(maze, node):
            if move not in visited:
                previous_node[move] = node
                queue.append(move)

    # Trace and store the path from S to E
    path = [node]

    while True:
        prev = previous_node[node]
        path.append(prev)
        node = prev

        if node == find_start_position(maze):
            break 
    
    return path[::-1]

def render(maze):
    """
    Print the maze grid (list[list[str]]) once.
    """
    
    out = []
    for row in maze:
        out.append(''.join(row))
    sys.stdout.write('\n'.join(out) + '\n')
    sys.stdout.flush()

def animate_path(maze, solved_path, delay=0.05, mark='.'):
    """
    Animate the solver's progress.
      - maze: list[list[str]] (mutable grid)
      - solved_path: list[(r, c)], including S at [0] and E at [-1]
      - delay: seconds between steps
      - mark: character to draw for the path
    """

    rows = len(maze)

    # Initial draw
    render(maze)
    sleep(delay)

    # Walk the path, skipping the start and end nodes
    for r, c in solved_path[1:-1]:
        # Don't overwrite walls or labels
        if maze[r][c] not in ('#', '█', 'S', 'E'):
            maze[r][c] = mark

        # Move cursor up by the maze height and redraw in place
        sys.stdout.write(f'\x1b[{rows}A')  # move cursor up N lines
        render(maze)
        sleep(delay)

solved_path = solve_maze(maze)

print('Solving maze...\n')
sleep(3)

# make maze mutable:
maze = [list(row) for row in maze]

animate_path(maze, solved_path, delay=0.5, mark='.')

print('\nSolved!')