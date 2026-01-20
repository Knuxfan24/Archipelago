from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Item, ItemClassification
if TYPE_CHECKING:
    from .world import FP2World

# Create our item table, organised by:
# - Key Items
# - Extra Slots
# - Potions
# - Brave Stones
# - Chapter/Stage Unlocks
# - Chest Tracers
# - Traps
# - Filler
ITEM_NAME_TO_ID = {
    "Star Card": 1,
    "Time Capsule": 2,
    "Battlesphere Key": 3,
    
    "Extra Item Slot": 101,
    "Extra Potion Slot": 102,
    
    "Potion - Extra Stock": 201,
    "Potion - Strong Revivals": 202,
    "Potion - Cheaper Stocks": 203,
    "Potion - Healing Strike": 204,
    "Potion - Attack Up": 205,
    "Potion - Strong Shields": 206,
    "Potion - Accelerator": 207,
    "Potion - Super Feather": 208,
    
    "Element Burst": 301,
    "Max Life Up": 302,
    "Crystals to Petals": 303,
    "Powerup Start": 304,
    "Shadow Guard": 305,
    "Payback Ring": 306,
    "Wood Charm": 307,
    "Earth Charm": 308,
    "Water Charm": 309,
    "Fire Charm": 310,
    "Metal Charm": 311,
    "No Stocks": 312,
    "Expensive Stocks": 313,
    "Double Damage": 314,
    "No Revivals": 315,
    "No Guarding": 316,
    "No Petals": 317,
    "Time Limit": 318,
    "Items To Bombs": 319,
    "Life Oscillation": 320,
    "One Hit KO": 321,
    "Petal Armor": 322,
    "Rainbow Charm": 323,
    
    "Progressive Chapter": 401,
    "Mystery of the Frozen North": 402,
    "Sky Pirate Panic": 403,
    "Enter the Battlesphere": 404,
    "Globe Opera": 405,
    "Justice in the Sky Paradise": 406,
    "Robot Wars! Snake VS Tarsier": 407,
    "Echoes of the Dragon War": 408,
    "Bakunawa": 409,
    "Dragon Valley": 410,
    "Shenlin Park": 411,
    "Tiger Falls": 412,
    "Robot Graveyard": 413,
    "Shade Armory": 414,
    "Snowfields": 415,
    "Avian Museum": 416,
    "Airship Sigwada": 417,
    "Phoenix Highway": 418,
    "Zao Land": 419,
    "The Battlesphere": 420,
    "Globe Opera 1": 421,
    "Globe Opera 2": 422,
    "Auditorium": 423,
    "Palace Courtyard": 424,
    "Tidal Gate": 425,
    "Sky Bridge": 426,
    "Lightning Tower": 427,
    "Zulon Jungle": 428,
    "Nalao Lake": 429,
    "Ancestral Forge": 430,
    "Magma Starscape": 431,
    "Diamond Point": 432,
    "Gravity Bubble": 433,
    "Bakunawa Chase": 434,
    "Bakunawa Rush": 435,
    "Refinery Room": 436,
    "Clockwork Arboretum": 437,
    "Inversion Dynamo": 438,
    "Lunar Cannon": 439,
    "Merga": 440,
    
    "Chest Tracer - Dragon Valley": 501,
    "Chest Tracer - Shenlin Park": 502,
    "Chest Tracer - Tiger Falls": 503,
    "Chest Tracer - Robot Graveyard": 504,
    "Chest Tracer - Shade Armory": 505,
    "Chest Tracer - Avian Museum": 506,
    "Chest Tracer - Airship Sigwada": 507,
    "Chest Tracer - Phoenix Highway": 508,
    "Chest Tracer - Zao Land": 509,
    "Chest Tracer - Globe Opera 1": 510,
    "Chest Tracer - Globe Opera 2": 511,
    "Chest Tracer - Palace Courtyard": 512,
    "Chest Tracer - Tidal Gate": 513,
    "Chest Tracer - Sky Bridge": 514,
    "Chest Tracer - Lightning Tower": 515,
    "Chest Tracer - Zulon Jungle": 516,
    "Chest Tracer - Nalao Lake": 517,
    "Chest Tracer - Ancestral Forge": 518,
    "Chest Tracer - Magma Starscape": 519,
    "Chest Tracer - Gravity Bubble": 520,
    "Chest Tracer - Bakunawa Rush": 521,
    "Chest Tracer - Clockwork Arboretum": 522,
    "Chest Tracer - Inversion Dynamo": 523,
    "Chest Tracer - Lunar Cannon": 524,
    "Chest Tracer": 525,
    
    "Swap Trap": 601,
    "Mirror Trap": 602,
    "Pie Trap": 603,
    "Spring Trap": 604,
    "PowerPoint Trap": 605,
    "Zoom Trap": 606,
    "Aaa Trap": 607,
    "Spike Ball Trap": 608,
    "Pixellation Trap": 609,
    "Rail Trap": 610,
    "Spam Trap": 611,
    "Syntax Jumpscare Trap": 612,
    
    "Crystals": 701,
    "Extra Life": 702,
    "Invincibility": 703,
    "Wood Shield": 704,
    "Earth Shield": 705,
    "Water Shield": 706,
    "Fire Shield": 707,
    "Metal Shield": 708,
    "Powerup": 709,
    "Gold Gem": 710
}

