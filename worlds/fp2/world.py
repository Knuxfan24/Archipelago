from collections.abc import Mapping
from typing import Any
from worlds.AutoWorld import World
from . import items, locations, options, regions, rules, web_world

class FP2World(World):
    """
    Freedom Planet 2 is a fast paced action platformer.
    """

    game = "Freedom Planet 2"

    web = web_world.FP2WebWorld()

    options_dataclass = options.FP2Options
    options: options.FP2Options

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID
    
    item_name_groups = {
        "Potions": set(["Potion - Extra Stock", "Potion - Strong Revivals", "Potion - Cheaper Stocks", "Potion - Healing Strike", "Potion - Attack Up", "Potion - Strong Shields", "Potion - Accelerator", "Potion - Super Feather", "Potion - Hover", "Potion - Energy", "Potion - Resonance"]),
        "Brave Stones": set(["Element Burst", "Max Life Up", "Crystals to Petals", "Powerup Start", "Shadow Guard", "Payback Ring", "Wood Charm", "Earth Charm", "Water Charm", "Fire Charm", "Metal Charm", "Petal Armor", "Rainbow Charm", "Angel Tear", "Turtle Godshell", "Tinker Glove", "Pheonix Tonic", "Warpstone", "Madstone", "Guardian Charm", "Explosive Finale", "Idol of Greed", "Bomb Magnet", "Ninja Garb", "Ice Crown", "Invisibility Cloak", "Gravity Boots", "Magic Compass"]),
        "Chapter Unlocks": set(["Progressive Chapter", "Mystery of the Frozen North", "Sky Pirate Panic", "Enter the Battlesphere", "Globe Opera", "Justice in the Sky Paradise", "Robot Wars! Snake VS Tarsier", "Echoes of the Dragon War", "Bakunawa", "Dragon Valley", "Shenlin Park", "Tiger Falls", "Robot Graveyard", "Shade Armory", "Snowfields", "Avian Museum", "Airship Sigwada", "Phoenix Highway", "Zao Land", "The Battlesphere", "Globe Opera 1", "Globe Opera 2", "Auditorium", "Palace Courtyard", "Tidal Gate", "Sky Bridge", "Lightning Tower", "Zulon Jungle", "Nalao Lake", "Ancestral Forge", "Magma Starscape", "Diamond Point", "Gravity Bubble", "Bakunawa Chase", "Bakunawa Rush", "Refinery Room", "Clockwork Arboretum", "Inversion Dynamo", "Lunar Cannon", "Merga"]),
        "Chest Tracers": set(["Chest Tracer - Dragon Valley", "Chest Tracer - Shenlin Park", "Chest Tracer - Tiger Falls", "Chest Tracer - Robot Graveyard", "Chest Tracer - Shade Armory", "Chest Tracer - Avian Museum", "Chest Tracer - Airship Sigwada", "Chest Tracer - Phoenix Highway", "Chest Tracer - Zao Land", "Chest Tracer - Globe Opera 1", "Chest Tracer - Globe Opera 2", "Chest Tracer - Palace Courtyard", "Chest Tracer - Tidal Gate", "Chest Tracer - Sky Bridge", "Chest Tracer - Lightning Tower", "Chest Tracer - Zulon Jungle", "Chest Tracer - Nalao Lake", "Chest Tracer - Ancestral Forge", "Chest Tracer - Magma Starscape", "Chest Tracer - Gravity Bubble", "Chest Tracer - Bakunawa Rush", "Chest Tracer - Clockwork Arboretum", "Chest Tracer - Inversion Dynamo", "Chest Tracer - Lunar Cannon", "Chest Tracer"]),
        "Traps": set(["Swap Trap", "Mirror Trap", "Pie Trap", "Spring Trap", "PowerPoint Trap", "Zoom Trap", "Aaa Trap", "Spike Ball Trap", "Pixellation Trap", "Rail Trap", "Spam Trap", "Syntax Jumpscare Trap", "Trivia Trap", "Mach Speed Trap", "Scott The Woz Trap", "No Stocks", "Expensive Stocks", "Double Damage", "No Revivals", "No Guarding", "No Petals", "Time Limit", "Items To Bombs", "Life Oscillation", "One Hit KO"]),
        
        "Chaos Emeralds": set(["Red Chaos Emerald", "Blue Chaos Emerald", "Yellow Chaos Emerald", "Green Chaos Emerald", "White Chaos Emerald", "Cyan Chaos Emerald", "Purple Chaos Emerald"])
    }

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)
        
    def create_item(self, name: str) -> items.FP2Item:
        if name == items.FP2UTGlitchFlag.FLAG_NAME:
            return items.FP2UTGlitchFlag(self.player)
        
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "death_link", "ring_link", "trap_link", "damage_link", "chest_tracer_items", "chapters", "trap_stones", "fast_weapons_core", "dangerous_time_limit", "chest_tracers", "chests", "chest_tracer_strict", "enemies", "bosses", "milla_shop", "milla_shop_price", "milla_shop_amount", "vinyl_shop", "vinyl_shop_price", "vinyl_shop_amount", "item_boxes"
        )
    
    # Add the flags for Universal Tracker.
    ut_can_gen_without_yaml = False
    glitches_item_name: str = items.FP2UTGlitchFlag.FLAG_NAME