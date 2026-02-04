import sys

class ConfigSyntaxError(Exception):
    pass

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
            config_object = Config(
                width=int(config_dict.get('WIDTH')),
                height=int(config_dict.get('HEIGHT')),
                entry=Coords.parse(config_dict.get('ENTRY')),
                exit=Coords.parse(config_dict.get('EXIT')),
                output_file=config_dict.get('OUTPUT_FILE'),
                perfect=str_to_bool(config_dict.get('PERFECT')),
                seed=int(config_dict.get('SEED', 10))
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
    print(config)
