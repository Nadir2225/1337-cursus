def garden_operations(error):
    try:
        if error == 0:
            int("abc")
        elif error == 1:
            10 / 0
        elif error == 2:
            open("missing.txt")
        elif error == 3:
            {}["missing_plant"]
        else:
            foo = []
            foo[3]
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    except Exception:
        print("Caught an error, but program continues!")


print("=== Garden Error Types Demo ===")
print()
print("Testing ValueError...")
garden_operations(0)
print()
print("Testing ZeroDivisionError...")
garden_operations(1)
print()
print("Testing FileNotFoundError...")
garden_operations(2)
print()
print("Testing KeyError...")
garden_operations(3)
print()
print("Testing multiple errors together...")
garden_operations(4)
print()
print("All error types tested successfully!")
