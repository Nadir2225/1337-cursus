import sys
import math

def calc_distance(pos: tuple) -> float:
    x1, y1, z1 = (0, 0, 0)
    x2, y2, z2 = pos
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return dist

def create_position(x: int, y: int, z: int) -> tuple:
    pos = (x, y, z)
    print(F'Position created: {pos}')
    return pos


def parse_position(pos_str: str) -> tuple:
    try:
        pos = tuple(int(x) for x in pos_str.split(','))
        print(f'Parsing coordinates: "{pos_str}"')
        print(f'Parsed position: {pos}')
        return pos
    except ValueError as e:
        print(f'Parsing invalid coordinates: "{pos_str}"')
        print(f'Error parsing coordinates: {e}')
        print(f'Error details - Type: {e.__class__.__name__}, Args: {e.args}')
    return (0, 0, 0)


def ft_coordinate_system():
    print('=== Game Coordinate System ===')
    p1 = create_position(10, 20, 5)
    print(f'Distance between (0, 0, 0) and {p1}: {calc_distance(p1) : .2f}')
    calc_distance(p1)
    print()
    p2 = parse_position("3,4,0")
    print(f'Distance between (0, 0, 0) and {p2}: {calc_distance(p2)}')
    print()
    p3 = parse_position("abc,def,ghi")
    print()
    print('Unpacking demonstration:')
    x, y, z = p2
    print(f'Player at x={x}, y={y}, z={z}')
    print(f'Coordinates: X={p2[0]}, Y={p2[1]}, Z={p2[2]}')


if __name__ == '__main__':
    ft_coordinate_system()