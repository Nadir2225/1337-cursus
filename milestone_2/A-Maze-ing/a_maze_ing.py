import sys
from my_types import Config, Coords
from maze_generator import MazeGenerator
from adnane import solve_maze_shortest

class ConfigSyntaxError(Exception):
    pass

def str_to_bool(s: str) -> bool:
    if s == "True":
        return True
    elif s == "False":
        return False
    else:
        raise ValueError(f"Invalid boolean string: {s}")

def validate_config(filename: str) -> Config:
    try:
        with open(filename, 'r') as f:
            valid_keys = ['WIDTH', 'HEIGHT', 'ENTRY', 'EXIT', 'OUTPUT_FILE', 'PERFECT']
            optional_keys = ['SEED']
            base_keys = valid_keys + optional_keys
            lines = f.readlines()
            for line in lines:
                line = line.rstrip('\n')
                if (line[0] == '#'):
                    continue
                line = line.split('=')
                if (len(line) != 2):
                    raise ConfigSyntaxError('syntax error')
                if line[0] in valid_keys or line[0] in optional_keys:
                    valid_keys.remove(line[0]) if line[0] in valid_keys else optional_keys.remove(line[0])
                elif line[0] in base_keys:
                    raise ConfigSyntaxError(f'duplicated key: {line[0]}')
                else:
                    raise ConfigSyntaxError(f'invalid key: {line[0]}')
            if len(valid_keys) > 0:
                raise ConfigSyntaxError(f'missing keys: {valid_keys}')
            # f.seek(0)
            # lines = f.readlines()
            config_dict = {line.rstrip('\n').split('=')[0]: line.rstrip('\n').split('=')[1] for line in lines if line[0] != '#'}
            seed_value = config_dict.get('SEED')
            if seed_value is not None:
                seed_value = int(seed_value)
            else:
                seed_value = None
            config_object = Config(
                width=int(config_dict.get('WIDTH')),
                height=int(config_dict.get('HEIGHT')),
                entry=Coords.parse(config_dict.get('ENTRY')),
                exit=Coords.parse(config_dict.get('EXIT')),
                output_file=config_dict.get('OUTPUT_FILE'),
                perfect=str_to_bool(config_dict.get('PERFECT')),
                seed=seed_value
            )
            return config_object
    except PermissionError as e:
        print('grant permissions')
        sys.exit(1)
    except FileNotFoundError as e:
        print('file not found')
        sys.exit(1)
    except ConfigSyntaxError as e:
        print(e)
        sys.exit(1)
    except ValueError as e:
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("you should specify the config file's name")
        sys.exit()
    config = validate_config(sys.argv[1])
    # print(config)
    maze_gen = MazeGenerator(config)
    maze_gen.generate()
    maze = maze_gen.maze
    print(solve_maze_shortest(maze, config.entry, config.exit))