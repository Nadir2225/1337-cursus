from collections import deque
from my_types import Maze, Coords

def solve_maze_shortest(maze: Maze, entry: Coords, exit: Coords) -> str:
    queue = deque()
    queue.append(entry)

    visited = set()
    visited.add((entry.x, entry.y))

    # parent[(x, y)] = ((px, py), direction_letter)
    parent = {}

    moves = [
        ('N', 0, -1, 'north'),
        ('E', 1, 0, 'east'),
        ('S', 0, 1, 'south'),
        ('W', -1, 0, 'west')
    ]

    while queue:
        current = queue.popleft()
        cell = maze.get_cell(current)

        if current.x == exit.x and current.y == exit.y:
            break

        for letter, dx, dy, wall in moves:
            if getattr(cell, wall):  # wall is closed
                continue

            nx, ny = current.x + dx, current.y + dy
            if (nx, ny) in visited:
                continue

            neighbor = maze.get_cell(Coords(nx, ny))
            if neighbor:
                visited.add((nx, ny))
                parent[(nx, ny)] = ((current.x, current.y), letter)
                queue.append(Coords(nx, ny))

    # 🔁 Rebuild path from exit to entry
    path = []
    cur = (exit.x, exit.y)

    while cur != (entry.x, entry.y):
        prev, letter = parent[cur]
        path.append(letter)
        cur = prev

    return ''.join(reversed(path))
