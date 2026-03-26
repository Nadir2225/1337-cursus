from ex0 import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Deal 3 damage to target'
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            'spell': self.name,
            'targets': [target.name for target in targets],
            'effect_resolved': True
        }
