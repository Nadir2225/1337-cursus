from typing import Optional

from pydantic import BaseModel
from .models.parsestates import ParseStates
from .models.hub import Hub
from .models.connection import Connection


class Graph(BaseModel):
    nb_drones: int
    start_hub: Hub
    end_hub: Hub
    hubs: list[Hub]
    connections: list[Connection]

    @classmethod
    def parser(self, map_path: str) -> "Graph":
        nb_drones = None
        start_hub = None
        end_hub = None
        hubs: list[Hub] = []
        connections: list[Connection] = []

        state = ParseStates.nb_drones

        with open(map_path, "r") as f:
            if len(f.readline()) == 0:
                raise Exception('empty map file')
            for line in f:
                if line[0] == '#' or line[0] == '\n':
                    continue
                line = line.strip()
                key, value = line.split(': ')
                if state == ParseStates.nb_drones:
                    if key != "nb_drones":
                        raise Exception('wrong format')
                    nb_drones = int(value)
                    state = ParseStates.start
                elif state == ParseStates.start:
                    start_hub = Hub.create(
                        key=key,
                        value=value,
                        state=ParseStates.start,
                        created_hubs=hubs
                    )
                    state = ParseStates.zones
                elif state == ParseStates.zones:
                    if (key == "end_hub"):
                        end_hub = Hub.create(
                            key=key,
                            value=value,
                            state=ParseStates.end,
                            created_hubs=hubs + [start_hub, end_hub]
                        )
                        state = ParseStates.connections
                        continue
                    hubs.append(
                        Hub.create(
                            key=key,
                            value=value,
                            state=ParseStates.zones,
                            created_hubs=hubs + [start_hub, end_hub]
                        )
                    )
                elif state == ParseStates.connections:
                    connections.append(
                        Connection.create(
                            key=key,
                            value=value,
                            created_connections=connections,
                            available_hubs=hubs + [start_hub, end_hub]
                        )
                    )
        assert nb_drones
        return Graph(
            nb_drones=nb_drones,
            start_hub=start_hub,
            end_hub=end_hub,
            hubs=hubs,
            connections=connections
        )

    def get_neighbors(self, hub: Hub) -> list[Hub]:
        l: list[Hub] = []
        for connection in self.connections:
            if connection.hub_exists(hub):
                l.append(connection.get_neighbor(hub))
        return l

    def get_connection(self, zone1: Hub, zone2: Hub) -> Optional[Connection]:
        for conn in self.connections:
            if conn.zone1 == zone1 and conn.zone2 == zone2:
                return conn
            if conn.zone1 == zone2 and conn.zone2 == zone1:
                return conn
        return None
