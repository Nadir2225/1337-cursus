import random
from ex0 import CreatureCard, Card
from ex3 import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        print("\nTurn execution:")
        print(f"Strategy: {self.get_strategy_name()}")
        cards_played = []
        mana_used = 0
        damage_dealt = 0
        targets_attacked = self.prioritize_targets(battlefield)

        for _ in range(2):
            card: Card = random.choice(hand)
            hand.remove(card)
            cards_played.append(card.name)
            mana_used += card.cost
            if isinstance(card, CreatureCard):
                damage_dealt += card.attack

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list[Card]) -> list:
        filtred = []

        targets = [target.name for target in available_targets]
        for target in targets:
            if "enemy" in target.lower():
                filtred.append(target)
        return filtred
