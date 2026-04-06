import time
from my_types import Config, Maze, Cell, Coords
import random
from typing import Optional


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
                neighbor_coords = Coords(
                    current.coords.x + dx, current.coords.y + dy
                )
                neighbor = self.maze.get_cell(neighbor_coords)
                if neighbor and not neighbor.visited and not neighbor.pattern:
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

    def apply_42_pattern(self) -> None:
        """
        Fully hard-coded '42' pattern.
        Assumes maze is at least 8x8.
        No loops. No dynamic building.
        """

        start_x = (self.maze.width + 1) // 2
        start_y = (self.maze.height + 1) // 2

        def seal(x: int, y: int) -> None:
            cell = self.maze.get_cell(Coords(x, y))
            if cell:
                cell.north = True
                cell.east = True
                cell.south = True
                cell.west = True
                cell.pattern = True
                cell.visited = True
                self._seal_cell_neighbors(cell)

        # number 2
        seal(start_x, start_y)
        seal(start_x, start_y - 1)
        seal(start_x + 1, start_y - 1)
        seal(start_x + 2, start_y - 1)
        seal(start_x + 2, start_y - 2)
        seal(start_x + 2, start_y - 3)
        seal(start_x + 1, start_y - 3)
        seal(start_x, start_y - 3)
        seal(start_x, start_y + 1)
        seal(start_x + 1, start_y + 1)
        seal(start_x + 2, start_y + 1)

        # number 4
        start_x -= 2
        seal(start_x, start_y)
        seal(start_x, start_y - 1)
        seal(start_x, start_y - 2)
        seal(start_x, start_y - 3)
        seal(start_x - 1, start_y - 1)
        seal(start_x - 2, start_y - 1)
        seal(start_x - 2, start_y - 2)
        seal(start_x - 2, start_y - 3)
        seal(start_x, start_y + 1)

        entry_cell = self.maze.get_cell(self.config.entry)
        exit_cell = self.maze.get_cell(self.config.exit)
        if (
            entry_cell is not None
            and exit_cell is not None
        ):
            if (
                entry_cell.pattern
                or exit_cell.pattern
            ):
                raise ValueError("Entry/Exit cannot be on '42' pattern")

    def _seal_cell_neighbors(self, cell: Cell) -> None:
        """Ensure neighboring cells have matching walls for a sealed cell."""
        x, y = cell.coords.x, cell.coords.y
        for direction, (dx, dy), opp in [
            ('north', (0, -1), 'south'),
            ('east', (1, 0), 'west'),
            ('south', (0, 1), 'north'),
            ('west', (-1, 0), 'east'),
        ]:
            neighbor = self.maze.get_cell(Coords(x+dx, y+dy))
            if neighbor:
                setattr(neighbor, opp, True)

    def open_rooms_exist(self) -> bool:
        for y in range(self.maze.height):
            for x in range(self.maze.width):
                center = self.maze.get_cell(Coords(x, y))
                top = self.maze.get_cell(Coords(x, y - 1))
                right = self.maze.get_cell(Coords(x + 1, y))
                bottom = self.maze.get_cell(Coords(x, y + 1))
                left = self.maze.get_cell(Coords(x - 1, y))
                if (
                    not center or not top
                    or not right or not left
                    or not bottom
                ):
                    continue
                if (
                    not center.north and not center.east
                    and not center.south and not center.west
                    and not top.east and not top.west
                    and not right.north and not right.south
                    and not bottom.east and not bottom.west
                    and not left.north and not left.south
                ):
                    return True
        return False

    def generate(self) -> None:
        try:
            if self.config.seed is None:
                seed: Optional[str | int] = int(time.time() * 1000)
            else:
                seed = self.config.seed
            self.config.seed = seed
            random.seed(seed)
            self.maze.create_grid()
            self.apply_42_pattern()
            self._generate_perfect_maze()
            if not self.config.perfect:
                self._generate_imperfect_maze()
            # i = 0
            # self.open_room()
            while self.open_rooms_exist():
                self.maze.create_grid()
                self.apply_42_pattern()
                self._generate_perfect_maze()
                if not self.config.perfect:
                    self._generate_imperfect_maze()
                # self.open_room()
                # if i < 10:
                #     print("Retrying maze generation to avoid open rooms...")
                # else:
                #     break
                # i += 1
        except Exception as e:
            raise e

    def open_room(self) -> None:
        """
        use the following configuration to test open room detection:
            # === MAZE CONFIGURATION FILE ===
            # Lines starting with # are comments
            WIDTH=9
            HEIGHT=9
            # Entry point (x,y)
            ENTRY=2,5
            # Exit point (x,y)
            EXIT=7,7
            # Output file name
            OUTPUT_FILE=maze.txt
            # Perfect maze (no loops)
            PERFECT=True
            SEED=355
        """
        center = self.maze.get_cell(Coords(1, 7))
        top = self.maze.get_cell(Coords(1, 6))
        right = self.maze.get_cell(Coords(2, 7))
        bottom = self.maze.get_cell(Coords(1, 8))
        left = self.maze.get_cell(Coords(0, 7))
        top_right = self.maze.get_cell(Coords(2, 6))
        top_left = self.maze.get_cell(Coords(0, 6))
        bottom_right = self.maze.get_cell(Coords(2, 8))
        bottom_left = self.maze.get_cell(Coords(0, 8))
        if (
            center and top and right and bottom
            and left and top_right and top_left
            and bottom_right and bottom_left
        ):
            center.north = False
            center.east = False
            center.south = False
            center.west = False
            top.east = False
            top.west = False
            right.north = False
            right.south = False
            bottom.east = False
            bottom.west = False
            left.north = False
            left.south = False
            top_right.west = False
            top_right.south = False
            top_left.east = False
            top_left.south = False
            bottom_right.north = False
            bottom_right.west = False
            bottom_left.north = False
            bottom_left.east = False
