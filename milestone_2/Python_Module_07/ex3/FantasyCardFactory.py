import random
from typing import List, Dict, Any
from ex0 import CreatureCard, Card
from ex1 import ArtifactCard, SpellCard
from ex3 import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creature_list: List[CreatureCard] = []
        self.spell_list: List[SpellCard] = []
        self.artifact_list: List[ArtifactCard] = []

    def create_creature(self, name_or_power: Any) -> Card:
        self.creature_list.append(CreatureCard(name_or_power, 5, "rar", 8, 1))
        return self.creature_list[-1]

    def create_spell(self, name_or_power: Any) -> Card:
        self.spell_list.append(
            SpellCard(
                name_or_power,
                5,
                "rar",
                "Deal 3 damage to target",
            )
        )
        return self.spell_list[-1]

    def create_artifact(self, name_or_power: Any) -> Card:
        self.artifact_list.append(
            ArtifactCard(
                name_or_power,
                5,
                "rar",
                5,
                "Permanent: +1 mana per turn",
            )
        )
        return self.artifact_list[-1]

    def create_themed_deck(self, size: int) -> Dict[str, Any]:
        deck: List[Card] = []
        for i in range(size):
            card_type = random.choice(
                ["creature", "spell", "artifact"],
            )
            if card_type == "creature":
                deck.append(self.create_creature())
            elif card_type == "spell":
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())

        return {
            "theme": "Fantasy",
            "size": size,
            "cards": deck,
        }

    def get_supported_types(self) -> Dict[str, Any]:
        return {
            "creatures": [c.name for c in self.creature_list],
            "spells": [s.name for s in self.spell_list],
            "artifacts": [a.name for a in self.artifact_list],
        }
