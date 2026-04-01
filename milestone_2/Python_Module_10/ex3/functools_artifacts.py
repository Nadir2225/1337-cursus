import functools
import operator

def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        raise ValueError("Invalid operation")

    func = operations[operation]

    return functools.reduce(func, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
	return
def memoized_fibonacci(n: int) -> int:
	return
def spell_dispatcher() -> callable:
	return 

if __name__ == "__main__":
	spell_powers = [14, 42, 34, 24, 49, 37]
	operations = ['add', 'multiply', 'max', 'min']
	fibonacci_tests = [9, 15, 17]

	print("\nTesting spell reducer...")
	print(f"Sum: {spell_reducer(spell_powers, 'add')}")
	print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
	print(f"Max: {spell_reducer(spell_powers, 'max')}")

	# print("\nTesting memoized fibonacci...")
	# print(f"Fib(10): {memoized_fibonacci(10)}")
	# print(f"Fib(15): {memoized_fibonacci(15)}")
