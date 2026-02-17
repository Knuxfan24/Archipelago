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
    "Rupture Farms": 101,
    "Stockyards": 102,
    "Paramonia": 103,
    "Scrabania": 104,
    "Zulag 1": 105,
    "Zulag 2": 106,
    "Zulag 3": 107,
    "Zulag 4": 108,
    "Monsaic Lines": 109, # Only used if Extra Area Clear Checks are on. 
    "Rescued Mudokon": 201,
    "Shock Trap": 301,
    "Trip Trap": 302,
    "lol brawl reference": 303,
    "QuikSave Trap": 304,
    "Drop Trap": 305
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
    "Monsaic Lines": ItemClassification.progression,
    "Rescued Mudokon": ItemClassification.progression_skip_balancing | ItemClassification.filler,
    "Shock Trap": ItemClassification.trap,
    "Trip Trap": ItemClassification.trap,
    "lol brawl reference": ItemClassification.trap,
    "QuikSave Trap": ItemClassification.trap,
    "Drop Trap": ItemClassification.trap
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
            
    # If we're using the Extra Area Clears option, then add the item for the Monsaic Lines too.
    if (world.options.extra_area_clears == 1 and world.options.area_clears == 1): itempool.append(world.create_item("Monsaic Lines"))
            
    # Determine how many remaining locations we have.
    needed_number_of_filler_items = len(world.multiworld.get_unfilled_locations(world.player)) - len(itempool)

    # Calculate how many Mudokons are needed based on our YAML and how much filler will be needed to fill the remaining slots.
    world.required_muds = math.ceil((world.options.muds_required * needed_number_of_filler_items) / 100.0)
    actual_filler = needed_number_of_filler_items - world.required_muds

    # Add the required Mudokons to the item pool.
    itempool += [world.create_item("Rescued Mudokon") for _ in range(world.required_muds)]
    
    # Add filler to the remaning slots, either as more Mudokons or traps.
    trap_items = ["Shock Trap", "Trip Trap", "Drop Trap"] # TODO: Add the QuikSave Trap if I decide to actually include it.
    for _ in range(actual_filler):
        if world.random.randint(0, 99) < world.options.filler_traps:
            trapItem = world.random.choice(trap_items)
            
            # Roll a 1 in 10000 chance to swap this trap out for the "lol brawl reference one"
            if (world.random.randint(0, 9999) == 0):
                trapItem = "lol brawl reference"
                input("Hit the chance for the brawl joke.") # thing to tell me that we've hit that chance, remove this when an actual ap build happens.
            
            itempool.append(world.create_item(trapItem))
        else:
            itempool.append(NNTItem("Rescued Mudokon", ItemClassification.filler, ITEM_NAME_TO_ID["Rescued Mudokon"], world.player))

    # Add our pool to the multiworld's.
    world.multiworld.itempool += itempool
