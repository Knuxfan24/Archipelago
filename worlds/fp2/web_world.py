from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld
from .options import option_groups

class FP2WebWorld(WebWorld):
    game = "Freedom Planet 2"

    theme = "grassFlowers"
    
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Freedom Planet 2 for use in Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Knuxfan24"],
    )

    tutorials = [setup_en]
    option_groups = option_groups