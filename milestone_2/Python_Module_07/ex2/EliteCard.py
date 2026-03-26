from ex0 import Card
from ex2 import Magical, Combatable


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str):
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
        }

    def cast_spell(self, spell_name: str, targets: list[Card]) -> dict:
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': [target.name for target in targets],
            'mana_used': 4
        }

    def channel_mana(self, amount: int) -> dict:
        return {'channeled': amount, 'total_mana': amount + 4}

    def get_magic_stats(self) -> dict:
        return {
            'card_name': self.name,
            'magic_stats': "Unknown"
        }

    def attack(self, target: Card) -> dict:
        return {
            'attacker': self.name,
            'target': target.name,
            'damage': 5,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked_damage = 3
        taken = incoming_damage - blocked_damage
        return {
            'defender': self.name,
            'damage_taken': taken,
            'damage_blocked': blocked_damage,
            'still_alive': taken > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            'card_name': self.name,
            'combat_stats': "Unknown"
        }
