from my_types import Config, Maze, Cell, Coords
import random

class MazeGenerator:
    """
    Generates a maze according to configuration.
    """

    def __init__(
        self,
        config: Config
    ) -> None:
        self.config = config
        self.maze = Maze(config.width, config.height)

    def generate(self) -> None:
        """
        Generate the maze.
        """
        if self.config.seed:
            random.seed(self.config.seed)
        self.maze.create_grid()

        self._generate_perfect_maze()
        if not self.config.perfect:
            self._generate_imperfect_maze()

        # self.maze.print_maze(self.config.entry, self.config.exit)

    def _generate_perfect_maze(self) -> None:
        """
        Generate a perfect maze (DFS / backtracker).
        """
        stack = []

        start_cell = self.maze.get_cell(self.config.entry)
        if not start_cell:
            raise ValueError("Invalid entry coordinates")
        
        start_cell.visited = True
        stack.append(start_cell)

        while stack:
            current = stack[-1]

            neighbors = []
            directions = [
                ('north', (0, -1)),
                ('east', (1, 0)),
                ('south', (0, 1)),
                ('west', (-1, 0))
            ]

            for direction, (dx, dy) in directions:
                neighbor_coords = Coords(current.coords.x + dx, current.coords.y + dy)
                neighbor = self.maze.get_cell(neighbor_coords)
                if neighbor and not neighbor.visited:
                    neighbors.append(neighbor)

            if neighbors:
                next_cell = random.choice(neighbors)
                self._remove_walls(current, next_cell)
                next_cell.visited = True
                stack.append(next_cell)
            else:
                stack.pop()
    
    def _generate_imperfect_maze(self) -> None:
        """
        Generate an imperfect maze by creating a perfect maze first,
        then randomly removing walls to create loops.
        """

        total_cells = self.maze.width * self.maze.height
        extra_walls = total_cells // 4

        removed = 0
        while removed < extra_walls:
            x = random.randint(0, self.maze.width - 1)
            y = random.randint(0, self.maze.height - 1)
            cell = self.maze.grid[y][x]

            directions = ['north', 'east', 'south', 'west']
            random.shuffle(directions)

            for direction in directions:
                nx, ny = cell.coords.x, cell.coords.y
                if direction == 'north':
                    ny -= 1
                elif direction == 'east':
                    nx += 1
                elif direction == 'south':
                    ny += 1
                elif direction == 'west':
                    nx -= 1

                neighbor = self.maze.get_cell(Coords(nx, ny))
                if neighbor:
                    if direction == 'north' and cell.north:
                        cell.north = False
                        neighbor.south = False
                        removed += 1
                        break
                    elif direction == 'east' and cell.east:
                        cell.east = False
                        neighbor.west = False
                        removed += 1
                        break
                    elif direction == 'south' and cell.south:
                        cell.south = False
                        neighbor.north = False
                        removed += 1
                        break
                    elif direction == 'west' and cell.west:
                        cell.west = False
                        neighbor.east = False
                        removed += 1
                        break


    def _remove_walls(self, current: Cell, neighbor: Cell) -> None:
        """
        Remove walls between two adjacent cells.
        """
        dx = neighbor.coords.x - current.coords.x
        dy = neighbor.coords.y - current.coords.y

        if dx == 1:
            current.east = False
            neighbor.west = False
        elif dx == -1:
            current.west = False
            neighbor.east = False
        elif dy == 1:
            current.south = False
            neighbor.north = False
        elif dy == -1:
            current.north = False
            neighbor.south = False
        else:
            raise ValueError("Cells are not adjacent")
