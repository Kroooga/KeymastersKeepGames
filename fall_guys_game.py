from __future__ import annotations


from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class FallGuysArchipelagoOptions:
    pass

class FallGuysGame(Game):

    name = "Fall Guys"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.AND,
        KeymastersKeepGamePlatforms.IOS,
    ]

    is_adult_only_or_unrated = False

    options_cls = FallGuysArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Qualify from COUNT rounds in MODE",
                data={
                    "COUNT": (self.round_range, 1),
                    "MODE": (self.modes, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=7,
            ),
            GameObjectiveTemplate(
                label="Qualify from COUNT ROUND rounds",
                data={
                    "COUNT": (self.round_range, 1),
                    "ROUND": (self.round_types, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Win a game of MODE",
                data={
                    "MODE": (self.modes, 1), 
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Place 1st in a Race or Team round",
                data={
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Play COUNT rounds of a limited time mode",
                data={
                    "COUNT": (self.round_range, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a game of a limited time mode",
                data={
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
        ]

    @staticmethod
    def modes() -> List[str]:
        return [
            "Solos",
            "Duos",
            "Squads",
            "Knockout",
            "Creator Spotlight",
            "Explore",
        ]

    @staticmethod
    def round_types() -> List[str]:
        return [
            "Race",
            "Survival",
            "Hunt",
            "Logic",
            "Team",
        ]
    
    @staticmethod
    def round_range() -> range:
            return range(3, 8)

# Archipelago Options
# ...