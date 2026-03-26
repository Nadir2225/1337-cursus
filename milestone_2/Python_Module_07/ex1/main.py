from ex0 import CreatureCard, Card
from ex1 import ArtifactCard, Deck, SpellCard


def card_type(card: Card) -> str:
    if isinstance(card, CreatureCard):
        return "Creature"
    elif isinstance(card, SpellCard):
        return "Spell"
    elif isinstance(card, ArtifactCard):
        return "Artifact"
    else:
        return "Unknown Card Type"


if __name__ == "__main__":
    print("\n=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")
    deck = Deck()
    deck.add_card(
        SpellCard(
            name="Lightning Bolt", cost=3, rarity="Common",
            effect_type="Damage"
        )
    )
    deck.add_card(
        ArtifactCard(
            name="Mana Crystal", cost=2, rarity="Rare",
            durability=3, effect="Equip"
        )
    )
    deck.add_card(
        CreatureCard(
            name="Fire Dragon", cost=5, rarity="Legendary",
            attack=7, health=5
        )
    )
    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")

    while (deck.cards):
        card = deck.draw_card()
        print(f"\nDrew: {card.name} ({card_type(card)})")
        print(f"Play result: {card.play({})}")

    print(
        "\nPolymorphism in action: Same interface, different card behaviors!"
    )
