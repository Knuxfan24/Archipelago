from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import CollectionState, Location
from worlds.generic.Rules import add_rule, set_rule
import math
if TYPE_CHECKING:
    from .world import FP2World

def set_all_rules(world: FP2World) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: FP2World) -> None:
    # Get the entrances to the stage regions.
    dValley = world.get_entrance("Menu to Dragon Valley")
    sPark = world.get_entrance("Menu to Shenlin Park")
    tFalls = world.get_entrance("Menu to Tiger Falls")
    rGraveyard = world.get_entrance("Menu to Robot Graveyard")
    sArmory = world.get_entrance("Menu to Shade Armory")
    snowfields = world.get_entrance("Menu to Snowfields")
    aMuseum = world.get_entrance("Menu to Avian Museum")
    aSigwada = world.get_entrance("Menu to Airship Sigwada")
    pHighway = world.get_entrance("Menu to Phoenix Highway")
    zLand = world.get_entrance("Menu to Zao Land")
    battlesphere = world.get_entrance("Menu to The Battlesphere")
    gOpera1 = world.get_entrance("Menu to Globe Opera 1")
    gOpera2 = world.get_entrance("Menu to Globe Opera 2")
    auditorium = world.get_entrance("Menu to Auditorium")
    pCourtyard = world.get_entrance("Menu to Palace Courtyard")
    tGate = world.get_entrance("Menu to Tidal Gate")
    sBridge = world.get_entrance("Menu to Sky Bridge")
    lTower = world.get_entrance("Menu to Lightning Tower")
    zJungle = world.get_entrance("Menu to Zulon Jungle")
    nLake = world.get_entrance("Menu to Nalao Lake")
    aForge = world.get_entrance("Menu to Ancestral Forge")
    mStarscape = world.get_entrance("Menu to Magma Starscape")
    dPoint = world.get_entrance("Menu to Diamond Point")
    gBubble = world.get_entrance("Menu to Gravity Bubble")
    bChase = world.get_entrance("Menu to Bakunawa Chase")
    bRush = world.get_entrance("Menu to Bakunawa Rush")
    rRoom = world.get_entrance("Menu to Refinery Room")
    cArboretum = world.get_entrance("Menu to Clockwork Arboretum")
    iDynamo = world.get_entrance("Menu to Inversion Dynamo")
    lCannon = world.get_entrance("Menu to Lunar Cannon")
    merga = world.get_entrance("Menu to Merga")
    wCore = world.get_entrance("Menu to Weapon's Core")

    # Set up requirements for accessing the stages.
    # Dragon Valley and Shenlin Park are only locked if using Open Stages, so they have a seperate function.
    def requiresDragonValleyAccess(state: CollectionState) -> bool:
        if world.options.chapters == 2: return state.has("Dragon Valley", world.player)
        else: return True
    def requiresShenlinParkAccess(state: CollectionState) -> bool:
        if world.options.chapters == 2: return state.has("Shenlin Park", world.player)
        else: return True
        
    # Checks if the player has access to a stage depending on the value of the Chapters option.
    def stageAccessCheck(chapterName, starCardCount, progressiveChapterCount, stageName) -> bool:
        if world.options.chapters == 0: return lambda state: state.has_all_counts({chapterName: 1, "Star Card": starCardCount}, world.player)
        if world.options.chapters == 1: return lambda state: state.has_all_counts({"Progressive Chapter": progressiveChapterCount, "Star Card": starCardCount}, world.player)
        if world.options.chapters == 2: return lambda state: state.has(stageName, world.player)
        
    # Checks if the player has the required items to access Weapon's Core and beat the game.
    def GoModeCheck(state: CollectionState) -> bool:
        if state.has("Star Card", world.player, 32) == False: return False
        if state.has("Time Capsule", world.player, 13) == False: return False
        if world.options.chapters == 0: return state.has("Bakunawa", world.player)
        if world.options.chapters == 1: return state.has("Progressive Chapter", world.player, 8)
        return True

    # Sets all the access rules for the stages.
    set_rule(dValley, requiresDragonValleyAccess)
    set_rule(sPark, requiresShenlinParkAccess)
    set_rule(tFalls, stageAccessCheck("Mystery of the Frozen North", 0, 1, "Tiger Falls"))
    set_rule(rGraveyard, stageAccessCheck("Mystery of the Frozen North", 0, 1, "Robot Graveyard"))
    set_rule(sArmory, stageAccessCheck("Mystery of the Frozen North", 0, 1, "Shade Armory"))
    set_rule(snowfields, stageAccessCheck("Mystery of the Frozen North", 0, 1, "Snowfields"))
    set_rule(aMuseum, stageAccessCheck("Sky Pirate Panic", 0, 2, "Avian Museum"))
    set_rule(aSigwada, stageAccessCheck("Sky Pirate Panic", 0, 2, "Airship Sigwada"))
    set_rule(pHighway, stageAccessCheck("Enter the Battlesphere", 0, 3, "Phoenix Highway"))
    set_rule(zLand, stageAccessCheck("Enter the Battlesphere", 0, 3, "Zao Land"))
    set_rule(battlesphere, stageAccessCheck("Enter the Battlesphere", 0, 3, "The Battlesphere"))
    set_rule(gOpera1, stageAccessCheck("Globe Opera", 11, 4, "Globe Opera 1"))
    set_rule(gOpera2, stageAccessCheck("Globe Opera", 11, 4, "Globe Opera 2"))
    set_rule(auditorium, stageAccessCheck("Globe Opera", 11, 4, "Auditorium"))
    set_rule(pCourtyard, stageAccessCheck("Globe Opera", 11, 4, "Palace Courtyard"))
    set_rule(tGate, stageAccessCheck("Globe Opera", 11, 4, "Tidal Gate"))
    set_rule(sBridge, stageAccessCheck("Justice in the Sky Paradise", 11, 5, "Sky Bridge"))
    set_rule(lTower, stageAccessCheck("Justice in the Sky Paradise", 11, 5, "Lightning Tower"))
    set_rule(zJungle, stageAccessCheck("Robot Wars! Snake VS Tarsier", 11, 6, "Zulon Jungle"))
    set_rule(nLake, stageAccessCheck("Robot Wars! Snake VS Tarsier", 11, 6, "Nalao Lake"))
    set_rule(aForge, stageAccessCheck("Echoes of the Dragon War", 11, 7, "Ancestral Forge"))
    set_rule(mStarscape, stageAccessCheck("Echoes of the Dragon War", 11, 7, "Magma Starscape"))
    set_rule(dPoint, stageAccessCheck("Echoes of the Dragon War", 11, 7, "Diamond Point"))
    set_rule(gBubble, stageAccessCheck("Bakunawa", 23, 8, "Gravity Bubble"))
    set_rule(bChase, stageAccessCheck("Bakunawa", 23, 8, "Bakunawa Chase"))
    set_rule(bRush, stageAccessCheck("Bakunawa", 23, 8, "Bakunawa Rush"))
    set_rule(rRoom, stageAccessCheck("Bakunawa", 23, 8, "Refinery Room"))
    set_rule(cArboretum, stageAccessCheck("Bakunawa", 23, 8, "Clockwork Arboretum"))
    set_rule(iDynamo, stageAccessCheck("Bakunawa", 23, 8, "Inversion Dynamo"))
    set_rule(lCannon, stageAccessCheck("Bakunawa", 23, 8, "Lunar Cannon"))
    set_rule(merga, stageAccessCheck("Bakunawa", 23, 8, "Merga"))
    set_rule(wCore, GoModeCheck)

    # If the Chests option is enabled and the chest tracers are included in item form, then add rules for them as well.
    if world.options.chests and world.options.chest_tracer_items > 0 and world.options.chest_tracers:
        # Get the entrances to the chest regions.
        dValleyChests = world.get_entrance("Dragon Valley Chest Inclusion")
        sParkChests = world.get_entrance("Shenlin Park Chest Inclusion")
        tFallsChests = world.get_entrance("Tiger Falls Chest Inclusion")
        rGraveyardChests = world.get_entrance("Robot Graveyard Chest Inclusion")
        sArmoryChests = world.get_entrance("Shade Armory Chest Inclusion")
        aMuseumChests = world.get_entrance("Avian Museum Chest Inclusion")
        aSigwadaChests = world.get_entrance("Airship Sigwada Chest Inclusion")
        pHighwayChests = world.get_entrance("Phoenix Highway Chest Inclusion")
        zLandChests = world.get_entrance("Zao Land Chest Inclusion")
        gOpera1Chests = world.get_entrance("Globe Opera 1 Chest Inclusion")
        gOpera2Chests = world.get_entrance("Globe Opera 2 Chest Inclusion")
        pCourtyardChests = world.get_entrance("Palace Courtyard Chest Inclusion")
        tGateChests = world.get_entrance("Tidal Gate Chest Inclusion")
        sBridgeChests = world.get_entrance("Sky Bridge Chest Inclusion")
        lTowerChests = world.get_entrance("Lightning Tower Chest Inclusion")
        zJungleChests = world.get_entrance("Zulon Jungle Chest Inclusion")
        nLakeChests = world.get_entrance("Nalao Lake Chest Inclusion")
        aForgeChests = world.get_entrance("Ancestral Forge Chest Inclusion")
        mStarscapeChests = world.get_entrance("Magma Starscape Chest Inclusion")
        gBubbleChests = world.get_entrance("Gravity Bubble Chest Inclusion")
        bRushChests = world.get_entrance("Bakunawa Rush Chest Inclusion")
        cArboretumChests = world.get_entrance("Clockwork Arboretum Chest Inclusion")
        iDynamoChests = world.get_entrance("Inversion Dynamo Chest Inclusion")
        lCannonChests = world.get_entrance("Lunar Cannon Chest Inclusion")
        
        # Assign a requirement of the stage's chest tracer or the global one to each entrance.
        set_rule(dValleyChests, lambda state: state.has_any(["Chest Tracer - Dragon Valley", "Chest Tracer"], world.player))
        set_rule(sParkChests, lambda state: state.has_any(["Chest Tracer - Shenlin Park", "Chest Tracer"], world.player))
        set_rule(tFallsChests, lambda state: state.has_any(["Chest Tracer - Tiger Falls", "Chest Tracer"], world.player))
        set_rule(rGraveyardChests, lambda state: state.has_any(["Chest Tracer - Robot Graveyard", "Chest Tracer"], world.player))
        set_rule(sArmoryChests, lambda state: state.has_any(["Chest Tracer - Shade Armory", "Chest Tracer"], world.player))
        set_rule(aMuseumChests, lambda state: state.has_any(["Chest Tracer - Avian Museum", "Chest Tracer"], world.player))
        set_rule(aSigwadaChests, lambda state: state.has_any(["Chest Tracer - Airship Sigwada", "Chest Tracer"], world.player))
        set_rule(pHighwayChests, lambda state: state.has_any(["Chest Tracer - Phoenix Highway", "Chest Tracer"], world.player))
        set_rule(zLandChests, lambda state: state.has_any(["Chest Tracer - Zao Land", "Chest Tracer"], world.player))
        set_rule(gOpera1Chests, lambda state: state.has_any(["Chest Tracer - Globe Opera 1", "Chest Tracer"], world.player))
        set_rule(gOpera2Chests, lambda state: state.has_any(["Chest Tracer - Globe Opera 2", "Chest Tracer"], world.player))
        set_rule(pCourtyardChests, lambda state: state.has_any(["Chest Tracer - Palace Courtyard", "Chest Tracer"], world.player))
        set_rule(tGateChests, lambda state: state.has_any(["Chest Tracer - Tidal Gate", "Chest Tracer"], world.player))
        set_rule(sBridgeChests, lambda state: state.has_any(["Chest Tracer - Sky Bridge", "Chest Tracer"], world.player))
        set_rule(lTowerChests, lambda state: state.has_any(["Chest Tracer - Lightning Tower", "Chest Tracer"], world.player))
        set_rule(zJungleChests, lambda state: state.has_any(["Chest Tracer - Zulon Jungle", "Chest Tracer"], world.player))
        set_rule(nLakeChests, lambda state: state.has_any(["Chest Tracer - Nalao Lake", "Chest Tracer"], world.player))
        set_rule(aForgeChests, lambda state: state.has_any(["Chest Tracer - Ancestral Forge", "Chest Tracer"], world.player))
        set_rule(mStarscapeChests, lambda state: state.has_any(["Chest Tracer - Magma Starscape", "Chest Tracer"], world.player))
        set_rule(gBubbleChests, lambda state: state.has_any(["Chest Tracer - Gravity Bubble", "Chest Tracer"], world.player))
        set_rule(bRushChests, lambda state: state.has_any(["Chest Tracer - Bakunawa Rush", "Chest Tracer"], world.player))
        set_rule(cArboretumChests, lambda state: state.has_any(["Chest Tracer - Clockwork Arboretum", "Chest Tracer"], world.player))
        set_rule(iDynamoChests, lambda state: state.has_any(["Chest Tracer - Inversion Dynamo", "Chest Tracer"], world.player))
        set_rule(lCannonChests, lambda state: state.has_any(["Chest Tracer - Lunar Cannon", "Chest Tracer"], world.player))
        
