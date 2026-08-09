from typing import Dict, List, Optional, Union
from .colors import colorize, zone_color
from .models.zonetype import ZoneType
from .models.drone import Drone
from .models.hub import Hub
from .models.connection import Connection
from .pathfinder import Pathfinder
from .graph import Graph


class Simulation():

    def __init__(self, graph: Graph):
        self.graph: Graph = graph
        self.paths_by_cost: Dict[float, List[List[Hub]]] = (
            Pathfinder(graph).pathfinding()
        )
        self.paths: List[List[Hub]] = []
        self.drones: List[Drone] = []
        self.used_conn: Dict[str, int] = {}

    def run(self) -> None:
        self.setup_drones()
        all_turns: List[str] = []

        while not self.all_delivered():
            turn_moves: str = self.play_turn()
            if turn_moves:
                all_turns.append(turn_moves)
            else:
                break

        for turn_num, turn in enumerate(all_turns, start=1):
            print(f"Turn {turn_num}: {turn}")

        print("Total Turns", len(all_turns))

    def play_turn(self) -> str:
        turn_moves: List[str] = []
        n_p = [ZoneType.normal, ZoneType.priority]

        for conn in self.graph.connections:
            self.used_conn[conn.name] = len(conn.drones)

        for drone in self.drones:
            if drone.delivered():
                continue

            current = drone.path[drone.pos]
            next = drone.path[drone.pos + 1]
            connection = self.linked_connection(current, next)

            assert connection is not None

            if next.metadata.zone_type in n_p:
                if len(next.drones) == next.metadata.max_drones:
                    continue

                if self.used_conn[
                    connection.name
                ] == connection.metadata.max_link_capacity:
                    continue

                self.used_conn[connection.name] += 1
                self.move_drone(
                    drone,
                    current,
                    next
                )
                label = colorize(next.name, zone_color(next))
                turn_moves.append(f"D{drone.id}-{label}")
            elif next.metadata.zone_type == ZoneType.restricted:
                if drone.in_transit:
                    if len(next.drones) >= next.metadata.max_drones:
                        continue
                    self.move_drone(drone, connection, next)
                    drone.in_transit = False
                    label = colorize(next.name, zone_color(next))
                    turn_moves.append(f"D{drone.id}-{label}")
                else:
                    reserved = len(next.drones) + len(connection.drones)
                    if reserved >= next.metadata.max_drones:
                        continue

                    if self.used_conn[
                        connection.name
                    ] >= connection.metadata.max_link_capacity:
                        continue

                    self.used_conn[connection.name] += 1
                    self.move_drone(drone, current, connection, True)
                    drone.in_transit = True
                    label = (
                        f"{colorize(current.name, zone_color(current))}-"
                        f"{colorize(next.name, zone_color(next))}"
                    )
                    turn_moves.append(f"D{drone.id}-{label}")

        if turn_moves:
            return " ".join(turn_moves)
        else:
            return ""

    def setup_drones(self) -> None:
        for conn in self.graph.connections:
            self.used_conn[conn.name] = 0

        self.graph.start_hub.metadata.max_drones = self.graph.nb_drones
        self.graph.end_hub.metadata.max_drones = self.graph.nb_drones

        self.paths = [
            path for paths in self.paths_by_cost.values() for path in paths
        ]

        for i in range(self.graph.nb_drones):
            path = self.paths[i % len(self.paths)]
            d = Drone(
                path=path,
                start=self.graph.start_hub,
                end=self.graph.end_hub
            )
            self.drones.append(d)

    def all_delivered(self) -> bool:
        """whether every drone has reached the graph's end zone."""
        assert self.graph.end_hub is not None
        return bool(len(self.graph.end_hub.drones) == self.graph.nb_drones)

    def linked_connection(
        self, current: Hub, next: Hub
    ) -> Optional[Connection]:
        """find the connection between two zone names, in either direction."""
        for conn in self.graph.connections:
            if conn.hub_exists(current) and conn.hub_exists(next):
                return conn
        return None

    def move_drone(
            self,
            drone: Drone,
            fromm: Union[Hub, Connection],
            to: Union[Hub, Connection],
            to_conn: bool = False) -> None:
        """move a drone from one zone/connection to another."""

        if not to_conn:
            drone.pos += 1

        drone.current_zone = to
        if drone in fromm.drones:
            fromm.drones.remove(drone)
        to.drones.append(drone)

    def print_path(self, path: Dict[float, List[List[Hub]]]) -> None:
        for cost, p in path.items():
            print(f"cost is {cost}")
            for pth in p:
                print('=> ', end='')
                for index, hub in enumerate(pth):
                    if index == len(pth) - 1:
                        print(f'{hub.name}')
                    else:
                        print(f'{hub.name}-', end='')
