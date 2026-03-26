from ex0 import Card


class ArtifactCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str,
        durability: int, effect: str
    ):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Permanent: +1 mana per turn'
        }

    def activate_ability(self) -> dict:
        return {
            'ability_activated': self.effect,
        }
