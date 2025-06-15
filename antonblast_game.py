from __future__ import annotations


from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class AntonblastArchipelagoOptions:
    pass

class AntonblastGame(Game):

    name = "Antonblast"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.SW,
    ]

    is_adult_only_or_unrated = False

    options_cls = AntonblastArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Complete LEVEL in MODE mode",
                data={
                    "LEVEL": (self.levels, 1),
                    "MODE": (self.modes, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=9,
            ),
            GameObjectiveTemplate(
                label="Defeat BOSS",
                data={
                    "BOSS": (self.bosses, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Collect the ITEM in LEVEL",
                data={
                    "ITEM": (self.items, 1),
                    "LEVEL": (self.levels, 1), 
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=7,
            ),
            GameObjectiveTemplate(
                label="Achieve Par Time on LEVEL in Time Trial",
                data={
                    "LEVEL": (self.levels, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Achieve CRACKED ranking on LEVEL in Combo Chain",
                data={
                    "LEVEL": (self.levels, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Achieve CRACKED ranking on BOSS",
                data={
                    "BOSS": (self.bosses, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
        ]

    @staticmethod
    def levels() -> List[str]:
        return [
            "Boiler City",
            "Slowroast Sewer",
            "Cinnamon Springs",
            "Bomb Candy Mines",
            "The Big Bath",
            "Concrete Jungle",
            "Pinball Mire",
            "Mad Mall",
            "Crimson Factory",
            "The Mysterious Glasshouse",
            "Devilled Gardens",
            "Hell Manor",
        ]

    @staticmethod
    def modes() -> List[str]:
        return [
            "Arcade",
            "Time Trial",
            "Chain Combo",
        ]

    @staticmethod
    def items() -> List[str]:
        return [
            "Spirit",
            "Cassette Tape",
            "Spray Can",
            "Memento",
            "Paul",
        ]

    @staticmethod
    def bosses() -> List[str]:
        return [
            "Brawlbuster",
            "Jewel Ghoul",
            "Tallbuster",
            "Freako Dragon",
            "Smallbuster",
            "Maulbuster",
            "Ring-a-Ding",
            "Satan",
        ]

# Archipelago Options
# ...