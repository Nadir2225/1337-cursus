def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined_spells():
        return f"{spell1()}, {spell2()}"
    return combined_spells


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def mult():
        return base_spell() * multiplier
    return mult


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster():
        if condition():
            return spell()
        else:
            return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence():
        result = []
        for spell in spells:
            result.append(spell())
        return result
    return sequence


if __name__ == '__main__':
    print("\nTesting spell combiner...")
    print("Combined spell result: ", end="")
    comb = spell_combiner(
        lambda: "Fireball hits Dragon",
        lambda: "Heals Dragon"
    )
    print(f"{comb()}")
    print("\nTesting power amplifier...")

    def fireball() -> int:
        return 10
    mega_fireball = power_amplifier(fireball, 3)
    print(
        f"Original: {fireball()}, "
        f"Amplified: {mega_fireball()}"
    )
