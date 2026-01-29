def ft_different_errors(error: int) -> None:
    """
        this function takes an int as the number of error and then
        makes that error and handles it
    """
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
ft_different_errors(0)
print()
print("Testing ZeroDivisionError...")
ft_different_errors(1)
print()
print("Testing FileNotFoundError...")
ft_different_errors(2)
print()
print("Testing KeyError...")
ft_different_errors(3)
print()
print("Testing multiple errors together...")
ft_different_errors(4)
print()
print("All error types tested successfully!")
