def water_plants(plant_list: list):
    print("Opening watering system")
    try:
        for plant in plant_list:
            if isinstance(plant, str):
                print(f"Watering {plant}")
            else:
                raise TypeError
    except TypeError:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


print("=== Garden Watering System ===")
print()
print("Testing normal watering...")
water_plants(["tomato", "lettuce", "carrots"])
print("Watering completed successfully!")
print()
print("Testing with error...")
water_plants(["tomato", None])
print()
print("Cleanup always happens, even with errors!")