# Set the item classifications.
DEFAULT_ITEM_CLASSIFICATIONS = {
    "Star Card": ItemClassification.progression_skip_balancing | ItemClassification.filler,
    "Time Capsule": ItemClassification.progression_skip_balancing | ItemClassification.filler,
    "Battlesphere Key": ItemClassification.progression,
    
    "Extra Item Slot": ItemClassification.useful,
    "Extra Potion Slot": ItemClassification.useful,
    
    "Potion - Extra Stock": ItemClassification.useful,
    "Potion - Strong Revivals": ItemClassification.useful,
    "Potion - Cheaper Stocks": ItemClassification.useful,
    "Potion - Healing Strike": ItemClassification.useful,
    "Potion - Attack Up": ItemClassification.useful,
    "Potion - Strong Shields": ItemClassification.useful,
    "Potion - Accelerator": ItemClassification.useful,
    "Potion - Super Feather": ItemClassification.progression,
    
    "Element Burst": ItemClassification.useful,
    "Max Life Up": ItemClassification.useful,
    "Crystals to Petals": ItemClassification.useful,
    "Powerup Start": ItemClassification.useful,
    "Shadow Guard": ItemClassification.useful,
    "Payback Ring": ItemClassification.useful,
    "Wood Charm": ItemClassification.useful,
    "Earth Charm": ItemClassification.useful,
    "Water Charm": ItemClassification.useful,
    "Fire Charm": ItemClassification.useful,
    "Metal Charm": ItemClassification.useful,
    "No Stocks": ItemClassification.trap,
    "Expensive Stocks": ItemClassification.trap,
    "Double Damage": ItemClassification.trap,
    "No Revivals": ItemClassification.trap,
    "No Guarding": ItemClassification.trap,
    "No Petals": ItemClassification.trap,
    "Time Limit": ItemClassification.trap,
    "Items To Bombs": ItemClassification.trap,
    "Life Oscillation": ItemClassification.trap,
    "One Hit KO": ItemClassification.trap,
    "Petal Armor": ItemClassification.useful,
    "Rainbow Charm": ItemClassification.useful,
    
    "Progressive Chapter": ItemClassification.progression,
    "Mystery of the Frozen North": ItemClassification.progression,
    "Sky Pirate Panic": ItemClassification.progression,
    "Enter the Battlesphere": ItemClassification.progression,
    "Globe Opera": ItemClassification.progression,
    "Justice in the Sky Paradise": ItemClassification.progression,
    "Robot Wars! Snake VS Tarsier": ItemClassification.progression,
    "Echoes of the Dragon War": ItemClassification.progression,
    "Bakunawa": ItemClassification.progression,
    "Dragon Valley": ItemClassification.progression,
    "Shenlin Park": ItemClassification.progression,
    "Tiger Falls": ItemClassification.progression,
    "Robot Graveyard": ItemClassification.progression,
    "Shade Armory": ItemClassification.progression,
    "Snowfields": ItemClassification.progression,
    "Avian Museum": ItemClassification.progression,
    "Airship Sigwada": ItemClassification.progression,
    "Phoenix Highway": ItemClassification.progression,
    "Zao Land": ItemClassification.progression,
    "The Battlesphere": ItemClassification.progression,
    "Globe Opera 1": ItemClassification.progression,
    "Globe Opera 2": ItemClassification.progression,
    "Auditorium": ItemClassification.progression,
    "Palace Courtyard": ItemClassification.progression,
    "Tidal Gate": ItemClassification.progression,
    "Sky Bridge": ItemClassification.progression,
    "Lightning Tower": ItemClassification.progression,
    "Zulon Jungle": ItemClassification.progression,
    "Nalao Lake": ItemClassification.progression,
    "Ancestral Forge": ItemClassification.progression,
    "Magma Starscape": ItemClassification.progression,
    "Diamond Point": ItemClassification.progression,
    "Gravity Bubble": ItemClassification.progression,
    "Bakunawa Chase": ItemClassification.progression,
    "Bakunawa Rush": ItemClassification.progression,
    "Refinery Room": ItemClassification.progression,
    "Clockwork Arboretum": ItemClassification.progression,
    "Inversion Dynamo": ItemClassification.progression,
    "Lunar Cannon": ItemClassification.progression,
    "Merga": ItemClassification.progression,
    
    "Chest Tracer - Dragon Valley": ItemClassification.progression,
    "Chest Tracer - Shenlin Park": ItemClassification.progression,
    "Chest Tracer - Tiger Falls": ItemClassification.progression,
    "Chest Tracer - Robot Graveyard": ItemClassification.progression,
    "Chest Tracer - Shade Armory": ItemClassification.progression,
    "Chest Tracer - Avian Museum": ItemClassification.progression,
    "Chest Tracer - Airship Sigwada": ItemClassification.progression,
    "Chest Tracer - Phoenix Highway": ItemClassification.progression,
    "Chest Tracer - Zao Land": ItemClassification.progression,
    "Chest Tracer - Globe Opera 1": ItemClassification.progression,
    "Chest Tracer - Globe Opera 2": ItemClassification.progression,
    "Chest Tracer - Palace Courtyard": ItemClassification.progression,
    "Chest Tracer - Tidal Gate": ItemClassification.progression,
    "Chest Tracer - Sky Bridge": ItemClassification.progression,
    "Chest Tracer - Lightning Tower": ItemClassification.progression,
    "Chest Tracer - Zulon Jungle": ItemClassification.progression,
    "Chest Tracer - Nalao Lake": ItemClassification.progression,
    "Chest Tracer - Ancestral Forge": ItemClassification.progression,
    "Chest Tracer - Magma Starscape": ItemClassification.progression,
    "Chest Tracer - Gravity Bubble": ItemClassification.progression,
    "Chest Tracer - Bakunawa Rush": ItemClassification.progression,
    "Chest Tracer - Clockwork Arboretum": ItemClassification.progression,
    "Chest Tracer - Inversion Dynamo": ItemClassification.progression,
    "Chest Tracer - Lunar Cannon": ItemClassification.progression,
    "Chest Tracer": ItemClassification.progression,
    
    "Swap Trap": ItemClassification.trap,
    "Mirror Trap": ItemClassification.trap,
    "Pie Trap": ItemClassification.trap,
    "Spring Trap": ItemClassification.trap,
    "PowerPoint Trap": ItemClassification.trap,
    "Zoom Trap": ItemClassification.trap,
    "Aaa Trap": ItemClassification.trap,
    "Spike Ball Trap": ItemClassification.trap,
    "Pixellation Trap": ItemClassification.trap,
    "Rail Trap": ItemClassification.trap,
    "Spam Trap": ItemClassification.trap,
    "Syntax Jumpscare Trap": ItemClassification.trap,
    
    "Crystals": ItemClassification.filler,
    "Extra Life": ItemClassification.filler,
    "Invincibility": ItemClassification.filler,
    "Wood Shield": ItemClassification.filler,
    "Earth Shield": ItemClassification.filler,
    "Water Shield": ItemClassification.filler,
    "Fire Shield": ItemClassification.filler,
    "Metal Shield": ItemClassification.filler,
    "Powerup": ItemClassification.filler,
    "Gold Gem": ItemClassification.filler
}

