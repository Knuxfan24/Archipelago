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
            "death_link", "ring_link", "trap_link", "chest_tracer_items", "chapters", "shop_information", "trap_stones", "fast_weapons_core", "dangerous_time_limit", "chest_tracers", "chests", "chest_tracer_strict", "enemies", "bosses", "milla_shop", "milla_shop_price", "milla_shop_amount", "vinyl_shop", "vinyl_shop_price", "vinyl_shop_amount", "item_boxes"
        )
    
    # TODO: Maybe make look up tables of some sort for the maps that are just left to right rather than just jamming a load of if statements together?
    # TODO: Reinstate this function once we get all the maps and don't have them taking up hundreds of megabytes of space.
    #def map_page_index(data: Any) -> int:        
    #    if (isinstance(data, dict)):
    #        match data["Scene"]:
                #case "DragonValley":
                #    if (data["PositionX"] < 5360): return 1
                #    if (data["PositionX"] < 11752): return 2
                #    if (data["PositionX"] < 18224): return 3
                #    if (data["PositionX"] < 24656): return 4
                #    if (data["PositionX"] < 31104): return 5
                #    if (data["PositionX"] < 37536): return 6
                #    if (data["PositionX"] < 44048): return 7
                #    if (data["PositionX"] < 50392): return 8
                #    if (data["PositionX"] < 56872): return 9
                #    return 10
                #
                #case "ShenlinPark":
                #    if (data["PositionX"] < 4464): return 11
                #    if (data["PositionX"] < 10144): return 12
                #    if (data["PositionX"] < 15776): return 13
                #    if (data["PositionX"] < 21448): return 14
                #    if (data["PositionX"] < 27104): return 15
                #    if (data["PositionX"] < 32752): return 16
                #    if (data["PositionX"] < 38400): return 17
                #    if (data["PositionX"] < 44096): return 18
                #    if (data["PositionX"] < 49728): return 19
                #    if (data["PositionX"] < 55392): return 20
                #    if (data["PositionX"] < 61056): return 21
                #    return 22
                #
                #case "TigerFalls":
                #    if (data["PositionX"] < 10912): return 23
                #    if (data["PositionX"] < 23736): return 24
                #    return 25
                #
                #case "RobotGraveyard":
                #    if (data["PositionX"] < 12384): return 26
                #    if (data["PositionX"] < 28664): return 27
                #    return 28
                #
                #case "ShadeArmory":
                #    if (data["PositionX"] < 13168): return 29
                #    return 30
                #
                #case "AvianMuseum":
                #    if (data["PositionX"] < 7072): return 31
                #    if (data["PositionX"] < 16288): return 32
                #    if (data["PositionX"] < 25536): return 33
                #    if (data["PositionX"] < 34680): return 34
                #    return 35
                #
                #case "AirshipSigwada":
                #    if (data["PositionX"] < 15120): return 36
                #    if (data["PositionX"] < 32008): return 37
                #    if (data["PositionX"] < 39792): return 38
                #    if (data["PositionX"] < 48352): return 39
                #    if (data["PositionX"] < 60048): return 40
                #    return 41
                    
                #case _:
                #    print("Scene " + data["Scene"] + " is currently unhandled!")
                    
        #return 0

    # TODO: Reinstate the other maps and locations once we get all the maps and don't have them taking up hundreds of megabytes of space.
    tracker_world = {"map_page_folder": "tracker",
                     "map_page_maps": [
                        "maps/misc.json"#,
                        #"maps/dValley.json",
                        #"maps/sPark.json",
                        #"maps/tFalls.json",
                        #"maps/rGraveyard.json",
                        #"maps/sArmory.json",
                        #"maps/aMuseum.json",
                        #"maps/aSigwada.json",
                        #"maps/pHighway.json"
                        ],
                     "map_page_locations": [
                         "locations/map.json",
                         "locations/battlesphereMenu.json"
                         #"locations/dValley.json",
                         #"locations/sPark.json",
                         #"locations/tFalls.json",
                         #"locations/rGraveyard.json",
                         #"locations/sArmory.json",
                         #"locations/aMuseum.json",
                         #"locations/aSigwada.json",
                         #"locations/pHighway.json",
                         #"locations/enemies.json",
                         #"locations/bosses.json"
                         ],
                     "map_page_setting_key": "FP2_PlayerSlot{player}"#,
                     #"map_page_index": map_page_index,
                     }
    ut_can_gen_without_yaml = False
    glitches_item_name: str = items.FP2UTGlitchFlag.FLAG_NAME