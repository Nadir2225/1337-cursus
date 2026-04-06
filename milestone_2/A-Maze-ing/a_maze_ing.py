from typing import Optional, Tuple, Any
import sys
from mazegen import (
    generate_output_file,
    MazeGenerator,
    solve_maze_shortest,
    Config, Coords
)
import os


class ConfigSyntaxError(Exception):
    pass


class MazeDimensionsError(Exception):
    pass


class OutOfMazeError(Exception):
    pass


class ChoiceError(Exception):
    def __init__(self, choice: str, *args: Tuple[Any, ...]) -> None:
        super().__init__(*args)
        self.choice = choice


def str_to_bool(s: Optional[str]) -> bool:
    if s is None:
        raise ValueError(f"Invalid boolean string: {s}")
    else:
        if s.lower() == "true":
            return True
        elif s.lower() == "false":
            return False
        else:
            raise ValueError(f"Invalid boolean string: {s}")


def validate_config(filename: str) -> Config:
    try:
        with open(filename, 'r') as f:
            valid_keys = [
                'WIDTH', 'HEIGHT', 'ENTRY',
                'EXIT', 'OUTPUT_FILE', 'PERFECT'
            ]
            optional_keys = ['SEED']
            base_keys = valid_keys + optional_keys
            lines = f.readlines()
            for line in lines:
                if (line[0] == '\n'):
                    continue
                line = line.rstrip('\n')
                if (line[0] == '#'):
                    continue
                splitted_line = line.split('=')
                if (len(splitted_line) != 2):
                    raise ConfigSyntaxError('syntax error')
                if (
                    (splitted_line[0].strip()).upper() in valid_keys
                    or (splitted_line[0].strip()).upper() in optional_keys
                ):
                    (
                        valid_keys.remove((splitted_line[0].strip()).upper())
                        if (splitted_line[0].strip()).upper() in valid_keys
                        else optional_keys.remove(
                            (splitted_line[0].strip()).upper()
                        )
                    )
                elif (splitted_line[0].strip()) in base_keys:
                    raise ConfigSyntaxError(
                        f'duplicated key: {(splitted_line[0].strip())}'
                    )
                else:
                    raise ConfigSyntaxError(
                        f'invalid key: {splitted_line[0].strip()}'
                    )
            if len(valid_keys) > 0:
                raise ConfigSyntaxError(f'missing keys: {valid_keys}')
            # f.seek(0)
            # lines = f.readlines()
            config_dict = {
                (line.rstrip('\n').split('=')[0].strip()).upper():
                (line.rstrip('\n').split('=')[1].strip())
                for line in lines if (line[0] != '\n' and line[0] != '#')
            }
            width_value = config_dict.get('WIDTH')
            if width_value is not None:
                width = int(width_value)
            height_value = config_dict.get('HEIGHT')
            if height_value is not None:
                height = int(height_value)
            entry_value = Coords.parse(config_dict.get('ENTRY')),
            exit_value = Coords.parse(config_dict.get('EXIT')),
            if entry_value == exit_value:
                raise ValueError(
                    "entry and exit cannot have the same coordinates"
                )
            config_object = Config(
                width=width,
                height=height,
                entry=entry_value[0],
                exit=exit_value[0],
                output_file=config_dict.get('OUTPUT_FILE'),
                perfect=str_to_bool(config_dict.get('PERFECT')),
                seed=config_dict.get('SEED')
            )
            if config_object.width < 8 or config_object.height < 8:
                raise MazeDimensionsError
            if (
                config_object.entry.x >= config_object.width
                or config_object.exit.x >= config_object.width
            ):
                raise OutOfMazeError
            if (
                config_object.entry.y >= config_object.height
                or config_object.exit.y >= config_object.height
            ):
                raise OutOfMazeError
            return config_object
    except PermissionError:
        print('grant permissions')
        sys.exit(1)
    except FileNotFoundError:
        print('file not found')
        sys.exit(1)
    except MazeDimensionsError:
        print('maze should at least be 8x8')
        sys.exit(1)
    except OutOfMazeError:
        print('Out of Maze Error: entry and exit should belong to the maze')
        sys.exit(1)
    except ConfigSyntaxError as e:
        print(e)
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)
    # except IndexError:
    #     print('config file is empty')
    #     sys.exit(1)


def solve_to_path(entry: Coords, solve: str) -> set[tuple[int, int]]:
    directions = {
        'N': (0, -1),
        'E': (1, 0),
        'S': (0, 1),
        'W': (-1, 0)
    }
    path = set()
    current = (entry.x, entry.y)
    for move in solve:
        dx, dy = directions[move]
        current = (current[0] + dx, current[1] + dy)
        path.add(current)
    return path


def display_menu() -> int:
    print("==== A-Maze-ing ====")
    print("1. Re-generate a new maze")
    print("2. Show/hide path from entry to exit")
    print("3. Rotate maze colors")
    print("4. Quit")
    inp = input("choice? (1-4): ")
    choices = ['1', '2', '3', '4']
    if inp not in choices:
        raise ChoiceError(inp)
    return int(inp)


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    colors = [
        ("\033[31m", "\033[32m"),  # red walls, green path
        ("\033[34m", "\033[33m"),  # blue walls, yellow path
        ("\033[35m", "\033[36m"),  # magenta walls, cyan path
        ("\033[32m", "\033[31m"),  # green walls, red path
        ("\033[36m", "\033[35m"),  # cyan walls, magenta path
        ("\033[33m", "\033[34m"),  # yellow walls, blue path
        ("\033[37m", "\033[90m"),  # default white walls, grey path
    ]
    DEFAULT = ("\033[37m", "\033[90m")
    color = DEFAULT
    if len(sys.argv) != 2:
        print("you should specify the config file's name")
        sys.exit()
    config = validate_config(sys.argv[1])
    seed_configured = config.seed is not None
    path = None
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        # print(config)
        try:
            maze_gen = MazeGenerator(config)
            maze_gen.generate()
            maze = maze_gen.maze
            solve = solve_maze_shortest(maze, config.entry, config.exit)
            generate_output_file(maze, config, solve)
            maze.print_maze(
                color=color,
                entry=config.entry,
                exit=config.exit,
                path_cells=path
            )
            # print(path)
            choice = display_menu()
            if choice == 1:
                if not seed_configured:
                    config.seed = None
                path = None
            else:
                if not seed_configured:
                    config.seed = maze_gen.config.seed
            if choice == 2:
                if path is None:
                    path = solve_to_path(config.entry, solve)
                else:
                    path = None
                continue
            if choice == 3:
                color = colors[(colors.index(color) + 1) % len(colors)]
                continue
            if choice == 4:
                break
            # os.system('cls' if os.name == 'nt' else 'clear')
            # if os.name == 'nt':
            #     print('\033c', end="")
        except ChoiceError as e:
            print(f'invalid choice input: {e.choice}')
        except Exception as e:
            print(e)
            sys.exit(1)
        except BaseException:
            os.system('cls' if os.name == 'nt' else 'clear')
            if os.name == 'nt':
                print('\033c', end="")
            continue
