import random
from ex0 import Card, CreatureCard
from ex1 import ArtifactCard, SpellCard


class Deck:
    def __init__(self):
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if self.cards:
            return self.cards.pop(0)
        else:
            raise IndexError("Deck is empty")

    def get_deck_stats(self) -> dict:
        return {
            'total_cards': len(self.cards),
            'creatures': sum(
                1 for card in self.cards if isinstance(card, CreatureCard)
            ),
            'spells': sum(
                1 for card in self.cards if isinstance(card, SpellCard)
            ),
            'artifacts': sum(
                1 for card in self.cards if isinstance(card, ArtifactCard)
            ),
            'avg_cost': sum(
                card.cost for card in self.cards
            ) / len(self.cards) if self.cards else 0
        }
