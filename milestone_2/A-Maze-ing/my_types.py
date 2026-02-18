from typing import Optional

class Coords:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    @classmethod
    def parse(cls, cords: str):
        try:
            cords_list = cords.split(',')
            if len(cords_list) != 2:
                raise ValueError('invalid coordinates')
            return cls(int(cords_list[0]), int(cords_list[1]))
        except ValueError as e:
            raise ValueError('invalid coordinates')

    def __str__(self):
        return f'({self.x}, {self.y})'

class Config:
    def __init__(
        self, 
        width: int,
        height: int,
        entry: Coords,
        exit: Coords,
        output_file: str,
        perfect: bool,
        seed: int,
    ):
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.output_file = output_file
        self.perfect = perfect
        self.seed = seed
    
    def __str__(self):
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
        # Walls: True = closed, False = open
        self.north: bool = True
        self.east: bool = True
        self.south: bool = True
        self.west: bool = True
        
        self.visited: bool = False

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

    def print_maze(self, entry: Optional[Coords] = None, exit: Optional[Coords] = None) -> None:
        """
        Print a simple ASCII representation of the maze.
        """
        for y in range(self.height):
            # Print top walls
            for x in range(self.width):
                cell = self.grid[y][x]
                print("+", end="")
                print("---" if cell.north else "   ", end="")
            print("+")  # rightmost corner

            # Print side walls and entry/exit
            for x in range(self.width):
                cell = self.grid[y][x]
                # Left wall
                print("|" if cell.west else " ", end="")

                # Cell content
                if entry and cell.coords.x == entry.x and cell.coords.y == entry.y:
                    print(" E ", end="")  # Entry
                elif exit and cell.coords.x == exit.x and cell.coords.y == exit.y:
                    print(" X ", end="")  # Exit
                else:
                    print("   ", end="")  # Empty space

            # Rightmost wall
            print("|")
        
        # Print bottom walls
        for x in range(self.width):
            print("+---", end="")
        print("+")
    