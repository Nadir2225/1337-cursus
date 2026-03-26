from ex4 import TournamentCard, TournamentPlatform


if __name__ == "__main__":
    print("\n=== DataDeck Tournament Platform ===")
    platform = TournamentPlatform()
    fire_dragon = TournamentCard(
        "dragon_001", "Fire Dragon", 5, "rare", rating=1200
    )
    ice_wizard = TournamentCard(
        "wizard_001", "Ice Wizard", 3, "uncommon", rating=1150
    )

    print("\nRegistering Tournament Cards...")
    platform.register_card(ice_wizard)
    platform.register_card(fire_dragon)
    for card_id in platform.cards.keys():
        card = platform.cards[card_id]
        interfaces = [cls.__name__ for cls in card.__class__.__bases__]
        print(f"\n{card.name} ({card_id}):")
        print(f"- Interfaces: [{', '.join(interfaces)}]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.record['wins']}-{card.record['losses']}")

    print("\nCreating tournament match...")
    print("Match Result:", platform.create_match("dragon_001", "wizard_001"))

    print("\nTournament Leaderboard:")
    i = 1
    for card in platform.get_leaderboard():
        print(f"{i}- {card.get_rank_info()}")
        i += 1

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")
