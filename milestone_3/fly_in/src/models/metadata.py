from typing import Optional
from pydantic import BaseModel
from .zonetype import ZoneType


class ZoneMetadata(BaseModel):
    zone_type: ZoneType
    color: Optional[str]
    max_drones: int

    @classmethod
    def from_obj(self, obj: dict[str, str]) -> Optional["ZoneMetadata"]:
        if not obj:
            return ZoneMetadata(
                zone_type=ZoneType.normal,
                max_drones=1,
                color=None
            )
        zone_type = obj.get("zone", None)

        if (zone_type == "normal" or zone_type is None):
            zone_type = ZoneType.normal
        elif (zone_type == "priority"):
            zone_type = ZoneType.priority
        elif (zone_type == "restricted"):
            zone_type = ZoneType.restricted
        elif (zone_type == "blocked"):
            zone_type = ZoneType.blocked
        else:
            raise Exception("mal formatted")

        temp_max_drones = obj.get("max_drones", "1")

        max_drones = int(temp_max_drones)

        return ZoneMetadata(
            zone_type=zone_type,
            color=obj.get("color", None),
            max_drones=max_drones
        )


class ConnMetadata(BaseModel):
    max_link_capacity: int

    @classmethod
    def from_obj(self, obj: dict[str, str]) -> Optional["ConnMetadata"]:
        if not obj:
            return ConnMetadata(
                max_link_capacity=1
            )
        if len(obj.keys()) != 1:
            raise Exception('mal formatted')
        temp_max_link_capacity = obj.get("max_link_capacity", "1")
        max_link_capacity = int(temp_max_link_capacity)
        return ConnMetadata(
            max_link_capacity=max_link_capacity
        )
