from typing import Optional, List


class Coords:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @classmethod
    def parse(cls, cords: Optional[str]) -> 'Coords':
        if cords is None:
            raise ValueError('coordinates cannot be None')
        try:
            cords_list = cords.split(',')
            if len(cords_list) != 2:
                raise ValueError('invalid coordinates')
            return cls(int(cords_list[0]), int(cords_list[1]))
        except ValueError:
            raise ValueError('invalid coordinates')

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'


class Config:
    def __init__(
        self,
        width: int,
        height: int,
        entry: Coords,
        exit: Coords,
        output_file: Optional[str],
        perfect: bool,
        seed: Optional[int],
    ):
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.output_file = output_file
        self.perfect = perfect
        self.seed = seed

    def __str__(self) -> str:
        return (
            f"=========== Config: ==========\n"
            f"  Width       : {self.width}\n"
            f"  Height      : {self.height}\n"
            f"  Entry       : {self.entry}\n"
            f"  Exit        : {self.exit}\n"
            f"  Output file : {self.output_file}\n"
            f"  Perfect     : {self.perfect}\n"
            f"  Seed        : {self.seed}\n"
            f"=============================="
        )


class Cell:
    """
    Represents a single maze cell.
    """

    def __init__(self, coords: Coords) -> None:
        self.coords = coords
        self.visited: bool = False
        self.pattern: bool = False
        # Walls: True = closed, False = open
        self.north: bool = True
        self.east: bool = True
        self.south: bool = True
        self.west: bool = True


class Maze:
    """
    Represents the maze grid.
    """

    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height
        self.grid: List[List[Cell]] = []

    def create_grid(self) -> None:
        """
        Create the grid of cells.
        """
        self.grid = [
            [Cell(Coords(x, y)) for x in range(self.width)]
            for y in range(self.height)
        ]

    def get_cell(self, coords: Coords) -> Optional[Cell]:
        """
        Return a cell at (x, y) if inside bounds.
        """
        if 0 <= coords.x < self.width and 0 <= coords.y < self.height:
            return self.grid[coords.y][coords.x]
        return None

    def print_maze(
        self,
        color: tuple[str, str],
        entry: Optional[Coords] = None,
        exit: Optional[Coords] = None,
        path_cells: Optional[set[tuple[int, int]]] = None
    ) -> None:
        """Print ASCII maze with '42' cells rendered as solid blocks."""

        def is_sealed(cell: Cell) -> bool:
            return cell.north and cell.east and cell.south and cell.west

        path_set = path_cells or set()

        for y in range(self.height):
            # Top wall row
            top_line = ""
            for x in range(self.width):
                cell = self.grid[y][x]
                top_line += f"{color[0]}+\033[0m"
                # if is_sealed(cell) and cell.pattern:
                if cell.pattern:
                    top_line += f"{color[1]}###\033[0m"
                else:
                    top_line += (
                        f"{color[0]}---\033[0m"
                        if cell.north else "   "
                    )
            top_line += f"{color[0]}+\033[0m"
            print(top_line)

            # Cell content row
            mid_line = ""
            for x in range(self.width):
                cell = self.grid[y][x]

                # if is_sealed(cell) and cell.pattern:
                if cell.pattern:
                    # Sealed = part of "42" pattern, render as solid block
                    mid_line += f"{color[1]}####\033[0m"
                    continue

                # Left wall
                mid_line += f"{color[0]}|\033[0m" if cell.west else " "

                # Cell content
                if (
                    entry
                    and cell.coords.x == entry.x
                    and cell.coords.y == entry.y
                ):
                    mid_line += " E "
                elif (
                    exit
                    and cell.coords.x == exit.x
                    and cell.coords.y == exit.y
                ):
                    mid_line += " X "
                elif (x, y) in path_set:
                    mid_line += " · "  # path marker
                else:
                    mid_line += "   "

            # Rightmost wall (only if last cell wasn't sealed)
            last_cell = self.grid[y][self.width - 1]
            if not is_sealed(last_cell):
                mid_line += f"{color[0]}|\033[0m"
            print(mid_line)

        # Bottom wall row
        bottom_line = ""
        for x in range(self.width):
            bottom_line += f"{color[0]}+---\033[0m"
        bottom_line += f"{color[0]}+\033[0m"
        print(bottom_line)
