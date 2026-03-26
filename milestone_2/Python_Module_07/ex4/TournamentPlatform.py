import random
from typing import Dict
from ex4 import TournamentCard


class TournamentPlatform:
    def __init__(self):
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        try:
            game_points = 16
            cards = [card1_id, card2_id]

            winner = random.choice(cards)
            self.cards[winner].update_wins(1)
            self.cards[winner].rating += game_points

            loser = cards[1] if winner == cards[0] else cards[0]
            self.cards[loser].update_losses(1)
            self.cards[loser].rating -= game_points
            self.matches_played += 1
            return {
                "winner": winner,
                "loser": loser,
                "winner_rating": self.cards[winner].rating,
                "loser_rating": self.cards[loser].rating
            }
        except KeyError:
            return {"error": "One or both card IDs not found."}

    def get_rating(self, card: TournamentCard) -> int:
        return self.cards[card.card_id].calculate_rating()

    def get_leaderboard(self) -> list:
        leaderboard = [card for card in self.cards.values()]
        leaderboard.sort(key=self.get_rating, reverse=True)
        return leaderboard

    def generate_tournament_report(self) -> dict:
        avg = 0
        for card in self.cards.values():
            avg += card.calculate_rating()
        avg_rating = avg / len(self.cards) if self.cards else 0

        return {
            'total_cards': len(self.cards),
            'matches_played': self.matches_played,
            'avg_rating': int(avg_rating),
            'platform_status': 'active'
        }
