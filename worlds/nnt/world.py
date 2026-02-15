from collections.abc import Mapping
from typing import Any
from worlds.AutoWorld import World
from . import items, locations, regions, rules
from . import options as nnt_options

class NNTWorld(World):
    """
    APQuest is a minimal 8bit-era inspired adventure game with grid-like movement.
    Good games don't need more than six checks.
    """
    
    game = "New 'n' Tasty"

    options_dataclass = nnt_options.NNTOptions
    options: nnt_options.NNTOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID
    
    required_muds = 999

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.NNTItem:
        return items.create_item_with_correct_classification(self, name)
    
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        slot_data = self.options.as_dict(
            "goal",
            "area_clears",
            "extra_area_clears",
            "death_link",
            "death_link_amnesty",
            "ring_link"
        )
        
        slot_data.update({"required_muds": self.required_muds})
        
        return slot_data