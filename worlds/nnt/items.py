from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Item, ItemClassification
if TYPE_CHECKING:
    from .world import NNTWorld
import math

# Create our item table, organised by:
# - Abilities
# - Areas
# - Key Items
ITEM_NAME_TO_ID = {
    "Levers": 1,
    "Possession": 2,
    "Grenades": 3,
    "Rocks": 4,
    "UXB Defusion": 5,
    "Lifts": 6,
    "Spirit Rings": 7,
    "Meat": 8,
    "Shrykull": 9,
    "Rupture Farms": 101, # can't be a starting place without other items
    "Stockyards": 102,
    "Paramonia": 103, # can't be a starting place without other items
    "Scrabania": 104, # can't be a starting place without other items
    "Zulag 1": 105,
    "Zulag 2": 106, # can't be a starting place without other items
    "Zulag 3": 107, # can't be a starting place without other items
    "Zulag 4": 108, # can't be a starting place without other items
    "Rescued Mudokon": 201,
}

# Set the item classifications.
DEFAULT_ITEM_CLASSIFICATIONS = {
    "Levers": ItemClassification.progression,
    "Possession": ItemClassification.progression,
    "Grenades": ItemClassification.progression,
    "Rocks": ItemClassification.progression,
    "UXB Defusion": ItemClassification.progression,
    "Lifts": ItemClassification.progression,
    "Spirit Rings": ItemClassification.progression,
    "Meat": ItemClassification.progression,
    "Shrykull": ItemClassification.progression,
    "Rupture Farms": ItemClassification.progression,
    "Stockyards": ItemClassification.progression,
    "Paramonia": ItemClassification.progression,
    "Scrabania": ItemClassification.progression,
    "Zulag 1": ItemClassification.progression,
    "Zulag 2": ItemClassification.progression,
    "Zulag 3": ItemClassification.progression,
    "Zulag 4": ItemClassification.progression,
    "Rescued Mudokon": ItemClassification.progression_skip_balancing | ItemClassification.filler,
}

class NNTItem(Item):
    game = "New 'n' Tasty"

# TODO: Maybe create some junk items solely for this?
def get_random_filler_item_name(world: NNTWorld) -> str:
    return "Rescued Mudokon"

def create_item_with_correct_classification(world: NNTWorld, name: str) -> NNTItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return NNTItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: NNTWorld) -> None:
    # Create the item pool.
    itempool: list[Item] = []
    
    # Set up lists of the abilities and areas.
    abilities = ["Levers", "Possession", "Grenades", "Rocks", "UXB Defusion", "Lifts", "Spirit Rings", "Meat", "Shrykull"]
    area_access = ["Rupture Farms", "Stockyards", "Paramonia", "Scrabania", "Zulag 1", "Zulag 2", "Zulag 3", "Zulag 4"]
        
    # Select a starting area, add it to our precollected and remove it from the list.
    starting_area = world.random.choice(area_access)
    world.push_precollected(world.create_item(starting_area))
    area_access.remove(starting_area)
    
    # Determine and handled abilities that need to be given depending on the starting area.
    match starting_area:
        
        case "Rupture Farms":
            world.push_precollected(world.create_item("Levers"))
            abilities.remove("Levers")
            choice = world.random.choice(["Possession", "Grenades", "Lifts"])
            world.push_precollected(world.create_item(choice))
            abilities.remove(choice)
            
        case "Paramonia" | "Zulag 3":
            world.push_precollected(world.create_item("Possession"))
            world.push_precollected(world.create_item("Lifts"))
            world.push_precollected(world.create_item("Levers"))
            abilities.remove("Possession")
            abilities.remove("Lifts")
            abilities.remove("Levers")
            
        case "Scrabania":
            world.push_precollected(world.create_item("Possession"))
            world.push_precollected(world.create_item("UXB Defusion"))
            abilities.remove("Possession")
            abilities.remove("UXB Defusion")
            
        case "Zulag 2":
            world.push_precollected(world.create_item("Possession"))
            world.push_precollected(world.create_item("Lifts"))
            abilities.remove("Possession")
            abilities.remove("Lifts")
            
        case "Zulag 4":
            choice = world.random.choice(["Levers", "Possession"])
            world.push_precollected(world.create_item(choice))
            abilities.remove(choice)
            
    # Add the area and ability items to the item pool.
    for area_item in area_access: itempool.append(world.create_item(area_item))
    for ability_item in abilities: itempool.append(world.create_item(ability_item))
            
    # Determine how many remaining locations we have.
    needed_number_of_filler_items = len(world.multiworld.get_unfilled_locations(world.player)) - len(itempool)

    # Calculate how many Mudokons are needed based on our YAML and how much filler will be needed to fill the remaining slots.
    world.required_muds = math.ceil((world.options.muds_required * needed_number_of_filler_items) / 100.0)
    actual_filler = needed_number_of_filler_items - world.required_muds

    # Add the Mudokons to the item pool.
    itempool += [world.create_item("Rescued Mudokon") for _ in range(world.required_muds)]
    for _ in range(actual_filler):
        itempool.append(NNTItem("Rescued Mudokon", ItemClassification.filler, ITEM_NAME_TO_ID["Rescued Mudokon"], world.player))

    # Add our pool to the multiworld's.
    world.multiworld.itempool += itempool
