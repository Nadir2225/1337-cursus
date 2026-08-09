from enum import Enum


class ParseStates(Enum):
    nb_drones = 0
    start = 1
    zones = 2
    end = 3
    connections = 4
