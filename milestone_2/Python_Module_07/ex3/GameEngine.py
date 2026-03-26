from typing import Any, Dict, Optional, List
from ex3 import CardFactory, GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: Optional[CardFactory] = None
        self.strategy: Optional[GameStrategy] = None
        self.in_hand: List[Any] = []
        self.battlefield: List[Any] = []
        self.total_damage: int = 0
        self.turns: int = 0
        self.cards_created: int = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        print("\nConfiguring Fantasy Card Game...")
        self.factory = factory
        self.strategy = strategy
        print(f"Factory: {type(self.factory).__name__}")
        print(f"Strategy: {self.strategy.get_strategy_name()}")
        print(f"Available types: {self.factory.get_supported_types()}")

    def simulate_turn(self) -> Dict[str, Any]:
        try:
            print("\nSimulating aggressive turn...")
            print(f"Hand: {[card.name for card in self.in_hand]}")
            self.turns += 1
            result = self.strategy.execute_turn(
                self.in_hand,
                self.battlefield,
            )
            self.total_damage += result["damage_dealt"]
            return result
        except IndexError:
            print("No cards in hand to play!")
            return {
                'cards_played': [],
                'mana_used': 0,
                'targets_attacked': [],
                'damage_dealt': 0,
            }

    def get_engine_status(self) -> Dict[str, Any]:
        return {
            "turns_simulated": self.turns,
            "strategy_used": self.strategy.get_strategy_name(),
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
