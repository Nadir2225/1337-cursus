from .my_types import Cell, Config, Maze


def cell_to_bin(cell: Cell) -> str:
    return (
        ('1' if cell.west else '0') +
        ('1' if cell.south else '0') +
        ('1' if cell.east else '0') +
        ('1' if cell.north else '0')
    )


def bin_to_hex(bin_str: str) -> str:
    hex_str = ''
    for i in range(0, len(bin_str), 4):
        four_bits = bin_str[i:i+4]
        hex_digit = hex(int(four_bits, 2))[2:]
        hex_str += hex_digit
    return hex_str.upper()


def generate_output_file(maze: Maze, config: Config, solve: str) -> None:
    EXCLUDES = [
        "Makefile", "config.txt", "a_maze_ing.py",
        "pyproject.toml", "README.md", "./Makefile",
        "./config.txt", "./a_maze_ing.py", "./pyproject.toml",
        "./README.md"
    ]
    if config.output_file is None:
        return
    if config.output_file in EXCLUDES:
        raise FileExistsError("wrong output file name")
    with open(config.output_file, 'w') as f:
        for row in maze.grid:
            bin_row = ''.join(cell_to_bin(cell) for cell in row)
            hex_row = bin_to_hex(bin_row)
            f.write(hex_row + '\n')
        f.write(f'\n{config.entry.x},{config.entry.y}\n')
        f.write(f'{config.exit.x},{config.exit.y}\n')
        f.write(solve + '\n')
