from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule
if TYPE_CHECKING:
    from .world import NNTWorld


def set_all_rules(world: NNTWorld) -> None:
    set_rupturefarms_entrance_rules(world)
    set_stockyards_entrance_rules(world)
    set_paramonia_entrance_rules(world)
    set_scrabania_entrance_rules(world)
    set_zulag1_entrance_rules(world)
    set_zulag2_entrance_rules(world)
    set_zulag3_entrance_rules(world)
    set_zulag4_entrance_rules(world)
    set_completion_condition(world)

def set_rupturefarms_entrance_rules(world: NNTWorld) -> None:
    rFarmAccess = world.get_entrance("Menu to Rupture Farms")
    rFarmS1Requirements = world.get_entrance("Rupture Farms Secret Area 1 Access")
    rFarmS2Requirements = world.get_entrance("Rupture Farms Secret Area 2 Access")
    rFarmS3Requirements = world.get_entrance("Rupture Farms Secret Area 3 Access")
    rFarmS4Requirements = world.get_entrance("Rupture Farms Secret Area 4 Access")
    rFarmsInteractablesRequirements = world.get_entrance("Rupture Farms Interactables Tutorial")
    rFarmS5Requirements = world.get_entrance("Rupture Farms Secret Area 5 Access")
    rFarmsUXBRequirements = world.get_entrance("Rupture Farms UXB Tutorial")
    rFarmS6Requirements = world.get_entrance("Rupture Farms Secret Area 6 Access")

    set_rule(rFarmAccess, lambda state: state.has("Rupture Farms", world.player))
    add_rule(rFarmAccess, lambda state: state.has("Levers", world.player))
    set_rule(rFarmS1Requirements, lambda state: state.has("Possession", world.player))
    set_rule(rFarmS2Requirements, lambda state: state.has("Grenades", world.player))
    set_rule(rFarmS3Requirements, lambda state: state.has("Grenades", world.player))
    set_rule(rFarmS4Requirements, lambda state: state.has("Grenades", world.player))
    set_rule(rFarmsInteractablesRequirements, lambda state: state.has("Lifts", world.player))
    set_rule(rFarmS5Requirements, lambda state: state.has("Grenades", world.player))
    set_rule(rFarmsUXBRequirements, lambda state: state.has("UXB Defusion", world.player))
    add_rule(rFarmS5Requirements, lambda state: state.has("Possession", world.player))
    set_rule(rFarmS6Requirements, lambda state: state.has("Possession", world.player))

def set_stockyards_entrance_rules(world: NNTWorld) -> None:
    stockyardsAccess = world.get_entrance("Menu to Stockyards")
    stockyardsS1Requirements = world.get_entrance("Stockyards Secret Area Access")
    ffZoneS1Requirements = world.get_entrance("Free Fire Zone Secret Area 1 Access")
    ffZoneS2Requirements = world.get_entrance("Free Fire Zone Secret Area 2 Access")
    ffZoneRockRequirements = world.get_entrance("Free Fire Zone Rock Tutorial")
    ffZoneS4Requirements = world.get_entrance("Free Fire Zone Secret Area 4 Access")
    ffZoneS6Requirements = world.get_entrance("Free Fire Zone Secret Area 6 Access")
    
    set_rule(stockyardsAccess, lambda state: state.has("Stockyards", world.player))
    set_rule(stockyardsS1Requirements, lambda state: state.has("Levers", world.player))
    set_rule(ffZoneS1Requirements, lambda state: state.has("Levers", world.player))
    add_rule(ffZoneS1Requirements, lambda state: state.has("Possession", world.player))
    set_rule(ffZoneS2Requirements, lambda state: state.has("Possession", world.player))
    set_rule(ffZoneRockRequirements, lambda state: state.has("Rocks", world.player))
    set_rule(ffZoneS4Requirements, lambda state: state.has("Possession", world.player))
    add_rule(world.get_location("Free Fire Zone ~ Secret Area 5 - Mudokon 2"), lambda state: state.has("Levers", world.player))
    add_rule(world.get_location("Free Fire Zone ~ Secret Area 5 - Mudokon 3"), lambda state: state.has("Levers", world.player))
    set_rule(ffZoneS6Requirements, lambda state: state.has("Levers", world.player))
    
