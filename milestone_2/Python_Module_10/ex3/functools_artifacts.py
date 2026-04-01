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
    return {
        "fire_enchant": functools.partial(
            base_enchantment,
            power=50,
            element="fire"
        ),
        "ice_enchant": functools.partial(
            base_enchantment,
            power=50,
            element="ice"
        ),
        "lightning_enchant": functools.partial(
            base_enchantment,
            power=50,
            element="lightning"
        )
    }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def cast_spell(spell):
        return f"Unknown spell type: {type(spell).__name__}"

    @cast_spell.register(int)
    def _(spell: int):
        return f"Casting damage spell: deals {spell} damage!"

    @cast_spell.register(str)
    def _(spell: str):
        return f"Enchantment activated: {spell}!"

    @cast_spell.register(list)
    def _(spell: list):
        return f"spells casted: {spell}"
    return cast_spell


if __name__ == "__main__":
    spell_powers = [25, 12, 20, 10, 21, 48]

    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
