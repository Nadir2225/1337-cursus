from ex0.CreatureCard import CreatureCard


if __name__ == '__main__':
    print("\n=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")

    fire_dragon = CreatureCard(
        name="Fire Dragon", cost=5, rarity="Legendary",
        attack=7, health=5
    )
    goblin_warrior = CreatureCard(
        name="Goblin Warrior", cost=5, rarity="Legendary",
        attack=7, health=5
    )

    print("\nCreatureCard Info:")
    print(fire_dragon.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {fire_dragon.is_playable(available_mana=6)}")
    print(f"Play Result: {fire_dragon.play({})}")

    print("\nFire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {fire_dragon.attack_target(goblin_warrior)}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {fire_dragon.is_playable(available_mana=3)}")

    print("\nAbstract pattern successfully demonstrated!")
