class GardenError(Exception):
    """
        customized error class for a garden error
    """
    pass


class WaterError(GardenError):
    """
        customized error class for a water error
    """
    pass


class SunError(GardenError):
    """
        customized error class for a sun error
    """
    pass


class Plant:
    """
        this is a class to represent a plant
    """
    def __init__(self, name: str, water: int, sun: int):
        """
            this is a constructor for the plant
        """
        self._name = name
        self._water = water
        self._sun = sun


class GardenManager:
    """
        this is a class for the garden managers
    """
    plants = []

    def __init__(self, name, tank):
        """
            this is a constructor for the garden manager
        """
        self._name = name
        self._tank = tank

    def add_plant(self, name: str, water: int, sun: int):
        """
            this is a methode for adding new plants to the garden
        """
        try:
            if (name == ''):
                raise ValueError(
                    'Error adding plant: Plant name cannot be empty!'
                )
            GardenManager.plants.append(Plant(name, water, sun))
            print(f"Added {name} successfully")
        except ValueError as e:
            print(e)

    def water_plants(self, water_level: int):
        """
            this is a methode for watering the plants
        """
        print("Opening watering system")
        for plant in GardenManager.plants:
            self._tank -= water_level
            plant._water += water_level
            print(f'Watering {plant._name} - success')
        print("Closing watering system (cleanup)")

    def check_plant_health_print():
        """
            this is a methode for checking if the plant health
        """
        for plant in GardenManager.plants:
            try:
                if plant._water < 1:
                    raise WaterError(
                        "Error checking lettuce: Water level"
                        f" {plant._water} is too low (min 1)"
                        )
                elif plant._water > 10:
                    raise WaterError(
                        f"Error checking lettuce: Water level"
                        f" {plant._water} is too high (max 10)"
                        )
                elif plant._sun < 2:
                    raise SunError(
                        "Error checking lettuce: Sunlight"
                        f" hours {plant._sun} is too low (min 5)"
                        )
                elif plant._sun > 12:
                    raise SunError(
                        "Error checking lettuce: Sunlight"
                        " hours {plant._sun} is too high (max 10)"
                        )
                else:
                    print(
                        f"{plant._name}: healthy (water:"
                        f" {plant._water}, sun: {plant._sun})"
                        )
            except GardenError as e:
                print(e)

    def tank_check(self):
        """
            this is a methode for checking if the tank has enough water
        """
        try:
            if self._tank < 10:
                raise WaterError(
                    "Caught GardenError: Not enough water in tank"
                    )
        except WaterError as e:
            print(e)
        finally:
            print("System recovered and continuing...")


print("=== Garden Management System ===")
garden = GardenManager("nadir", 16)
print()
print("Adding plants to garden...")
garden.add_plant("tomate", 0, 8)
garden.add_plant("lettuce", 10, 8)
garden.add_plant("", 3, 3)
print()
print("Watering plants...")
garden.water_plants(5)
print()
print("Checking plant health...")
GardenManager.check_plant_health_print()
print()
print("Testing error recovery...")
garden.tank_check()
print()
print("Garden management system test complete!")
