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
            "death_link", "ring_link", "trap_link", "damage_link", "chest_tracer_items", "chapters", "shop_information", "trap_stones", "fast_weapons_core", "dangerous_time_limit", "chest_tracers", "chests", "chest_tracer_strict", "enemies", "bosses", "milla_shop", "milla_shop_price", "milla_shop_amount", "vinyl_shop", "vinyl_shop_price", "vinyl_shop_amount", "item_boxes"
        )
    
    # Add the flags for Universal Tracker.
    ut_can_gen_without_yaml = False
    glitches_item_name: str = items.FP2UTGlitchFlag.FLAG_NAME