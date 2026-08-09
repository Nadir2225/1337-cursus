import heapq
from itertools import count
from typing import Dict, List
from .graph import Graph
from .models.hub import Hub
from .models.zonetype import ZoneType


class Pathfinder:
    """Finds least-cost routes from a graph's start zone to its end zone."""

    def __init__(self, graph: Graph) -> None:
        self.graph = graph

    def pathfinding(self) -> Dict[float, List[List[Hub]]]:
        start = self.graph.start_hub
        end = self.graph.end_hub
        paths: Dict[float, List[List[Hub]]] = {}
        total_paths_found = 0
        counter = count()
        queue: list[tuple[float, int, list[Hub]]] = [
            (0.0, next(counter), [start])
        ]

        while queue and total_paths_found < 2:
            current_cost, _, current_path = heapq.heappop(queue)
            current_zone = current_path[-1]

            if current_zone == end:
                if current_cost in paths:
                    paths[current_cost].append(current_path)
                else:
                    paths[current_cost] = [current_path]
                total_paths_found += 1
                continue

            neighbors = self.graph.get_neighbors(current_zone)

            for neighbor in neighbors:
                if neighbor in current_path:
                    continue
                if neighbor.metadata.zone_type.value == ZoneType.blocked.value:
                    continue

                connection = self.graph.get_connection(current_zone, neighbor)
                next_mlc = (
                    connection.metadata.max_link_capacity
                    if connection.metadata else 1
                )
                max_drones = neighbor.metadata.max_drones
                if next_mlc is None:
                    next_mlc = 1
                if max_drones is None:
                    max_drones = 1
                next_cost = neighbor.metadata.zone_type.value - (
                    1 - (1/min(next_mlc, max_drones))
                )
                heapq.heappush(
                    queue,
                    (
                        current_cost + next_cost,
                        next(counter),
                        current_path + [neighbor]
                    )
                )
        if not paths:
            raise ValueError("The end goal is not reachable.")
        return paths
