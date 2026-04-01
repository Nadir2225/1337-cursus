def mage_counter() -> callable:
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def accumulator(power_gained: int):
        nonlocal power
        power += power_gained
        return power

    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    def enchanter(item_name: str):
        return f"{enchantment_type} {item_name}"

    return enchanter


def memory_vault() -> dict[str, callable]:
    vault = {}

    def store(key: str, value: str) -> None:
        vault[key] = value

    def recall(key: str) -> str:
        try:
            return vault[key]
        except KeyError:
            return "Memory not found"

    return {
        'store': store,
        'recall': recall
    }


if __name__ == '__main__':
    print("\nTesting mage counter...")
    mage_counter_v = mage_counter()
    for i in range(3):
        print(f"Call {i + 1}: {mage_counter_v()}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))