def set_paramonia_entrance_rules(world: NNTWorld) -> None:
    paramoniaAccess = world.get_entrance("Menu to Paramonia")
    paramoniaTempleHubRequirements = world.get_entrance("Paramonia to Temple HUB")
    paramoniaTrial1Requirements = world.get_entrance("Paramonia Temple HUB to Trial 1")
    paramoniaTrial2Requirements = world.get_entrance("Paramonia Temple HUB to Trial 2")
    paramoniaTrial5Requirements = world.get_entrance("Paramonia Temple HUB to Trial 5")
    paramoniaNestRequirements = world.get_entrance("Paramonia Temple HUB to Nests")
    
    set_rule(paramoniaAccess, lambda state: state.has("Paramonia", world.player))
    set_rule(paramoniaTempleHubRequirements, lambda state: state.has("Possession", world.player))
    add_rule(paramoniaTempleHubRequirements, lambda state: state.has("Lifts", world.player))
    add_rule(paramoniaTempleHubRequirements, lambda state: state.has("Levers", world.player))
    set_rule(paramoniaTrial1Requirements, lambda state: state.has("Meat", world.player))
    add_rule(paramoniaTrial1Requirements, lambda state: state.has("Spirit Rings", world.player))
    set_rule(paramoniaTrial2Requirements, lambda state: state.has("Rocks", world.player))
    set_rule(paramoniaTrial5Requirements, lambda state: state.has("Meat", world.player))
    set_rule(paramoniaNestRequirements, lambda state: state.has("Meat", world.player))
    add_rule(paramoniaNestRequirements, lambda state: state.has("Spirit Rings", world.player))
    add_rule(paramoniaNestRequirements, lambda state: state.has("Rocks", world.player))
    
def set_scrabania_entrance_rules(world: NNTWorld) -> None:
    scrabaniaAccess = world.get_entrance("Menu to Scrabania")
    scrabaniaStartSecretRequirements = world.get_entrance("Scrabania to Temple Entrance Secret")
    scrabaniaTempleHubRequirements = world.get_entrance("Scrabania to Temple HUB")
    scrabaniaTrial1Requirements = world.get_entrance("Scrabania Temple HUB to Trial 1")
    scrabaniaTrial4Requirements = world.get_entrance("Scrabania Temple HUB to Trial 4")
    scrabaniaTrial6Requirements = world.get_entrance("Scrabania Temple HUB to Trial 6")
    scrabaniaTrial8Requirements = world.get_entrance("Scrabania Temple HUB to Trial 8")
    scrabaniaNestRequirements = world.get_entrance("Scrabania Temple HUB to Nests")
    
    set_rule(scrabaniaAccess, lambda state: state.has("Scrabania", world.player))
    set_rule(scrabaniaStartSecretRequirements, lambda state: state.has("Possession", world.player))
    add_rule(scrabaniaStartSecretRequirements, lambda state: state.has("UXB Defusion", world.player))
    set_rule(scrabaniaTempleHubRequirements, lambda state: state.has("Levers", world.player))
    add_rule(scrabaniaTempleHubRequirements, lambda state: state.has("Possession", world.player))
    set_rule(scrabaniaTrial1Requirements, lambda state: state.has("Rocks", world.player))
    set_rule(scrabaniaTrial4Requirements, lambda state: state.has("Lifts", world.player))
    set_rule(scrabaniaTrial6Requirements, lambda state: state.has("Lifts", world.player))
    set_rule(scrabaniaTrial8Requirements, lambda state: state.has("Lifts", world.player))
    set_rule(scrabaniaNestRequirements, lambda state: state.has("Lifts", world.player))
    add_rule(scrabaniaNestRequirements, lambda state: state.has("Rocks", world.player))

def set_zulag1_entrance_rules(world: NNTWorld) -> None:
    zulag1Access = world.get_entrance("Menu to Zulag 1")
    zulag1CargoRequirements = world.get_entrance("Zulag 1 Cargo Lift")
    zulag1ShadowRequirements = world.get_entrance("Zulag 1 Shadow Tutorial")
    zulag1SligLockRequirements = world.get_entrance("Zulag 1 Slig Voice Lock")
    zulag1ShrykullRequirements = world.get_entrance("Zulag 1 Shrykull Portal Tutorial")
    zulag1Z2AccessRequirements = world.get_entrance("Zulag 1 Zulag 2 Access")
    
    set_rule(zulag1Access, lambda state: state.has("Zulag 1", world.player))
    set_rule(zulag1CargoRequirements, lambda state: state.has("Lifts", world.player))
    add_rule(zulag1CargoRequirements, lambda state: state.has("Shrykull", world.player))
    set_rule(zulag1ShadowRequirements, lambda state: state.has("Levers", world.player))
    add_rule(zulag1ShadowRequirements, lambda state: state.has_any(("Grenades", "Spirit Rings"), world.player))
    set_rule(zulag1SligLockRequirements, lambda state: state.has("Possession", world.player))
    set_rule(zulag1ShrykullRequirements, lambda state: state.has("Levers", world.player))
    add_rule(zulag1ShrykullRequirements, lambda state: state.has("Spirit Rings", world.player)) #Possession might be enough?
    set_rule(zulag1Z2AccessRequirements, lambda state: state.has("Possession", world.player))
    add_rule(zulag1Z2AccessRequirements, lambda state: state.has("Levers", world.player))
    
