class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def get_info(self):
        print(f'{self._name}: {self._height}cm , {self._age} days old')


def plant_factory(platns: list[dict[str, int | str]]) -> list[Plant]:
    plants_list = []
    print('=== Plant Factory Output ===')
    i = 0
    while i < len(plants):
        plants_list.append(
            Plant(
                plants[i]["name"],
                plants[i]["starting_height"],
                plants[i]["starting_age"]
            )
        )
        print(
            f'Created: {plants[i]["name"]} '
            f'({plants[i]["starting_height"]}cm, '
            f'{plants[i]["starting_age"]} days)'
        )
        i += 1
    print(f'Total plants created: {i}')
    return plants_list


plants = [
    {"name": "Rose", "starting_height": 25, "starting_age": 30},
    {"name": "Oak", "starting_height": 200, "starting_age": 365},
    {"name": "Cactus", "starting_height": 5, "starting_age": 90},
    {"name": "Sunflower", "starting_height": 80, "starting_age": 45},
    {"name": "Fern", "starting_height": 15, "starting_age": 120}
]

plant_factory(plants)
