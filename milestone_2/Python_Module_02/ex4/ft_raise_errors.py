def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        if plant_name == "":
            raise ValueError("Error: Plant name cannot be empty!")
        elif water_level < 1:
            raise ValueError(
                f"Water level {water_level} is too low (min 1)"
                )
        elif water_level > 10:
            raise ValueError(
                f"Water level {water_level} is too high (max 10)"
                )
        elif sunlight_hours < 2:
            raise ValueError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)"
                )
        elif sunlight_hours > 12:
            raise ValueError(
                f"Sunlight hours {water_level} is too high (max 12)"
                )
        else:
            return (f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(e)


print("=== Garden Plant Health Checker ===")
print()
print("Testing good values...")
print(check_plant_health("tomate", 9, 10))
print()
print("Testing empty plant name...")
check_plant_health("", 9, 10)
print()
print("Testing bad water level...")
check_plant_health("tomate", 15, 10)
print()
print("Testing bad sunlight hours...")
check_plant_health("tomate", 9, 0)
print()
print("All error raising tests completed!")
