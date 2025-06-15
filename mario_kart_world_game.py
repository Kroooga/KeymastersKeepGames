from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class MarioKartWorldArchipelagoOptions:
    pass

class MarioKartWorldGame(Game):

    name = "Mario Kart World"
    platform = KeymastersKeepGamePlatforms.SW

    platforms_other = [
        #KeymastersKeepGamePlatforms.SW2,
    ]

    is_adult_only_or_unrated = False

    options_cls = MarioKartWorldArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Complete the CUPS Cup on CC",
                data={
                    "CUPS": (self.cups, 1),
                    "CC": (self.ccs, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Complete the RALLIES Rally on CC",
                data={
                    "RALLIES": (self.rallies, 1),
                    "CC": (self.ccs, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Complete NUM P-Switch Challenges in or around COURSE",
                data={
                    "NUM": (self.switch_range, 1),
                    "COURSE": (self.courses, 1), 
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Activate NUM ? Mark Panels in COURSE",
                data={
                    "NUM": (self.panel_range, 1),
                    "COURSE": (self.courses, 1), 
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Collect a Peach Medallion in or around COURSE",
                data={
                    "COURSE": (self.courses, 1), 
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
        ]

    @staticmethod
    def courses() -> List[str]:
        return [
            "Mario Bros. Circuit",
            "Crown City",
            "Whistlestop Summit",
            "DK Spaceport",
            "Desert Hills",
            "Shy Guy Bazaar",
            "Wario Stadium",
            "Airship Fortress",
            "DK Pass",
            "Starview Peak",
            "Sky-High Sundae",
            "Wario Shipyard",
            "Koopa Troopa Beach",
            "Faraway Oasis",
            "Peach Stadium",
            "Peach Beach",
            "Salty Salty Speedway",
            "Dino Dino Jungle",
            "Great ? Block Ruins",
            "Cheep Cheep Falls",
            "Dandelion Depths",
            "Boo Cinema",
            "Dry Bones Burnout",
            "Moo Moo Meadows",
            "Choco Mountain",
            "Toad's Factory",
            "Bowser's Castle",
            "Acorn Heights",
            "Mario Circuit"
        ]

    @staticmethod
    def cups() -> List[str]:
        return [
            "Mushroom",
            "Flower",
            "Star",
            "Shell",
            "Banana",
            "Leaf",
            "Lightning",
            "Special"
        ]

    @staticmethod
    def rallies() -> List[str]:
        return [
            "Golden",
            "Ice",
            "Moon",
            "Spiny",
            "Cherry",
            "Acorn",
            "Cloud",
            "Heart"
        ]

    @staticmethod
    def ccs() -> List[str]:
        return [
            "50cc",
            "100cc",
            "150cc"
        ]
    
    @staticmethod
    def switch_range() -> range:
            return range(2, 6)
    
    @staticmethod
    def panel_range() -> range:
            return range(1, 4)
    

# Archipelago Options
# ...