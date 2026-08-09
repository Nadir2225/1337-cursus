from enum import Enum


class ZoneType(Enum):
    priority = 0.9
    normal = 1.0
    restricted = 3.0
    blocked = -1
