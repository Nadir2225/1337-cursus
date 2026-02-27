from my_types import Config, Maze, Cell, Coords
import random

DIGIT_4 = [
    [1,0,1,0],
    [1,0,1,0],
    [1,1,1,0],
    [0,0,1,0],
    [0,0,1,0],
]

DIGIT_2 = [
    [1,1,1,0],
    [0,0,1,0],
    [1,1,1,0],
    [1,0,0,0],
    [1,1,1,0],
]
PATTERN_42 = [
    "X  X XX ",
    "X  X  X ",
    "XXXX  X ",
    "   X XX ",
    "   X X  ",
    "   X XX ",
]

class MazeGenerator:
    """
    Generates a maze according to configuration.
    """

    # Each digit is 5 tall x 4 wide, with 1 col gap between

    def __init__(
        self,
        config: Config
    ) -> None:
        self.config = config
        self.maze = Maze(config.width, config.height)

    # def generate(self) -> None:
    #     """
    #     Generate the maze.
    #     """
    #     if self.config.seed:
    #         random.seed(self.config.seed)
    #     self.maze.create_grid()

    #     self._generate_perfect_maze()
    #     if not self.config.perfect:
    #         self._generate_imperfect_maze()

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

    def apply_42_pattern(self) -> bool:
        """
        Fully hard-coded '42' pattern.
        Assumes maze is at least 8x8.
        No loops. No dynamic building.
        """

        start_x = (self.maze.width - 9) // 2
        start_y = (self.maze.height - 5) // 2

        def seal(x, y):
            cell = self.maze.get_cell(Coords(x, y))
            if cell:
                cell.north = True
                cell.east = True
                cell.south = True
                cell.west = True
                self._seal_cell_neighbors(cell)

        seal(start_x + 0, start_y + 0)
        seal(start_x + 3, start_y + 0)

        seal(start_x + 0, start_y + 1)
        seal(start_x + 3, start_y + 1)

        seal(start_x + 0, start_y + 2)
        seal(start_x + 1, start_y + 2)
        seal(start_x + 2, start_y + 2)
        seal(start_x + 3, start_y + 2)

        seal(start_x + 3, start_y + 3)
        seal(start_x + 3, start_y + 4)

        offset = 5

        seal(start_x + offset + 0, start_y + 0)
        seal(start_x + offset + 1, start_y + 0)
        seal(start_x + offset + 2, start_y + 0)
        seal(start_x + offset + 3, start_y + 0)

        seal(start_x + offset + 3, start_y + 1)

        seal(start_x + offset + 0, start_y + 2)
        seal(start_x + offset + 1, start_y + 2)
        seal(start_x + offset + 2, start_y + 2)
        seal(start_x + offset + 3, start_y + 2)

        seal(start_x + offset + 0, start_y + 3)

        seal(start_x + offset + 0, start_y + 4)
        seal(start_x + offset + 1, start_y + 4)
        seal(start_x + offset + 2, start_y + 4)
        seal(start_x + offset + 3, start_y + 4)

        return True

    def _seal_cell_neighbors(self, cell: Cell) -> None:
        """Ensure neighboring cells have matching walls for a sealed cell."""
        x, y = cell.coords.x, cell.coords.y
        for direction, (dx, dy), opp in [
            ('north', (0,-1), 'south'),
            ('east',  (1, 0), 'west'),
            ('south', (0, 1), 'north'),
            ('west',  (-1,0), 'east'),
        ]:
            neighbor = self.maze.get_cell(Coords(x+dx, y+dy))
            if neighbor:
                setattr(neighbor, opp, True)

    def generate(self) -> None:
        if self.config.seed:
            random.seed(self.config.seed)
        self.maze.create_grid()
        self._generate_perfect_maze()
        if not self.config.perfect:
            self._generate_imperfect_maze()
        self.apply_42_pattern()  # ← add this