def set_zulag2_entrance_rules(world: NNTWorld) -> None:
    zulag2Access = world.get_entrance("Menu to Zulag 2")
    zulag2Door1Back = world.get_entrance("Zulag 2 Door 1 Back Area")
    zulag2Door2 = world.get_entrance("Zulag 2 Door 2 Path")
    zulag2Door3 = world.get_entrance("Zulag 2 Door 3 Path")
    
    set_rule(zulag2Access, lambda state: state.has("Zulag 2", world.player))
    add_rule(zulag2Access, lambda state: state.has("Possession", world.player))
    add_rule(zulag2Access, lambda state: state.has("Lifts", world.player))
    add_rule(world.get_location("Zulag 2 ~ Door 1 - Mudokon 2"), lambda state: state.has("Levers", world.player))
    add_rule(world.get_location("Zulag 2 ~ Door 1 - Mudokon 7"), lambda state: state.has("Levers", world.player))
    add_rule(world.get_location("Zulag 2 ~ Door 1 - Mudokon 6"), lambda state: state.has("Levers", world.player))
    add_rule(world.get_location("Zulag 2 ~ Door 1 - Mudokon 5"), lambda state: state.has("Levers", world.player))
    add_rule(world.get_location("Zulag 2 ~ Door 1 - Mudokon 1"), lambda state: state.has("Levers", world.player))
    add_rule(world.get_location("Zulag 2 ~ Door 1 - Mudokon 4"), lambda state: state.has("Levers", world.player))
    add_rule(world.get_location("Zulag 2 Door 1"), lambda state: state.has("Levers", world.player))
    set_rule(zulag2Door1Back, lambda state: state.has("Shrykull", world.player))
    set_rule(zulag2Door2, lambda state: state.has("Levers", world.player))
    add_rule(zulag2Door2, lambda state: state.has("Grenades", world.player))
    set_rule(zulag2Door3, lambda state: state.has("Levers", world.player))
    add_rule(zulag2Door3, lambda state: state.has("Grenades", world.player))
    
def set_zulag3_entrance_rules(world: NNTWorld) -> None:
    zulag3Access = world.get_entrance("Menu to Zulag 3")
    zulag3Door1 = world.get_entrance("Zulag 3 Door 1 Path")
    zulag3Door1Back = world.get_entrance("Zulag 3 Door 1 Back Area")
    zulag3Door2 = world.get_entrance("Zulag 3 Door 2 Path")
    zulag3Door3Back = world.get_entrance("Zulag 3 Door 3 Back Area")
    
    set_rule(zulag3Access, lambda state: state.has("Zulag 3", world.player))
    add_rule(zulag3Access, lambda state: state.has("Possession", world.player))
    add_rule(zulag3Access, lambda state: state.has("Lifts", world.player))
    add_rule(zulag3Access, lambda state: state.has("Levers", world.player))
    set_rule(zulag3Door1, lambda state: state.has("Grenades", world.player))
    set_rule(zulag3Door1Back, lambda state: state.has("Shrykull", world.player))
    set_rule(zulag3Door2, lambda state: state.has("Grenades", world.player))
    set_rule(zulag3Door3Back, lambda state: state.has("Grenades", world.player))
    
def set_zulag4_entrance_rules(world: NNTWorld) -> None:
    zulag4Access = world.get_entrance("Menu to Zulag 4")
    zulag4S1Access = world.get_entrance("Zulag 4 Secret Area 1 Access")
    zulag4SligPath = world.get_entrance("Zulag 4 Slig Path")
    zulag4SligPathG = world.get_entrance("Zulag 4 Slig Path Post Grenades")
    
    set_rule(zulag4Access, lambda state: state.has("Zulag 4", world.player))
    set_rule(zulag4S1Access, lambda state: state.has_any(("Levers", "Possession"), world.player))
    set_rule(zulag4SligPath, lambda state: state.has("Possession", world.player))
    add_rule(zulag4SligPath, lambda state: state.has("Lifts", world.player))
    add_rule(zulag4SligPath, lambda state: state.has("Levers", world.player))
    set_rule(zulag4SligPathG, lambda state: state.has("Grenades", world.player))
    
    # Checks if the player has enough rescued Mudokons and the abilities needed to complete The Boardroom.
    # TODO: Make a version of this for Alf's Escape when we implement that.
    def GoModeCheck(state: CollectionState) -> bool:
        if state.has("Rescued Mudokon", world.player, world.required_muds) == False: return False
        if state.has("Levers", world.player) == False: return False
        if state.has("Lifts", world.player) == False: return False
        if state.has("UXB Defusion", world.player) == False: return False
        if state.has("Shrykull", world.player) == False: return False
        return True
    
    boardroomAccess = world.get_entrance("Menu to Boardroom")
    set_rule(boardroomAccess, GoModeCheck)
        
def set_completion_condition(world: NNTWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
