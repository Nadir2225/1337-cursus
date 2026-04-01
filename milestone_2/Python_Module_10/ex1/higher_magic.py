from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spells():
        return f"{spell1()}, {spell2()}"

    return combined_spells


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def mult():
        return base_spell() * multiplier

    return mult


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster():
        if condition():
            return spell()
        return "Spell fizzled"

    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence():
        result = []
        for spell in spells:
            result.append(spell())
        return result

    return sequence


if __name__ == '__main__':
    print("\nTesting spell combiner...")
    print("Combined spell result: ", end="")
    comb = spell_combiner(lambda: "Fireball hits Dragon",
                          lambda: "Heals Dragon")
    print(comb())

    print("\nTesting power amplifier...")

    def fireball():
        return 10

    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball()}, Amplified: {mega_fireball()}")
