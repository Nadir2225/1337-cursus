from ex0 import Card, CreatureCard
from ex2 import Combatable, Magical, EliteCard

if __name__ == "__main__":
    print("\n=== DataDeck Ability System ===")
    print("\nEliteCard capabilities:")
    card_methods = [
        method for method in dir(Card) if not method.startswith("_")
    ]
    combatable_methods = [
        method for method in dir(Combatable) if not method.startswith("_")
    ]
    magical_methods = [
        method for method in dir(Magical) if not method.startswith("_")
    ]
    print(f"- Card: {card_methods}")
    print(f"- Combatable: {combatable_methods}")
    print(f"- Magical: {magical_methods}")

    arcane_worrior = EliteCard(
        name="Arcane Warrior", cost=5, rarity="Legendary"
    )

    print(f"\nPlaying {arcane_worrior.name} (Elite Card):")

    print("\nCombat phase:")
    target = CreatureCard(
        name='Enemy', cost=2, rarity='Common', health=10, attack=5
    )
    print(f"Attack result: {arcane_worrior.attack(target=target)}")
    print(f"Defense result: {arcane_worrior.defend(incoming_damage=5)}")

    print("\nMagic phase:")
    targets = [
        CreatureCard(
            name='Enemy 1', cost=2, rarity='Common', health=10, attack=5
        ),
        CreatureCard(
            name='Enemy 2', cost=2, rarity='Common', health=10, attack=5
        )
    ]
    print(
        f"Spell cast: "
        f"{arcane_worrior.cast_spell(spell_name='Fireball', targets=targets)}"
    )
    print(f"Mana channel: {arcane_worrior.channel_mana(amount=3)}")
    print("\nMultiple interface implementation successful!")