class FP2Item(Item):
    game = "Freedom Planet 2"

# Determines an item to act as filler.
def get_random_filler_item_name(world: FP2World) -> str:
    # Create the filler and trap item lists.
    filler_items = ["Extra Life", "Invincibility", "Wood Shield", "Earth Shield", "Water Shield", "Fire Shield", "Metal Shield", "Powerup"]
    trap_items = []
    
    # Add extra items to the filler list depend on our settings.
    if world.options.filler_star_cards: filler_items.append("Star Card")
    if world.options.filler_time_capsules: filler_items.append("Time Capsule")
    if world.options.milla_shop: filler_items.append("Gold Gem")
    if world.options.vinyl_shop: filler_items.append("Crystals")
    
    # Local function to add 1, 2 or 3 copies of a trap depending on its weight option.
    def get_trap_weights(option, trapName):
        if option >= 1: trap_items.append(trapName)
        if option >= 2: trap_items.append(trapName)
        if option == 3: trap_items.append(trapName)
    
    # Add the traps to the trap list.
    get_trap_weights(world.options.swap_trap_weight, "Swap Trap")
    get_trap_weights(world.options.mirror_trap_weight, "Mirror Trap")
    get_trap_weights(world.options.pie_trap_weight, "Pie Trap")
    get_trap_weights(world.options.spring_trap_weight, "Spring Trap")
    get_trap_weights(world.options.powerpoint_trap_weight, "PowerPoint Trap")
    get_trap_weights(world.options.zoom_trap_weight, "Zoom Trap")
    get_trap_weights(world.options.aaa_trap_weight, "Aaa Trap")
    get_trap_weights(world.options.spikeball_trap_weight, "Spike Ball Trap")
    get_trap_weights(world.options.pixellation_trap_weight, "Pixellation Trap")
    get_trap_weights(world.options.rail_trap_weight, "Rail Trap")
    get_trap_weights(world.options.spam_trap_weight, "Spam Trap")
    get_trap_weights(world.options.syntax_jumpscare_trap_weight, "Syntax Jumpscare Trap")
    
    # Add the negative Brave Stones to the trap list if the trap stones option is enabled.
    if world.options.trap_stones:
        trap_items.append("No Stocks")
        trap_items.append("Expensive Stocks")
        trap_items.append("Double Damage")
        trap_items.append("No Revivals")
        trap_items.append("No Guarding")
        trap_items.append("No Petals")
        trap_items.append("Time Limit")
        trap_items.append("Items To Bombs")
        trap_items.append("Life Oscillation")
        trap_items.append("One Hit KO")
        
    # Compare a random number to our filler traps value and return a trap if its less.
    # Also check that we actually HAVE any traps in the list.
    if world.random.randint(0, 99) < world.options.filler_traps and len(trap_items) > 0:
        return world.random.choice(trap_items)
    
    # Return a filler item.
    return world.random.choice(filler_items)