def set_all_location_rules(world: FP2World) -> None:
    # Set the key requirements for the Battlesphere Challenges.
    battlesphereChallenge1 = world.get_location("Beginner's Gauntlet")
    battlesphereChallenge2 = world.get_location("Battlebot Battle Royale")
    battlesphereChallenge3 = world.get_location("Hero Battle Royale")
    battlesphereChallenge4 = world.get_location("Kalaw's Challenge")
    battlesphereChallenge5 = world.get_location("Army of One")
    battlesphereChallenge6 = world.get_location("Ring-Out Challenge")
    battlesphereChallenge7 = world.get_location("Flip Fire Gauntlet")
    battlesphereChallenge8 = world.get_location("Vanishing Maze")
    battlesphereChallenge9 = world.get_location("Mondo Condo")
    battlesphereChallenge10 = world.get_location("Birds of Prey")
    battlesphereChallenge11 = world.get_location("Battlebot Revenge")
    battlesphereChallenge12 = world.get_location("Mach Speed Melee")
    battlesphereChallenge13 = world.get_location("Galactic Rumble")
    battlesphereChallenge14 = world.get_location("Stop and Go")
    battlesphereChallenge15 = world.get_location("Mecha Madness")
    battlesphereChallenge16 = world.get_location("Rolling Thunder")
    battlesphereChallenge17 = world.get_location("Blast from the Past")
    battlesphereChallenge18 = world.get_location("Bubble Battle")
    set_rule(battlesphereChallenge1, lambda state: state.has("Battlesphere Key", world.player, 1))
    set_rule(battlesphereChallenge2, lambda state: state.has("Battlesphere Key", world.player, 2))
    set_rule(battlesphereChallenge3, lambda state: state.has("Battlesphere Key", world.player, 3))
    set_rule(battlesphereChallenge4, lambda state: state.has("Battlesphere Key", world.player, 4))
    set_rule(battlesphereChallenge5, lambda state: state.has("Battlesphere Key", world.player, 5))
    set_rule(battlesphereChallenge6, lambda state: state.has("Battlesphere Key", world.player, 6))
    set_rule(battlesphereChallenge7, lambda state: state.has("Battlesphere Key", world.player, 7))
    set_rule(battlesphereChallenge8, lambda state: state.has("Battlesphere Key", world.player, 8))
    set_rule(battlesphereChallenge9, lambda state: state.has("Battlesphere Key", world.player, 9))
    set_rule(battlesphereChallenge10, lambda state: state.has("Battlesphere Key", world.player, 10))
    set_rule(battlesphereChallenge11, lambda state: state.has("Battlesphere Key", world.player, 11))
    set_rule(battlesphereChallenge12, lambda state: state.has("Battlesphere Key", world.player, 12))
    set_rule(battlesphereChallenge13, lambda state: state.has("Battlesphere Key", world.player, 13))
    set_rule(battlesphereChallenge14, lambda state: state.has("Battlesphere Key", world.player, 14))
    set_rule(battlesphereChallenge15, lambda state: state.has("Battlesphere Key", world.player, 15))
    set_rule(battlesphereChallenge16, lambda state: state.has("Battlesphere Key", world.player, 16))
    set_rule(battlesphereChallenge17, lambda state: state.has("Battlesphere Key", world.player, 17))
    set_rule(battlesphereChallenge18, lambda state: state.has("Battlesphere Key", world.player, 18))
    
    # A few chests logically expect the Super Feather Potion (tested primarily with Neera).
    if world.options.chests:
        set_rule(world.get_location("Shenlin Park - Chest 1"), lambda state: state.has("Potion - Super Feather", world.player))
        set_rule(world.get_location("Tiger Falls - Chest 3"), lambda state: state.has("Potion - Super Feather", world.player))
        set_rule(world.get_location("Tiger Falls - Chest 4"), lambda state: state.has("Potion - Super Feather", world.player))
        set_rule(world.get_location("Airship Sigwada - Chest 1"), lambda state: state.has("Potion - Super Feather", world.player))
        set_rule(world.get_location("Globe Opera 2 - Chest 1"), lambda state: state.has("Potion - Super Feather", world.player))
        set_rule(world.get_location("Zulon Jungle - Chest 1"), lambda state: state.has("Potion - Super Feather", world.player))
        set_rule(world.get_location("Nalao Lake - Chest 2"), lambda state: state.has("Potion - Super Feather", world.player))
        set_rule(world.get_location("Nalao Lake - Chest 3"), lambda state: state.has("Potion - Super Feather", world.player))
        
        # Add the check for the Universal Tracker glitched logic item, as these chests are easily grabbable with the others without too much effort.
        add_rule(world.get_location("Shenlin Park - Chest 1"), lambda state: state.has(world.glitches_item_name, world.player), "or")
        add_rule(world.get_location("Tiger Falls - Chest 3"), lambda state: state.has(world.glitches_item_name, world.player), "or")
        add_rule(world.get_location("Tiger Falls - Chest 4"), lambda state: state.has(world.glitches_item_name, world.player), "or")
        add_rule(world.get_location("Airship Sigwada - Chest 1"), lambda state: state.has(world.glitches_item_name, world.player), "or")
        add_rule(world.get_location("Globe Opera 2 - Chest 1"), lambda state: state.has(world.glitches_item_name, world.player), "or")
        add_rule(world.get_location("Zulon Jungle - Chest 1"), lambda state: state.has(world.glitches_item_name, world.player), "or")
        add_rule(world.get_location("Nalao Lake - Chest 2"), lambda state: state.has(world.glitches_item_name, world.player), "or")
        add_rule(world.get_location("Nalao Lake - Chest 3"), lambda state: state.has(world.glitches_item_name, world.player), "or")
        
    # Add the Battlesphere Key requirements for the Item Boxes.
    if world.options.item_boxes:
        if world.options.item_boxes_crystals:
            set_rule(world.get_location("Beginner's Gauntlet - Crystal Box 1"), lambda state: state.has("Battlesphere Key", world.player, 1))
            set_rule(world.get_location("Beginner's Gauntlet - Crystal Box 2"), lambda state: state.has("Battlesphere Key", world.player, 1))
            set_rule(world.get_location("Beginner's Gauntlet - Crystal Box 3"), lambda state: state.has("Battlesphere Key", world.player, 1))
            set_rule(world.get_location("Flip Fire Gauntlet - Crystal Box 1"), lambda state: state.has("Battlesphere Key", world.player, 7))
            set_rule(world.get_location("Flip Fire Gauntlet - Crystal Box 2"), lambda state: state.has("Battlesphere Key", world.player, 7))
            set_rule(world.get_location("Stop and Go - Crystal Box 1"), lambda state: state.has("Battlesphere Key", world.player, 14))
            set_rule(world.get_location("Stop and Go - Crystal Box 2"), lambda state: state.has("Battlesphere Key", world.player, 14))
            set_rule(world.get_location("Stop and Go - Crystal Box 3"), lambda state: state.has("Battlesphere Key", world.player, 14))
            set_rule(world.get_location("Mach Speed Melee - Crystal Box 1"), lambda state: state.has("Battlesphere Key", world.player, 12))
            set_rule(world.get_location("Mach Speed Melee - Crystal Box 2"), lambda state: state.has("Battlesphere Key", world.player, 12))
            set_rule(world.get_location("Mach Speed Melee - Crystal Box 3"), lambda state: state.has("Battlesphere Key", world.player, 12))
            set_rule(world.get_location("Mach Speed Melee - Crystal Box 4"), lambda state: state.has("Battlesphere Key", world.player, 12))
            set_rule(world.get_location("Mach Speed Melee - Crystal Box 5"), lambda state: state.has("Battlesphere Key", world.player, 12))
            set_rule(world.get_location("Rolling Thunder - Crystal Box 1"), lambda state: state.has("Battlesphere Key", world.player, 16))
            set_rule(world.get_location("Rolling Thunder - Crystal Box 2"), lambda state: state.has("Battlesphere Key", world.player, 16))
            set_rule(world.get_location("Mondo Condo - Crystal Box 1"), lambda state: state.has("Battlesphere Key", world.player, 9))
            set_rule(world.get_location("Mondo Condo - Crystal Box 2"), lambda state: state.has("Battlesphere Key", world.player, 9))
            set_rule(world.get_location("Mondo Condo - Crystal Box 3"), lambda state: state.has("Battlesphere Key", world.player, 9))
            set_rule(world.get_location("Mondo Condo - Crystal Box 4"), lambda state: state.has("Battlesphere Key", world.player, 9))
            set_rule(world.get_location("Mondo Condo - Crystal Box 5"), lambda state: state.has("Battlesphere Key", world.player, 9))
            set_rule(world.get_location("Mondo Condo - Crystal Box 6"), lambda state: state.has("Battlesphere Key", world.player, 9))
            set_rule(world.get_location("Mondo Condo - Crystal Box 7"), lambda state: state.has("Battlesphere Key", world.player, 9))
            set_rule(world.get_location("Mondo Condo - Crystal Box 8"), lambda state: state.has("Battlesphere Key", world.player, 9))
            set_rule(world.get_location("Mondo Condo - Crystal Box 9"), lambda state: state.has("Battlesphere Key", world.player, 9))
            set_rule(world.get_location("Mondo Condo - Crystal Box 10"), lambda state: state.has("Battlesphere Key", world.player, 9))
            set_rule(world.get_location("Vanishing Maze - Crystal Box 1"), lambda state: state.has("Battlesphere Key", world.player, 8))
            set_rule(world.get_location("Vanishing Maze - Crystal Box 2"), lambda state: state.has("Battlesphere Key", world.player, 8))
            set_rule(world.get_location("Vanishing Maze - Crystal Box 3"), lambda state: state.has("Battlesphere Key", world.player, 8))
            set_rule(world.get_location("Vanishing Maze - Crystal Box 4"), lambda state: state.has("Battlesphere Key", world.player, 8))
            set_rule(world.get_location("Vanishing Maze - Crystal Box 5"), lambda state: state.has("Battlesphere Key", world.player, 8))
         
        if world.options.item_boxes_petals:
            set_rule(world.get_location("Stop and Go - Petal Box"), lambda state: state.has("Battlesphere Key", world.player, 14))
            set_rule(world.get_location("Mach Speed Melee - Petal Box"), lambda state: state.has("Battlesphere Key", world.player, 12))
            set_rule(world.get_location("Vanishing Maze - Petal Box 1"), lambda state: state.has("Battlesphere Key", world.player, 8))
            set_rule(world.get_location("Vanishing Maze - Petal Box 2"), lambda state: state.has("Battlesphere Key", world.player, 8))
            set_rule(world.get_location("Battlebot Battle Royale - Petal Box"), lambda state: state.has("Battlesphere Key", world.player, 2))
            
        if world.options.item_boxes_shields:
            set_rule(world.get_location("Beginner's Gauntlet - Metal Shield Box"), lambda state: state.has("Battlesphere Key", world.player, 1))
            set_rule(world.get_location("Beginner's Gauntlet - Wood Shield Box"), lambda state: state.has("Battlesphere Key", world.player, 1))
            set_rule(world.get_location("Beginner's Gauntlet - Petal Box"), lambda state: state.has("Battlesphere Key", world.player, 1))
            set_rule(world.get_location("Flip Fire Gauntlet - Fire Shield Box"), lambda state: state.has("Battlesphere Key", world.player, 7))
            set_rule(world.get_location("Vanishing Maze - Metal Shield Box"), lambda state: state.has("Battlesphere Key", world.player, 8))
            set_rule(world.get_location("Vanishing Maze - Wood Shield Box"), lambda state: state.has("Battlesphere Key", world.player, 8))
            set_rule(world.get_location("Mecha Madness - Wood Shield Box"), lambda state: state.has("Battlesphere Key", world.player, 15))
            set_rule(world.get_location("Mecha Madness - Fire Shield Box"), lambda state: state.has("Battlesphere Key", world.player, 15))
            
            
        
    # Set the Star Card requirements for the two shops if they're enabled. 
    def set_shop_rules(shopName):       
        # Get the locations for this shop. 
        locations = world.get_region(shopName).get_locations()
        
        # Determine how much we need to multiply the location index by.
        # TODO: If we manage to make the Star Card count scale by location count in the multiworld, then unhardcode this 30.
        multiplication_range = 30 / len(locations)
        
        # Set up a location index starting at 1.
        locationIndex = 1
        
        # Loop through each location to calculate its requirement, set it and increment the location index.
        for location in locations:
            starCardRequirement = math.ceil(multiplication_range * locationIndex)
            set_rule(location, lambda state, count=starCardRequirement: state.has("Star Card", world.player, count))
            locationIndex += 1
            
            # Debug print to show the Star Card cost for this location
            # print(location.name + " requires " + str(starCardRequirement) + " Star Cards.")
    
    if world.options.milla_shop: set_shop_rules("Milla Shop")
    if world.options.vinyl_shop: set_shop_rules("Vinyl Shop")
    
    # Set up requirements for accessing the stages.
    # Dragon Valley and Shenlin Park are only locked if using Open Stages, so they have a seperate function.
    def requiresDragonValleyAccess(state: CollectionState) -> bool:
        if world.options.chapters == 2: return state.has("Dragon Valley", world.player)
        else: return True
    def requiresShenlinParkAccess(state: CollectionState) -> bool:
        if world.options.chapters == 2: return state.has("Shenlin Park", world.player)
        else: return True
        
    # For the Battlesphere, we need to also check if the player has enough keys to access the challenge this enemy/boss is in.
    def requiresBattlesphereChallenge(keyCount) -> bool:
        if world.options.chapters == 0: return lambda state: state.has_all_counts({"Enter the Battlesphere": 1, "Battlesphere Key": keyCount}, world.player)
        if world.options.chapters == 1: return lambda state: state.has_all_counts({"Progressive Chapter": 3, "Battlesphere Key": keyCount}, world.player)
        if world.options.chapters == 2: return lambda state: state.has_all_counts({"The Battlesphere": 1, "Battlesphere Key": keyCount}, world.player)
        
    # Checks if the player has access to a stage depending on the value of the Chapters option.
    def stageAccessCheck(chapterName, starCardCount, progressiveChapterCount, stageName) -> bool:
        if world.options.chapters == 0: return lambda state: state.has_all_counts({chapterName: 1, "Star Card": starCardCount}, world.player)
        if world.options.chapters == 1: return lambda state: state.has_all_counts({"Progressive Chapter": progressiveChapterCount, "Star Card": starCardCount}, world.player)
        if world.options.chapters == 2: return lambda state: state.has(stageName, world.player)
        
    # Get the various stage access requirements for usage in enemy and boss sanity.
    tFalls = stageAccessCheck("Mystery of the Frozen North", 0, 1, "Tiger Falls")
    rGraveyard = stageAccessCheck("Mystery of the Frozen North", 0, 1, "Robot Graveyard")
    sArmory = stageAccessCheck("Mystery of the Frozen North", 0, 1, "Shade Armory")
    snowfields = stageAccessCheck("Mystery of the Frozen North", 0, 1, "Snowfields")
    aMuseum = stageAccessCheck("Sky Pirate Panic", 0, 2, "Avian Museum")
    aSigwada = stageAccessCheck("Sky Pirate Panic", 0, 2, "Airship Sigwada")
    pHighway = stageAccessCheck("Enter the Battlesphere", 0, 3, "Phoenix Highway")
    zLand = stageAccessCheck("Enter the Battlesphere", 0, 3, "Zao Land")
    gOpera1 = stageAccessCheck("Globe Opera", 11, 4, "Globe Opera 1")
    gOpera2 = stageAccessCheck("Globe Opera", 11, 4, "Globe Opera 2")
    auditorium = stageAccessCheck("Globe Opera", 11, 4, "Auditorium")
    pCourtyard = stageAccessCheck("Globe Opera", 11, 4, "Palace Courtyard")
    tGate = stageAccessCheck("Globe Opera", 11, 4, "Tidal Gate")
    sBridge = stageAccessCheck("Justice in the Sky Paradise", 11, 5, "Sky Bridge")
    lTower = stageAccessCheck("Justice in the Sky Paradise", 11, 5, "Lightning Tower")
    zJungle = stageAccessCheck("Robot Wars! Snake VS Tarsier", 11, 6, "Zulon Jungle")
    nLake = stageAccessCheck("Robot Wars! Snake VS Tarsier", 11, 6, "Nalao Lake")
    aForge = stageAccessCheck("Echoes of the Dragon War", 11, 7, "Ancestral Forge")
    mStarscape = stageAccessCheck("Echoes of the Dragon War", 11, 7, "Magma Starscape")
    dPoint = stageAccessCheck("Echoes of the Dragon War", 11, 7, "Diamond Point")
    gBubble = stageAccessCheck("Bakunawa", 23, 8, "Gravity Bubble")
    bChase = stageAccessCheck("Bakunawa", 23, 8, "Bakunawa Chase")
    bRush = stageAccessCheck("Bakunawa", 23, 8, "Bakunawa Rush")
    rRoom = stageAccessCheck("Bakunawa", 23, 8, "Refinery Room")
    cArboretum = stageAccessCheck("Bakunawa", 23, 8, "Clockwork Arboretum")
    iDynamo = stageAccessCheck("Bakunawa", 23, 8, "Inversion Dynamo")
    lCannon = stageAccessCheck("Bakunawa", 23, 8, "Lunar Cannon")
    merga = stageAccessCheck("Bakunawa", 23, 8, "Merga")
    
    # If enemy sanity is enabled, then set the rules for them.
    if world.options.enemies:
        # Get all the enemy locations.
        aTrooper = world.get_location("Aqua Trooper")
        aTrooperCorrupt = world.get_location("Corrupted Aqua Trooper")
        beartle = world.get_location("Beartle")
        beartleCorrupt = world.get_location("Corrupted Beartle")
        bCone = world.get_location("Blast Cone")
        bCrawler = world.get_location("Bonecrawler")
        bSpitter = world.get_location("Bonespitter")
        bBeth = world.get_location("Boom Beth")
        bubblorbiter = world.get_location("Bubblorbiter")
        burro = world.get_location("Burro")
        coccoon = world.get_location("Cocoon")
        cHorn = world.get_location("Cow Horn")
        crowitzer = world.get_location("Crowitzer")
        crustaceon = world.get_location("Crustaceon")
        dHog = world.get_location("Dart Hog")
        dWalker = world.get_location("Dino Walker")
        dWalkerCorrupt = world.get_location("Corrupted Dino Walker")
        dFly = world.get_location("Drake Fly")
        dFlyCorrupt = world.get_location("Corrupted Drake Fly")
        dShip = world.get_location("Droplet Ship")
        durugin = world.get_location("Durugin")
        fHopper = world.get_location("Fire Hopper")
        flamingo = world.get_location("Flamingo")
        flamingoCorrupt = world.get_location("Corrupted Flamingo")
        fMouth = world.get_location("Flash Mouth")
        fMouthCorrupt = world.get_location("Corrupted Flash Mouth")
        fSaucer = world.get_location("Flying Saucer")
        fSnake = world.get_location("Folding Snake")
        gHog = world.get_location("Gat Hog")
        girder = world.get_location("Girder")
        hellpo = world.get_location("Hellpo")
        hPoliceCar = world.get_location("Hijacked Police Car")
        hPlate = world.get_location("Hot Plate")
        iris = world.get_location("Iris")
        jawdrop = world.get_location("Jawdrop")
        keon = world.get_location("Keon")
        kCannon = world.get_location("Koi Cannon")
        lCutter = world.get_location("Line Cutter")
        macer = world.get_location("Macer")
        manpowa = world.get_location("Manpowa")
        mantis = world.get_location("Mantis")
        mRoller = world.get_location("Meteor Roller")
        peller = world.get_location("Peller")
        pendurum = world.get_location("Pendurum")
        pendurumCorrupt = world.get_location("Corrupted Pendurum")
        pSnail = world.get_location("Pogo Snail")
        prawn = world.get_location("Prawn")
        pWild = world.get_location("Prawn To Be Wild")
        raytracker = world.get_location("Raytracker")
        raytrackerCorrupt = world.get_location("Corrupted Raytracker")
        rTrooper = world.get_location("Rifle Trooper")
        sShrimp = world.get_location("Saw Shrimp")
        sentinel = world.get_location("Sentinel")
        shockula = world.get_location("Shockula")
        softballer = world.get_location("Softballer")
        sTurretus = world.get_location("Spy Turretus")
        sTurretusCorrupt = world.get_location("Corrupted Spy Turretus")
        stahp = world.get_location("Stahp")
        sTrooper = world.get_location("Sword Trooper")
        sWing = world.get_location("Sword Wing")
        tTurretus = world.get_location("Tombstone Turretus")
        torcher = world.get_location("Torcher")
        tCannon = world.get_location("Tower Cannon")
        tDecoy = world.get_location("Toy Decoy")
        traumagotcha = world.get_location("Traumagotcha")
        traumagotchaCorrupt = world.get_location("Corrupted Traumagotcha")
        troopish = world.get_location("Troopish")
        turretus = world.get_location("Turretus")
        turretusCorrupt = world.get_location("Corrupted Turretus")
        waterHopper = world.get_location("Water Hopper")
        woodHopper = world.get_location("Wood Hopper")
        zTrooper = world.get_location("Zombie Trooper")
                
        # Set each enemy's access rules.
        set_rule(aTrooper, pCourtyard)
        add_rule(aTrooper, zJungle, "or")
        add_rule(aTrooper, cArboretum, "or")
        add_rule(aTrooper, lCannon, "or")
        
        set_rule(aTrooperCorrupt, nLake)
        
        set_rule(beartle, tFalls)
        add_rule(beartle, tGate, "or")
        add_rule(beartle, iDynamo, "or")
        
        set_rule(beartleCorrupt, iDynamo)
        
        set_rule(bCone, requiresBattlesphereChallenge(8))
        add_rule(bCone, gOpera1, "or")
        add_rule(bCone, aMuseum, "or")
        
        set_rule(bCrawler, requiresBattlesphereChallenge(17))
        add_rule(bCrawler, aForge, "or")
        add_rule(bCrawler, cArboretum, "or")
        
        set_rule(bSpitter, requiresBattlesphereChallenge(17))
        add_rule(bSpitter, aForge, "or")
        
        set_rule(bBeth, requiresBattlesphereChallenge(15))
        add_rule(bBeth, gOpera1, "or")
        add_rule(bBeth, gOpera2, "or")
        add_rule(bBeth, lTower, "or")
        
        set_rule(bubblorbiter, requiresBattlesphereChallenge(12))
        add_rule(bubblorbiter, pHighway, "or")
        add_rule(bubblorbiter, gBubble, "or")
        
        set_rule(burro, pHighway)
        add_rule(burro, mStarscape, "or")
        
        set_rule(coccoon, requiresBattlesphereChallenge(9))
        add_rule(coccoon, aMuseum, "or")
        add_rule(coccoon, gOpera1, "or")
        add_rule(coccoon, gOpera2, "or")
        add_rule(coccoon, gBubble, "or")
        add_rule(coccoon, cArboretum, "or")
        
        set_rule(cHorn, bChase)
        
        set_rule(crowitzer, requiresBattlesphereChallenge(18))
        add_rule(crowitzer, pHighway, "or")
        add_rule(crowitzer, gOpera1, "or")
        add_rule(crowitzer, cArboretum, "or")
        
        set_rule(crustaceon, tGate)
        add_rule(crustaceon, gBubble, "or")
        
        set_rule(dHog, lTower)
        add_rule(dHog, cArboretum, "or")
        
        set_rule(dWalker, zJungle)
        add_rule(dWalker, bRush, "or")
        
        set_rule(dWalkerCorrupt, nLake)
        
        set_rule(dFly, requiresBattlesphereChallenge(12))
        add_rule(dFly, requiresDragonValleyAccess, "or")
        add_rule(dFly, zJungle, "or")
        
        set_rule(dFlyCorrupt, nLake)
        
        set_rule(dShip, requiresBattlesphereChallenge(15))
        add_rule(dShip, pCourtyard, "or")
        add_rule(dShip, sBridge, "or")
        add_rule(dShip, lCannon, "or")
        
        set_rule(durugin, sBridge)
        add_rule(durugin, mStarscape, "or")
        add_rule(durugin, cArboretum, "or")
        
        set_rule(fHopper, zLand)
        add_rule(fHopper, gOpera2, "or")
        
        set_rule(flamingo, requiresBattlesphereChallenge(8))
        add_rule(flamingo, aMuseum, "or")
        add_rule(flamingo, zJungle, "or")
        
        set_rule(flamingoCorrupt, nLake)
        
        set_rule(fMouth, requiresBattlesphereChallenge(14))
        add_rule(fMouth, aSigwada, "or")
        add_rule(fMouth, gOpera2, "or")
        add_rule(fMouth, cArboretum, "or")
        
        set_rule(fMouthCorrupt, iDynamo)
        
        set_rule(fSaucer, requiresBattlesphereChallenge(7))
        add_rule(fSaucer, zLand, "or")
        add_rule(fSaucer, gOpera2, "or")
        add_rule(fSaucer, sBridge, "or")
        
        set_rule(fSnake, requiresBattlesphereChallenge(7))
        add_rule(fSnake, zLand, "or")
        add_rule(fSnake, gBubble, "or")
        
        set_rule(gHog, requiresBattlesphereChallenge(1))
        
        set_rule(girder, requiresBattlesphereChallenge(7))
        add_rule(girder, aSigwada, "or")
        add_rule(girder, gOpera1, "or")
        
        set_rule(hellpo, requiresBattlesphereChallenge(1))
        
        set_rule(hPoliceCar, pCourtyard)
        
        set_rule(hPlate, pCourtyard)
        add_rule(hPlate, mStarscape, "or")
        add_rule(hPlate, cArboretum, "or")
        
        set_rule(iris, requiresBattlesphereChallenge(18))
        add_rule(iris, aForge, "or")
        add_rule(iris, cArboretum, "or")
        
        set_rule(jawdrop, requiresBattlesphereChallenge(9))
        add_rule(jawdrop, requiresShenlinParkAccess, "or")
        add_rule(jawdrop, gOpera2, "or")
        add_rule(jawdrop, cArboretum, "or")
        
        set_rule(keon, requiresBattlesphereChallenge(8))
        add_rule(keon, requiresDragonValleyAccess, "or")
        add_rule(keon, cArboretum, "or")
        
        set_rule(kCannon, tFalls)
        add_rule(kCannon, gOpera1, "or")
        
        set_rule(lCutter, requiresBattlesphereChallenge(9))
        add_rule(lCutter, requiresDragonValleyAccess, "or")
        add_rule(lCutter, aForge, "or")
        
        set_rule(macer, requiresBattlesphereChallenge(8))
        add_rule(macer, aMuseum, "or")
        add_rule(macer, gOpera2, "or")
        
        set_rule(manpowa, tGate)
        add_rule(manpowa, gBubble, "or")
        add_rule(manpowa, lCannon, "or")
        
        set_rule(mantis, requiresBattlesphereChallenge(9))
        add_rule(mantis, aSigwada, "or")
        add_rule(mantis, gOpera2, "or")
        
        set_rule(mRoller, requiresBattlesphereChallenge(7))
        add_rule(mRoller, requiresShenlinParkAccess, "or")
        add_rule(mRoller, gOpera1, "or")
        
        set_rule(peller, requiresShenlinParkAccess)
        add_rule(peller, lTower, "or")
        
        set_rule(pendurum, requiresBattlesphereChallenge(8))
        add_rule(pendurum, requiresShenlinParkAccess, "or")
        add_rule(pendurum, gOpera2, "or")
        add_rule(pendurum, iDynamo, "or")
        
        set_rule(pendurumCorrupt, iDynamo)
        
        set_rule(pSnail, requiresBattlesphereChallenge(1))
        add_rule(pSnail, gOpera2, "or")
        
        set_rule(prawn, requiresBattlesphereChallenge(17))
        add_rule(prawn, aForge, "or")
        
        set_rule(pWild, bChase)
        
        set_rule(raytracker, gBubble)
        
        set_rule(raytrackerCorrupt, iDynamo)
        
        set_rule(rTrooper, requiresBattlesphereChallenge(13))
        add_rule(rTrooper, sArmory, "or")
        add_rule(rTrooper, zJungle, "or")
        add_rule(rTrooper, iDynamo, "or")
        
        set_rule(sShrimp, requiresBattlesphereChallenge(1))
        add_rule(sShrimp, tGate, "or")
        
        set_rule(sentinel, requiresBattlesphereChallenge(18))
        add_rule(sentinel, aForge, "or")
        add_rule(sentinel, bRush, "or")
        add_rule(sentinel, cArboretum, "or")
        
        set_rule(shockula, sBridge)
        add_rule(shockula, lCannon, "or")
        
        set_rule(softballer, zLand)
        add_rule(softballer, gOpera2, "or")
        
        set_rule(sTurretus, requiresBattlesphereChallenge(15))
        add_rule(sTurretus, requiresDragonValleyAccess, "or")
        add_rule(sTurretus, rGraveyard, "or")
        add_rule(sTurretus, sArmory, "or")
        add_rule(sTurretus, iDynamo, "or")
        
        set_rule(sTurretusCorrupt, iDynamo)
        
        set_rule(stahp, requiresBattlesphereChallenge(14))
        add_rule(stahp, pHighway, "or")
        add_rule(stahp, gOpera2, "or")
        add_rule(stahp, sBridge, "or")
        add_rule(stahp, bRush, "or")
        
        set_rule(sTrooper, requiresBattlesphereChallenge(13))
        add_rule(sTrooper, sArmory, "or")
        add_rule(sTrooper, zJungle, "or")
        add_rule(sTrooper, iDynamo, "or")
        
        set_rule(sWing, bChase)
        
        set_rule(tTurretus, requiresBattlesphereChallenge(13))
        add_rule(tTurretus, rGraveyard, "or")
        add_rule(tTurretus, iDynamo, "or")
        
        set_rule(torcher, aMuseum)
        add_rule(torcher, tGate, "or")
        
        set_rule(tCannon, requiresShenlinParkAccess)
        add_rule(tCannon, gBubble, "or")
        
        set_rule(tDecoy, requiresBattlesphereChallenge(11))
        add_rule(tDecoy, zLand, "or")
        
        set_rule(traumagotcha, requiresBattlesphereChallenge(8))
        add_rule(traumagotcha, requiresShenlinParkAccess, "or")
        add_rule(traumagotcha, zJungle, "or")
        add_rule(traumagotcha, bRush, "or")
        add_rule(traumagotcha, iDynamo, "or")
        
        set_rule(traumagotchaCorrupt, iDynamo)
        
        set_rule(troopish, sArmory)
        add_rule(troopish, zJungle, "or")
        
        set_rule(turretus, requiresBattlesphereChallenge(2))
        add_rule(turretus, requiresDragonValleyAccess, "or")
        add_rule(turretus, iDynamo, "or")
        
        set_rule(turretusCorrupt, iDynamo)
        
        set_rule(waterHopper, tGate)
        add_rule(waterHopper, gBubble, "or")
        
        set_rule(woodHopper, aMuseum)
        
        set_rule(zTrooper, requiresBattlesphereChallenge(13))
        add_rule(zTrooper, rGraveyard, "or")
        add_rule(zTrooper, sArmory, "or")
        add_rule(zTrooper, nLake, "or")
    
    # If boss sanity is enabled, then set the rules for them.
    if world.options.bosses:
        # Get all the boss locations.
        acrabelle = world.get_location("Acrabelle")
        askal = world.get_location("Askal")
        aGolmechAaa = world.get_location("Astral Golmech (Aaa)")
        aGolmechAskal = world.get_location("Astral Golmech (Askal)")
        beastOne = world.get_location("Beast One")
        beastTwo = world.get_location("Beast Two")
        beastThree = world.get_location("Beast Three")
        bff2000 = world.get_location("BFF2000")
        cKalaw = world.get_location("Captain Kalaw")
        carol = world.get_location("Carol")
        corazon = world.get_location("Corazon")
        crabulon = world.get_location("Crabulon")
        discord = world.get_location("Discord")
        dCocoon = world.get_location("Drake Cocoon")
        duality = world.get_location("Duality")
        gGong = world.get_location("General Gong")
        gLock = world.get_location("Gnawsa Lock")
        herald = world.get_location("Herald")
        hDrillion = world.get_location("Hundred Drillion")
        kakugan = world.get_location("Kakugan")
        lBread = world.get_location("Lemon Bread")
        lilac = world.get_location("Lilac")
        mergaBlueMoon = world.get_location("Merga (Blue Moon)")
        mergaBloodMoon = world.get_location("Merga (Blood Moon)")
        mergaSuperMoon = world.get_location("Merga (Super Moon)")
        mergaEclipse = world.get_location("Merga (Eclipse)")
        mergaLilith = world.get_location("Merga (Lilith)")
        mergaBase = world.get_location("Merga")
        milla = world.get_location("Milla")
        mCube = world.get_location("Monster Cube")
        neera = world.get_location("Neera")
        pPincer = world.get_location("Proto Pincer")
        rDriver = world.get_location("Rail Driver")
        rosebud = world.get_location("Rosebud")
        serpentine = world.get_location("Serpentine")
        sGrowth = world.get_location("Shell Growth")
        sSlider = world.get_location("Storm Slider")
        sSpider = world.get_location("Syntax Spider")
        tArmor = world.get_location("Titan Armor")
        tJoy = world.get_location("Trigger Joy")
        tLancer = world.get_location("Trigger Lancer")
        tDriver = world.get_location("Tunnel Driver")
        wFace = world.get_location("Weather Face")
        wArmor = world.get_location("Wolf Armor")  
        
        # Set each boss's access rules.
        set_rule(acrabelle, requiresBattlesphereChallenge(11))
        
        set_rule(askal, dPoint)
        
        set_rule(aGolmechAaa, rRoom)
        
        set_rule(aGolmechAskal, rRoom)
        
        set_rule(beastOne, gOpera1)
        
        set_rule(beastTwo, gOpera2)
        
        set_rule(beastThree, auditorium)
        
        set_rule(bff2000, auditorium)
        
        set_rule(cKalaw, sBridge)
        
        set_rule(carol, requiresBattlesphereChallenge(3))
        add_rule(carol, pCourtyard, "or")
        
        set_rule(corazon, aSigwada)
        add_rule(corazon, cArboretum, "or")
        
        set_rule(crabulon, bChase)
        
        set_rule(discord, pHighway)
        add_rule(discord, bRush, "or")
        
        set_rule(dCocoon, requiresBattlesphereChallenge(9))
        add_rule(dCocoon, aMuseum, "or")
        add_rule(dCocoon, lTower, "or")
        
        set_rule(duality, pCourtyard)
        add_rule(duality, cArboretum, "or")
        
        set_rule(gGong, pCourtyard)
        
        set_rule(gLock, aForge)
        
        set_rule(herald, requiresBattlesphereChallenge(15))
        add_rule(herald, zLand, "or")
        add_rule(herald, bRush, "or")
        
        set_rule(hDrillion, mStarscape)
        
        set_rule(kakugan, requiresBattlesphereChallenge(15))
        add_rule(kakugan, aMuseum, "or")
        
        set_rule(lBread, requiresBattlesphereChallenge(17))
        
        set_rule(lilac, requiresBattlesphereChallenge(3))
        add_rule(lilac, pCourtyard, "or")
        
        set_rule(mergaBlueMoon, merga)
        
        set_rule(mergaBloodMoon, merga)
        
        set_rule(mergaSuperMoon, merga)
        
        set_rule(mergaEclipse, merga)
        
        set_rule(mergaLilith, merga)
        
        set_rule(mergaBase, merga)
        add_rule(mergaBase, pCourtyard, "or")
        
        set_rule(milla, requiresBattlesphereChallenge(3))
        add_rule(milla, pCourtyard, "or")
        
        set_rule(mCube, requiresBattlesphereChallenge(13))
        add_rule(mCube, rGraveyard, "or")
        add_rule(mCube, zJungle, "or")
        add_rule(mCube, nLake, "or")
        
        set_rule(neera, requiresBattlesphereChallenge(3))
        add_rule(neera, pCourtyard, "or")
        
        set_rule(pPincer, requiresDragonValleyAccess)
        add_rule(pPincer, bRush, "or")
        
        set_rule(rDriver, bRush)
        
        set_rule(rosebud, requiresBattlesphereChallenge(15))
        add_rule(rosebud, tFalls, "or")
        add_rule(rosebud, gBubble, "or")
        add_rule(rosebud, cArboretum, "or")
        
        set_rule(serpentine, snowfields)
        
        set_rule(sGrowth, tGate)
        add_rule(sGrowth, iDynamo, "or")
        
        set_rule(sSlider, lTower)
        
        set_rule(sSpider, requiresBattlesphereChallenge(13))
        add_rule(sSpider, sArmory, "or")
        
        set_rule(tArmor, nLake)
        add_rule(tArmor, iDynamo, "or")
        
        set_rule(tJoy, requiresBattlesphereChallenge(10))
        add_rule(tJoy, requiresShenlinParkAccess, "or")
        
        set_rule(tLancer, requiresBattlesphereChallenge(10))
        add_rule(tLancer, aSigwada, "or")
        
        set_rule(tDriver, zJungle)
        
        set_rule(wFace, requiresBattlesphereChallenge(17))
        add_rule(wFace, sBridge, "or")
        add_rule(wFace, cArboretum, "or")
        
        set_rule(wArmor, snowfields)
        
def set_completion_condition(world: FP2World) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Cordelia's Final Entry", world.player)