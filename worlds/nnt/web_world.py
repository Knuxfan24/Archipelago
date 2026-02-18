from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

class NNTWebWorld(WebWorld):
    game = "New 'n' Tasty"

    theme = "stone"
    
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Oddworld: New 'n' Tasty for use in Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Knuxfan24"],
    )

    tutorials = [setup_en]