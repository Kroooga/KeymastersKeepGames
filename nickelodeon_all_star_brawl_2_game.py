from __future__ import annotations

import functools

from typing import List, Set

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class NickelodeonAllStarBrawl2ArchipelagoOptions:
    nickelodeon_all_star_brawl_2_dlc_owned : NickelodeonAllStarBrawl2DLCOwned

class NickelodeonAllStarBrawl2Game(Game):

    name = "Nickelodeon All-Star Brawl 2"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = NickelodeonAllStarBrawl2ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return list()

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Complete MODE mode with CHARACTER on DIFFICULTY difficulty",
                data={
                    "MODE": (self.modes, 1),
                    "CHARACTER": (self.characters, 1),
                    "DIFFICULTY": (self.difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Complete MINIGAME with CHARACTERS",
                data={
                    "MINIGAME": (self.minigames, 1),
                    "CHARACTERS": (self.characters, 3),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Complete a Campaign Run with CHARACTER on DIFFICULTY difficulty",
                data={
                    "CHARACTER": (self.characters, 1),
                    "DIFFICULTY": (self.campaign_difficulties, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a 1v1 Match as CHARACTER on STAGE against a Level LEVEL OPPONENT computer",
                data={
                    "CHARACTER": (self.characters, 1),
                    "STAGE": (self.stages, 1),
                    "LEVEL": (self.cpu_range, 1),
                    "OPPONENT": (self.characters, 1),
                    
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
        ]

    @property
    def dlc_owned(self) -> Set[str]:
        return self.archipelago_options.nickelodeon_all_star_brawl_2_dlc_owned.value

    @property
    def has_dlc_character_mr_krabs(self) -> bool:
        return "Mr. Krabs" in self.dlc_owned

    @property
    def has_dlc_character_zuko(self) -> bool:
        return "Zuko" in self.dlc_owned

    @property
    def has_dlc_character_rocksteady(self) -> bool:
        return "Rocksteady" in self.dlc_owned

    @property
    def has_dlc_character_iroh(self) -> bool:
        return "Iroh" in self.dlc_owned

    @functools.cached_property
    def characters_base(self) -> List[str]:
        return [
            "Spongebob",
            "Patrick",
            "Squidward",
            "Plankton",
            "Donatello",
            "Raphael",
            "April O' Niel",
            "Aang",
            "Azula",
            "Korra",
            "Danny Phantom",
            "Ember McLain",
            "Gerald",
            "Grandma Gertie",
            "Ren & Stimpy",
            "Garfield",
            "Jimmy Neutron",
            "Zim",
            "Jenny Wakeman",
            "Rocko",
            "Lucy Loud",
            "Reptar",
            "Angry Beavers",
            "Nigel Thornberry",
            "El Tigre",
        ]
     
    def characters(self) -> List[str]:
        characters: List[str] = self.characters_base[:]

        if self.has_dlc_character_mr_krabs:
            characters.append("Mr. Krabs")

        if self.has_dlc_character_zuko:
            characters.append("Zuko")

        if self.has_dlc_character_rocksteady:
            characters.append("Rocksteady")

        if self.has_dlc_character_iroh:
            characters.append("Iroh")

        return characters

    @staticmethod
    def stages() -> List[str]:
        return [
            "Jellyfish Fields",
            "Flying Dutchman's Ship",
            "Bun Wrestling Ring",
            "The Chum Bucket",
            "Conch Street",
            "Sewers Slam",
            "Rooftop Rumble",
            "Technodrome Takedown",
            "Western Air Temple",
            "Fire Masters Meeting",
            "Harmonic Convergence",
            "Pariah's Keep",
            "Clockwork's Lair",
            "City Aquarium",
            "Messy Kitchen",
            "Food Dream",
            "Jimmy's Lab",
            "Irken Armada Invasion",
            "Tremorton Joyride",
            "Hardcore Chores",
            "Castle Loud",
            "Royal Woods Cemetery",
            "Reptar's Ruins",
            "Angry Beavers' Dam",
            "Wild Savannah",
            "Miracle City Volcano",
            "The Timeless Stardial",
        ]

    @staticmethod
    def modes() -> List[str]:
        return [
            "Arcade",
            "Boss Rush",
            "Gauntlet Run",
        ]

    @staticmethod
    def minigames() -> List[str]:
        return [
            "Pop The Slime Baloons",
            "Whack-A-Bot",
        ]

    @staticmethod
    def difficulties() -> List[str]:
        return [
            "Tiny but Mighty",
            "Texas Tough",
            "Master Class",
            "Unstoppable Force",
        ]
    
    @staticmethod
    def campaign_difficulties() -> List[str]:
        return [
            "Tiny but Mighty",
            "Texas Tough",
            "Master Class",
            "How Tough Are Ya?",
            "Madness Reigns",
            "Prepare For Doom",
        ]

    @staticmethod
    def cpu_range() -> range:
            return range(1, 10)

# Archipelago Options
class NickelodeonAllStarBrawl2DLCOwned(OptionSet):
    """
    Indicates which Nickelodeon All-Star Brawl 2 DLC the player owns, if any.
    """

    display_name = "Nickelodeon All-Star Brawl 2 DLC Owned"
    valid_keys = [
        "Mr. Krabs",
        "Zuko",
        "Rocksteady",
        "Iroh",
    ]

    default = valid_keys