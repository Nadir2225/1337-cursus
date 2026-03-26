from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Any


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0, le=100)
    oxygen_level: float = Field(ge=0, le=100)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> Any:
    print("Space Station Data Validation")
    print("========================================")

    space = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2022-04-13T09:21:40.400+02:30",
        is_operational=True,
        notes="optional"
    )
    print("Valid station created:")
    print(f"ID: {space.station_id}")
    print(f"Name: {space.name}")
    print(f"Crew: {space.crew} people")
    print(f"Power: {space.power_level}%")
    print(f"Oxygen: {space.oxygen_level}%")
    print(f"Status: {'Operational' if space.is_operational else 'Nonoperational'}")
    print("\n========================================")

    print("Expected validation error:")
    try:
        space = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2032-04-23T10:20:30.400+02:30",
            is_operational=False,
            notes="optional",
        )
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()