from ex3 import FantasyCardFactory, GameEngine, AggressiveStrategy

if __name__ == "__main__":
    print("\n=== DataDeck Game Engine ===")
    game_engine = GameEngine()
    fantasy_factory = FantasyCardFactory()
    agressive_strategy = AggressiveStrategy()
    fantasy_factory.create_creature("dragon")
    fantasy_factory.create_creature("goblin")
    fantasy_factory.create_spell("fireball")
    fantasy_factory.create_artifact("mana_ring")

    game_engine.configure_engine(fantasy_factory, agressive_strategy)
    game_engine.in_hand = [
        fantasy_factory.create_creature("Fire Dragon"),
        fantasy_factory.create_creature("Fire Dragon"),
        fantasy_factory.create_creature("Fire Dragon"),
        fantasy_factory.create_creature("Fire Dragon"),
        fantasy_factory.create_creature("Fire Dragon"),
        fantasy_factory.create_creature("Goblin Warrior"),
        fantasy_factory.create_creature("Goblin Warrior"),
        fantasy_factory.create_spell("Lightning Bolt"),
        fantasy_factory.create_spell("Lightning Bolt"),
        fantasy_factory.create_spell("Lightning Bolt"),
    ]
    game_engine.battlefield = [
        fantasy_factory.create_creature("Enemy Player"),
        fantasy_factory.create_creature("Friend Player"),
    ]

    actions = game_engine.simulate_turn()
    print(f"actions: {actions}")

    print("\nGame Report:")
    print(game_engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: "
        "Maximum flexibility achieved!"
    )
