from typing import Any
from pydantic import BaseModel
from .hub import Hub
from .metadata import ConnMetadata
# if TYPE_CHECKING:
#     from .drone import Drone


class Connection(BaseModel):
    zone1: Hub
    zone2: Hub
    name: str
    metadata: ConnMetadata
    drones: list = []

    @classmethod
    def create(
        self,
        key: str,
        value: str,
        created_connections: list["Connection"],
        available_hubs: list[Hub]
    ) -> "Connection":
        if (key != "connection"):
            raise Exception('wrong format')
        metadata = None
        if len(value.split(' [')) == 1:
            mand, = value.split(' [')
        else:
            mand, metadata = value.split(' [')
        name1, name2 = mand.split('-')
        if '\n' in name2:
            name2 = name2[:-1]
        zone1, zone2 = None, None
        for hub in available_hubs:
            if hub.name == name1:
                zone1 = hub
            if hub.name == name2:
                zone2 = hub
        if not zone1 or not zone2 or zone1 == zone2:
            raise Exception('mal formatted')
        metadata_obj = {}
        if metadata:
            metadata = metadata[:-1]
            metadatas = metadata.split(' ')
            keys = ['max_link_capacity']
            for md in metadatas:
                attribute, valeur = md.split('=')
                if attribute in keys:
                    metadata_obj[attribute] = valeur
                    keys.remove(attribute)
                else:
                    raise Exception('mal formatted')
        conn = Connection(
            name=f"{zone1.name}-{zone2.name}",
            zone1=zone1,
            zone2=zone2,
            metadata=ConnMetadata.from_obj(metadata_obj)
        )

        for connection in created_connections:
            if connection == conn:
                raise Exception('two connections can\'t have the same hubs')

        return conn

    def __eq__(self, other: object) -> Any:
        if not isinstance(other, Connection):
            return NotImplemented
        return (
            (self.zone1 == other.zone1 and self.zone2 == other.zone2)
            or (self.zone1 == other.zone2 and self.zone2 == other.zone1)
        )

    def hub_exists(self, hub: Hub) -> bool:
        return bool(hub == self.zone1 or hub == self.zone2)

    def get_neighbor(self, hub: Hub) -> Hub:
        if hub == self.zone1:
            return self.zone2
        elif hub == self.zone2:
            return self.zone1
