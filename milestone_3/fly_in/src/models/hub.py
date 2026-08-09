from typing import List, Self
from pydantic import BaseModel, model_validator
from .metadata import ZoneMetadata
from .parsestates import ParseStates
# if TYPE_CHECKING:
#     from .drone import Drone


class Hub(BaseModel):
    name: str
    x: int
    y: int
    metadata: ZoneMetadata
    drones: List = []

    @model_validator(mode='after')
    def validator(self) -> Self:
        if '-' in self.name or ' ' in self.name:
            raise ValueError('Name of a hub can\'t contain dashes nor spaces')
        return self

    @classmethod
    def create(
        self,
        key: str,
        value: str,
        state: ParseStates,
        created_hubs: list["Hub"]
    ) -> "Hub":
        if (
            state == ParseStates.start and key != "start_hub"
            or state == ParseStates.zones and key != "hub"
            or state == ParseStates.end and key != "end_hub"
        ):
            raise Exception('wrong format')
        metadata = None
        if len(value.split(' [')) == 1:
            mand, = value.split(' [')
        else:
            mand, metadata = value.split(' [')
        name, x, y = mand.split(' ')
        if metadata:
            metadata = metadata[:-1]
            metadatas = metadata.split(' ')
            metadata_obj = {}
            keys = ['zone', 'color', 'max_drones']
            for md in metadatas:
                attribute, valeur = md.split('=')
                if attribute in keys:
                    metadata_obj[attribute] = valeur
                    keys.remove(attribute)
                else:
                    raise Exception('mal formatted')
        return_hub = Hub(
            name=name,
            x=int(x),
            y=int(y),
            metadata=ZoneMetadata.from_obj(metadata_obj),
        )

        for hub in created_hubs:
            if hub == return_hub:
                raise Exception("you can't name 2 hubs with the same name :(")

        return return_hub

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Hub):
            return NotImplemented
        return self.name == other.name
