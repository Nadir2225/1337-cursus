def check_temperature(temp_str: str) -> int:
    """
        this function checks the temperature then prints
        a message and return the correspondent message
    """
    try:
        temp_str = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return
    if temp_str > 40:
        print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
    elif temp_str < 0:
        print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
    else:
        print(f"Temperature {temp_str}°C is perfect for plants!")
        return temp_str


print("=== Garden Temperature Checker ===")
print()
print("Testing temperature: 25")
check_temperature("25")
print()
print("Testing temperature: abc")
check_temperature("abc")
print()
print("Testing temperature: 100")
check_temperature("100")
print()
print("Testing temperature: -50")
check_temperature("-50")
print()
print("All tests completed - program didn't crash!")
