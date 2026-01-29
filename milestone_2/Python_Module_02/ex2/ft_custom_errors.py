class GardenError(Exception):
    """
        customized error class for a garden error
    """
    pass


class PlantError(GardenError):
    """
        customized error class for a plant error
    """
    pass


class WaterError(GardenError):
    """
        customized error class for a water error
    """
    pass


def ft_error(plant: str, last_watring: int, tank_lvl: int):
    """
        this function raise errors for some customized conditions
    """
    try:
        if last_watring > 3 and tank_lvl < 10:
            raise GardenError(
                f"The {plant} plant is wilting!",
                "Not enough water in the tank!"
                )
        if last_watring > 3:
            raise PlantError(f"The {plant} plant is wilting!")
        if tank_lvl < 10:
            raise WaterError("Not enough water in the tank!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    except GardenError as e:
        print(f"Caught a garden error: {e.args[0]}")
        print(f"Caught a garden error: {e.args[1]}")


print("=== Custom Garden Errors Demo ===")
print()
print("Testing PlantError...")
ft_error("tomato", 4, 11)
print()
print("Testing WaterError...")
ft_error("tomato", 1, 9)
print()
print("Testing catching all garden errors...")
ft_error("tomato", 4, 9)
print()
print("All custom error types work correctly!")
