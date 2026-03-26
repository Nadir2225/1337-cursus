from ex0 import Card
from ex2 import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
            self,
            card_id: str,
            name: str,
            cost: int,
            rarity: str,
            rating: int = 0,
            record: dict = None,
    ):
        super().__init__(name, cost, rarity)
        self.card_id = card_id
        self.rating = rating
        self.record = record if record is not None else {
            "wins": 0, "losses": 0
        }

    def play(self, game_state: dict) -> dict:
        return game_state

    def attack(self, target) -> dict:
        result = {
            "damage_dealt": 16,
            "target": target,
        }
        return result

    def defend(self, incoming_damage: int) -> dict:
        return {
            "damage_blocked": 8,
            "remaining_damage": incoming_damage,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack_power": 16,
            "defense_power": 8,
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.record["wins"] += wins

    def update_losses(self, losses: int) -> None:
        self.record["losses"] += losses

    def get_rank_info(self) -> dict:
        return (
            f"{self.name} - Rating: {self.rating} "
            f"({self.record['wins']}-{self.record['losses']})"
        )