def create_item_with_correct_classification(world: FP2World, name: str) -> FP2Item:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return FP2Item(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: FP2World) -> None:
    # Create our item pool.
    itempool: list[Item] = [
        world.create_item("Potion - Extra Stock"),
        world.create_item("Potion - Strong Revivals"),
        world.create_item("Potion - Cheaper Stocks"),
        world.create_item("Potion - Healing Strike"),
        world.create_item("Potion - Attack Up"),
        world.create_item("Potion - Strong Shields"),
        world.create_item("Potion - Accelerator"),
        world.create_item("Potion - Super Feather"),
        world.create_item("Element Burst"),
        world.create_item("Max Life Up"),
        world.create_item("Crystals to Petals"),
        world.create_item("Powerup Start"),
        world.create_item("Shadow Guard"),
        world.create_item("Payback Ring"),
        world.create_item("Wood Charm"),
        world.create_item("Earth Charm"),
        world.create_item("Water Charm"),
        world.create_item("Fire Charm"),
        world.create_item("Metal Charm"),
        world.create_item("No Stocks"),
        world.create_item("Expensive Stocks"),
        world.create_item("Double Damage"),
        world.create_item("No Revivals"),
        world.create_item("No Guarding"),
        world.create_item("No Petals"),
        world.create_item("Time Limit"),
        world.create_item("Items To Bombs"),
        world.create_item("Life Oscillation"),
        world.create_item("One Hit KO"),
        world.create_item("Petal Armor"),
        world.create_item("Rainbow Charm"),
    ]
    
    # Loop and create the multitude items.
    for _ in range(48): itempool.append(world.create_item("Star Card"))
    for _ in range(21): itempool.append(world.create_item("Time Capsule"))
    for _ in range(18): itempool.append(world.create_item("Battlesphere Key"))
    
    # Add the extra slot items if the option is enabled.
    if world.options.extra_items:
        itempool.append(world.create_item("Extra Item Slot")),
        itempool.append(world.create_item("Extra Item Slot")),
        itempool.append(world.create_item("Extra Potion Slot")),
        itempool.append(world.create_item("Extra Potion Slot")),

    # Add the Chest Tracers if both the Chests and Chest Tracer Items options are enabled.
    if world.options.chests:
        if world.options.chest_tracer_items == 1:
            itempool.append(world.create_item("Chest Tracer - Dragon Valley"))
            itempool.append(world.create_item("Chest Tracer - Shenlin Park"))
            itempool.append(world.create_item("Chest Tracer - Tiger Falls"))
            itempool.append(world.create_item("Chest Tracer - Robot Graveyard"))
            itempool.append(world.create_item("Chest Tracer - Shade Armory"))
            itempool.append(world.create_item("Chest Tracer - Avian Museum"))
            itempool.append(world.create_item("Chest Tracer - Airship Sigwada"))
            itempool.append(world.create_item("Chest Tracer - Phoenix Highway"))
            itempool.append(world.create_item("Chest Tracer - Zao Land"))
            itempool.append(world.create_item("Chest Tracer - Globe Opera 1"))
            itempool.append(world.create_item("Chest Tracer - Globe Opera 2"))
            itempool.append(world.create_item("Chest Tracer - Palace Courtyard"))
            itempool.append(world.create_item("Chest Tracer - Tidal Gate"))
            itempool.append(world.create_item("Chest Tracer - Sky Bridge"))
            itempool.append(world.create_item("Chest Tracer - Lightning Tower"))
            itempool.append(world.create_item("Chest Tracer - Zulon Jungle"))
            itempool.append(world.create_item("Chest Tracer - Nalao Lake"))
            itempool.append(world.create_item("Chest Tracer - Ancestral Forge"))
            itempool.append(world.create_item("Chest Tracer - Magma Starscape"))
            itempool.append(world.create_item("Chest Tracer - Gravity Bubble"))
            itempool.append(world.create_item("Chest Tracer - Bakunawa Rush"))
            itempool.append(world.create_item("Chest Tracer - Clockwork Arboretum"))
            itempool.append(world.create_item("Chest Tracer - Inversion Dynamo"))
            itempool.append(world.create_item("Chest Tracer - Lunar Cannon"))
        if world.options.chest_tracer_items == 2:
            itempool.append(world.create_item("Chest Tracer"))
            
    # Add the chapter/stage unlocks depending on the value of the Chapters option.
    if world.options.chapters == 0:
            # Add the individual chapter items to the item pool.
            itempool.append(world.create_item("Mystery of the Frozen North"))
            itempool.append(world.create_item("Sky Pirate Panic"))
            itempool.append(world.create_item("Enter the Battlesphere"))
            itempool.append(world.create_item("Globe Opera"))
            itempool.append(world.create_item("Justice in the Sky Paradise"))
            itempool.append(world.create_item("Robot Wars! Snake VS Tarsier"))
            itempool.append(world.create_item("Echoes of the Dragon War"))
            itempool.append(world.create_item("Bakunawa"))
            
    if world.options.chapters == 1:
            # Add the Progressive Chapter item to the item pool.
            itempool.append(world.create_item("Progressive Chapter"))
            itempool.append(world.create_item("Progressive Chapter"))
            itempool.append(world.create_item("Progressive Chapter"))
            itempool.append(world.create_item("Progressive Chapter"))
            itempool.append(world.create_item("Progressive Chapter"))
            itempool.append(world.create_item("Progressive Chapter"))
            itempool.append(world.create_item("Progressive Chapter"))
            itempool.append(world.create_item("Progressive Chapter"))
            
    if world.options.chapters == 2:
        # Add the Battlesphere unlock item, as there's no point in picking it as a starting stage thanks to the key requirements.
        itempool.append(world.create_item("The Battlesphere"))
        
        # Create a list of the stages and boss stages.
        stage_items = ["Dragon Valley", "Shenlin Park", "Tiger Falls", "Robot Graveyard", "Shade Armory", "Avian Museum", "Airship Sigwada", "Phoenix Highway", "Zao Land", "Globe Opera 1", "Globe Opera 2", "Palace Courtyard", "Tidal Gate", "Sky Bridge", "Lightning Tower", "Zulon Jungle", "Nalao Lake", "Ancestral Forge", "Magma Starscape", "Gravity Bubble", "Bakunawa Chase", "Bakunawa Rush", "Clockwork Arboretum", "Inversion Dynamo", "Lunar Cannon"]
        boss_items = ["Snowfields", "Auditorium", "Diamond Point", "Refinery Room", "Merga"]
            
        # Pick a starting stage and starting boss.
        starting_stage = world.random.choice(stage_items)
        starting_boss = world.random.choice(boss_items)
        
        # Add the items for the other stages and bosses to the item pool.
        for stage in stage_items:
            if stage != starting_stage:
                itempool.append(world.create_item(stage))
        for boss in boss_items:
            if boss != starting_boss:
                itempool.append(world.create_item(boss))
                    
        # Create and precollect the chosen starting stage and boss.
        world.push_precollected(world.create_item(starting_stage))
        world.push_precollected(world.create_item(starting_boss))

    # Get the count of items in our pool.
    number_of_items = len(itempool)

    # Determine how many locations we have yet to fill.
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Calculate how much filler we need.
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Loop through the required amount of filler.
    for _ in range(needed_number_of_filler_items):
        # Pick a random filler item.
        itemName = world.get_filler_item_name()
        
        # If the selected item is a Star Card or Time Capsule then specifically create it as a filler.
        if (itemName == "Star Card" or itemName == "Time Capsule"):
            itempool.append(FP2Item(itemName, ItemClassification.filler, ITEM_NAME_TO_ID[itemName], world.player))
            
        # If not, then just use the normal create_item function.
        else:
            itempool.append(world.create_item(itemName))

    # Add our pool to the multiworld's.
    world.multiworld.itempool += itempool
    
# Handles marking the eight Super Feather Potion required chests are valid (if out of logic) in Universal Tracker.
class FP2UTGlitchFlag(Item):
    game: str = "Freedom Planet 2"
    FLAG_NAME = "[UT Glitch Logic Flag]"

    def __init__(self, player) -> None:
        super().__init__(name=self.FLAG_NAME, classification=ItemClassification.progression, code=None, player=player)