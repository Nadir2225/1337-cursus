from enum import Enum
from typing import List
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime


class Rank(Enum):
    cadet = 'cadet'
    officer = 'officer'
    lieutenant = 'lieutenant'
    captain = 'captain'
    commander = 'commander'


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, lt=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode='after')
    def mission_validation(self):
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        captain_or_cammander = [
            m for m in self.crew if (
                m.rank.value == Rank.captain.value
                or m.rank.value == Rank.commander.value
            )
        ]
        if len(captain_or_cammander) == 0:
            raise ValueError("Must have at least one Commander or Captain")
        experienced = [1 for m in self.crew if m.years_experience > 5]
        if self.duration_days > 365:
            if (
                sum(experienced) == 0
                or len(self.crew) / sum(experienced) < 0.5
            ):
                raise ValueError(
                    "Long missions (> 365 days) need 50%"
                    " experienced crew (5+ years)"
                )
        active_members = [1 for m in self.crew if m.is_active]
        if (sum(active_members) != len(self.crew)):
            raise ValueError("All crew members must be active")
        return self


if __name__ == '__main__':
    print("Space Mission Crew Validation")
    print("======================================")
    member1 = CrewMember(
        member_id="001",
        name="Sarah Connor",
        rank=Rank.commander,
        age=23,
        specialization="Mission Command",
        years_experience=5,
        is_active=True,
    )
    member2 = CrewMember(
        member_id="002",
        name="John Smith",
        rank=Rank.lieutenant,
        age=21,
        specialization="Navigation",
        years_experience=6,
        is_active=True,
    )
    member3 = CrewMember(
        member_id="003",
        name="Alice Johnson",
        rank=Rank.officer,
        age=33,
        specialization="Engineering",
        years_experience=4,
        is_active=True,
    )

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2020-01-02T03:04:05Z",
        duration_days=900,
        crew=[member1, member2, member3],
        budget_millions=2500.0,
    )
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value})"
            f" - {member.specialization}"
        )

    print("\n========================================")
    print("Expected validation error:")
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2020-01-02T03:04:05Z",
            duration_days=900,
            crew=[member2, member3],
            budget_millions=2500.0,
        )
    except ValidationError as e:
        print(e.errors()[0]['msg'])
