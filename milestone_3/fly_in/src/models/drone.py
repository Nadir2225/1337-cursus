from typing import List, Union
from .connection import Connection
from .hub import Hub


class Drone:
    """A single drone moving along a precomputed path from start to end."""

    drone_id = 1

    def __init__(self, path: List[Hub], start: Hub, end: Hub) -> None:
        """Assign the drone the next sequential id and its route."""
        self.id = Drone.drone_id
        self.path: List[Hub] = path
        self.pos: int = 0
        self.in_transit: bool = False
        self.current_zone: Union[Hub, Connection] = start
        self.end_zone: Hub = end
        Drone.drone_id += 1

    def __repr__(self) -> str:
        return f"D{self.id}"

    def delivered(self) -> bool:
        """Whether the drone has reached its destination zone."""
        return bool(self.current_zone == self.end_zone)
