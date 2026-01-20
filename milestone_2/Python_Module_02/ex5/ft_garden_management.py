class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, water: int, sun: int):
        self._name = name
        self._water = water
        self._sun = sun


class GardenManager:
    plants = []

    def __init__(self, name, tank):
        self._name = name
        self._tank = tank

    def add_plant(self, name: str, water: int, sun: int):
        if not (GardenManager.check_plant_health(name)):
            return
        GardenManager.plants.append(Plant(name, water, sun))
        print(f"Added {name} successfully")

    def water_plants(self):
        print("Opening watering system")
        try:
            for plant in GardenManager.plants:
                if isinstance(plant._name, str):
                    print(f"Watering {plant._name} - success")
                else:
                    raise TypeError
        except TypeError:
            print(f"Error: Cannot water {plant} - invalid plant!")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(plant_name):
        try:
            if plant_name == "":
                raise ValueError(
                    "Error adding plant: Plant name cannot be empty!"
                    )
        except ValueError as e:
            print(e)
            return 0
        return 1

    def check_plant_health_print(self):
        for plant in self.plants:
            try:
                if plant._water < 1:
                    raise ValueError(
                        "Error checking lettuce: Water level"
                        f" {plant._water} is too low (min 1)"
                        )
                elif plant._water > 10:
                    raise ValueError(
                        f"Error checking lettuce: Water level"
                        f" {plant._water} is too high (max 10)"
                        )
                elif plant._sun < 2:
                    raise ValueError(
                        "Error checking lettuce: Sunlight"
                        f" hours {plant._sun} is too low (min 2)"
                        )
                elif plant._sun > 12:
                    raise ValueError(
                        "Error checking lettuce: Sunlight"
                        " hours {plant._sun} is too high (max 12)"
                        )
                else:
                    print(
                        f"{plant._name}: healthy (water:"
                        f" {plant._water}, sun: {plant._sun})"
                        )
            except ValueError as e:
                print(e)

    def tank_check(self):
        try:
            if self._tank < 10:
                raise GardenError(
                    "Caught GardenError: Not enough water in tank"
                    )
        except GardenError as e:
            print(e)


print("=== Garden Management System ===")
garden = GardenManager("nadir", 6)
print()
print("Adding plants to garden...")
garden.add_plant("tomate", 5, 8)
garden.add_plant("lettuce", 15, 8)
garden.add_plant("", 3, 3)
print()
print("Watering plants...")
garden.water_plants()
print()
print("Checking plant health...")
garden.check_plant_health_print()
print()
print("Testing error recovery...")
garden.tank_check()
print("System recovered and continuing...")
print()
print("Garden management system test complete!")
