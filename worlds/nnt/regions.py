from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Region
if TYPE_CHECKING:
    from .world import NNTWorld

def create_and_connect_regions(world: NNTWorld) -> None:
    # Create the menu regions.
    menu = Region("Menu", world.player, world.multiworld)
    regions = [menu]
    world.multiworld.regions += regions
    
    # Create the area regions.
    create_rupturefarms_regions(world)
    create_stockyards_regions(world)
    create_paramonia_regions(world)
    create_scrabania_regions(world)
    create_zulag1_regions(world)
    create_zulag2_regions(world)
    create_zulag3_regions(world)
    create_zulag4_regions(world)
    
    # Connect the area regions.
    connect_rupturefarms_regions(world)
    connect_stockyards_regions(world)
    connect_paramonia_regions(world)
    connect_scrabania_regions(world)
    connect_zulag1_regions(world)
    connect_zulag2_regions(world)
    connect_zulag3_regions(world)
    connect_zulag4_regions(world)

def create_rupturefarms_regions(world: NNTWorld) -> None:
    rFarms = Region("Rupture Farms", world.player, world.multiworld)
    rFarmsS1 = Region("Rupture Farms (Secret Area 1)", world.player, world.multiworld)
    rFarmsS2 = Region("Rupture Farms (Secret Area 2)", world.player, world.multiworld)
    rFarmsS3 = Region("Rupture Farms (Secret Area 3)", world.player, world.multiworld)
    rFarmsS4 = Region("Rupture Farms (Secret Area 4)", world.player, world.multiworld)
    rFarmsInteractables = Region("Rupture Farms (Interactables Tutorial)", world.player, world.multiworld)
    rFarmsGameSpeak = Region("Rupture Farms (GameSpeak Tutorial)", world.player, world.multiworld)
    rFarmsS5 = Region("Rupture Farms (Secret Area 5)", world.player, world.multiworld)
    rFarmsBottlecap = Region("Rupture Farms (Bottlecap Tutorial)", world.player, world.multiworld)
    rFarmsShadow = Region("Rupture Farms (Shadow Tutorial)", world.player, world.multiworld)
    rFarmsUXB = Region("Rupture Farms (UXB Tutorial)", world.player, world.multiworld)
    rFarmsGrinder = Region("Rupture Farms (Grinder Tutorial)", world.player, world.multiworld)
    rFarmsZ2Access = Region("Rupture Farms (Zulag 2 Access)", world.player, world.multiworld)
    rFarmsS6 = Region("Rupture Farms (Secret Area 6)", world.player, world.multiworld)

    regions = [rFarms, rFarmsS1, rFarmsS2, rFarmsS3, rFarmsS4, rFarmsInteractables, rFarmsGameSpeak, rFarmsS5, rFarmsBottlecap, rFarmsShadow, rFarmsUXB, rFarmsGrinder, rFarmsZ2Access, rFarmsS6]

    world.multiworld.regions += regions

def create_stockyards_regions(world: NNTWorld) -> None:
    stockyards = Region("Stockyards", world.player, world.multiworld)
    stockyardsSecret = Region("Stockyards (Secret Area)", world.player, world.multiworld)
    ffZone = Region("Free Fire Zone", world.player, world.multiworld)
    ffZoneS1 = Region("Free Fire Zone (Secret Area 1)", world.player, world.multiworld)
    ffZoneS2 = Region("Free Fire Zone (Secret Area 2)", world.player, world.multiworld)
    ffZoneS3 = Region("Free Fire Zone (Secret Area 3)", world.player, world.multiworld)
    ffZoneRocks = Region("Free Fire Zone (Rock Tutorial)", world.player, world.multiworld)
    ffZoneS4 = Region("Free Fire Zone (Secret Area 4)", world.player, world.multiworld)
    ffZoneS5 = Region("Free Fire Zone (Secret Area 5)", world.player, world.multiworld)
    ffZoneS6 = Region("Free Fire Zone (Secret Area 6)", world.player, world.multiworld)

    regions = [stockyards, stockyardsSecret, ffZone, ffZoneS1, ffZoneS2, ffZoneS3, ffZoneRocks, ffZoneS4, ffZoneS5, ffZoneS6]

    world.multiworld.regions += regions
    
def create_paramonia_regions(world: NNTWorld) -> None:
    paramonia = Region("Paramonia", world.player, world.multiworld)
    paramoniaTempleHub = Region("Paramonian Temple HUB", world.player, world.multiworld)
    paramoniaTrial1 = Region("Paramonian Temple Trial 1", world.player, world.multiworld)
    paramoniaTrial2 = Region("Paramonian Temple Trial 2", world.player, world.multiworld)
    paramoniaTrial3 = Region("Paramonian Temple Trial 3", world.player, world.multiworld)
    paramoniaTrial4 = Region("Paramonian Temple Trial 4", world.player, world.multiworld)
    paramoniaTrial5 = Region("Paramonian Temple Trial 5", world.player, world.multiworld)
    paramoniaTrial5Secret = Region("Paramonian Temple Trial 5 (Secret Area)", world.player, world.multiworld)
    paramoniaTrial6 = Region("Paramonian Temple Trial 6", world.player, world.multiworld)
    paramoniaNest = Region("Paramonian Nests", world.player, world.multiworld)

    regions = [paramonia, paramoniaTempleHub, paramoniaTrial1, paramoniaTrial2, paramoniaTrial3, paramoniaTrial4, paramoniaTrial5, paramoniaTrial5Secret, paramoniaTrial6, paramoniaNest]

    world.multiworld.regions += regions
    
def create_scrabania_regions(world: NNTWorld) -> None:
    scrabania = Region("Scrabania", world.player, world.multiworld)
    scrabaniaStartSecret = Region("Scrabanian Temple Entrance (Secret Area)", world.player, world.multiworld)
    scrabaniaTempleHub = Region("Scrabanian Temple HUB", world.player, world.multiworld)
    scrabaniaTrial1 = Region("Scrabanian Temple Trial 1", world.player, world.multiworld)
    scrabaniaTrial2 = Region("Scrabanian Temple Trial 2", world.player, world.multiworld)
    scrabaniaTrial3 = Region("Scrabanian Temple Trial 3", world.player, world.multiworld)
    scrabaniaTrial4 = Region("Scrabanian Temple Trial 4", world.player, world.multiworld)
    scrabaniaTrial5 = Region("Scrabanian Temple Trial 5", world.player, world.multiworld)
    scrabaniaTrial6 = Region("Scrabanian Temple Trial 6", world.player, world.multiworld)
    scrabaniaTrial7 = Region("Scrabanian Temple Trial 7", world.player, world.multiworld)
    scrabaniaTrial7Secret = Region("Scrabanian Temple Trial 7 (Secret Area)", world.player, world.multiworld)
    scrabaniaTrial8 = Region("Scrabanian Temple Trial 8", world.player, world.multiworld)
    scrabaniaTrial8Secret = Region("Scrabanian Temple Trial 8 (Secret Area)", world.player, world.multiworld)
    scrabaniaNest = Region("Scrabanian Nests", world.player, world.multiworld)

    regions = [scrabania, scrabaniaStartSecret, scrabaniaTempleHub, scrabaniaTrial1, scrabaniaTrial2, scrabaniaTrial3, scrabaniaTrial4, scrabaniaTrial5, scrabaniaTrial6, scrabaniaTrial7, scrabaniaTrial7Secret, scrabaniaTrial8, scrabaniaTrial8Secret, scrabaniaNest]

    world.multiworld.regions += regions
    
def create_zulag1_regions(world: NNTWorld) -> None:
    zulag1 = Region("Zulag 1", world.player, world.multiworld)
    zulag1Cargo = Region("Zulag 1 (Cargo Lift)", world.player, world.multiworld)
    zulag1Grinder = Region("Zulag 1 (Grinder Tutorial)", world.player, world.multiworld)
    zulag1Shadow = Region("Zulag 1 (Shadow Tutorial)", world.player, world.multiworld)
    zulag1SligLock = Region("Zulag 1 (Slig Voice Lock)", world.player, world.multiworld)
    zulag1Shrykull = Region("Zulag 1 (Shrykull Portal Tutorial)", world.player, world.multiworld)
    zulag1S1 = Region("Zulag 1 (Secret Area 1)", world.player, world.multiworld)
    zulag1GameSpeak = Region("Zulag 1 (GameSpeak Tutorial)", world.player, world.multiworld)
    zulag1Interactables = Region("Zulag 1 (Interactables Tutorial)", world.player, world.multiworld)
    zulag1S2 = Region("Zulag 1 (Secret Area 2)", world.player, world.multiworld)
    zulag1S3 = Region("Zulag 1 (Secret Area 3)", world.player, world.multiworld)
    zulag1S4 = Region("Zulag 1 (Secret Area 4)", world.player, world.multiworld)
    zulag1Backtrack = Region("Zulag 1 (Backtrack End)", world.player, world.multiworld)
    zulag1S5 = Region("Zulag 1 (Secret Area 5)", world.player, world.multiworld)
    zulag1Z2Access = Region("Zulag 1 (Zulag 2 Access)", world.player, world.multiworld)

    regions = [zulag1, zulag1Cargo, zulag1Grinder, zulag1Shadow, zulag1SligLock, zulag1Shrykull, zulag1S1, zulag1GameSpeak, zulag1Interactables, zulag1S2, zulag1S3, zulag1S4, zulag1Backtrack, zulag1S5, zulag1Z2Access]

    world.multiworld.regions += regions
    
def create_zulag2_regions(world: NNTWorld) -> None:
    zulag2 = Region("Zulag 2", world.player, world.multiworld)
    zulag2Door1 = Region("Zulag 2 (Door 1)", world.player, world.multiworld)
    zulag2Door1Back = Region("Zulag 2 (Door 1 Back Area)", world.player, world.multiworld)
    zulag2Door2 = Region("Zulag 2 (Door 2)", world.player, world.multiworld)
    zulag2Door3 = Region("Zulag 2 (Door 3)", world.player, world.multiworld)

    regions = [zulag2, zulag2Door1, zulag2Door1Back, zulag2Door2, zulag2Door3]

    world.multiworld.regions += regions
    
def create_zulag3_regions(world: NNTWorld) -> None:
    zulag3 = Region("Zulag 3", world.player, world.multiworld)
    zulag3Door1 = Region("Zulag 3 (Door 1)", world.player, world.multiworld)
    zulag3Door1Back = Region("Zulag 3 (Door 1 Back Area)", world.player, world.multiworld)
    zulag3Door2 = Region("Zulag 3 (Door 2)", world.player, world.multiworld)
    zulag3Door3 = Region("Zulag 3 (Door 3)", world.player, world.multiworld)
    zulag3Door3Back = Region("Zulag 3 (Door 3 Back Area)", world.player, world.multiworld)

    regions = [zulag3, zulag3Door1, zulag3Door1Back, zulag3Door2, zulag3Door3, zulag3Door3Back]

    world.multiworld.regions += regions
    
def create_zulag4_regions(world: NNTWorld) -> None:
    zulag4 = Region("Zulag 4", world.player, world.multiworld)
    zulag4S1 = Region("Zulag 4 (Secret Area 1)", world.player, world.multiworld)
    zulag4SligPath = Region("Zulag 4 (Slig Path)", world.player, world.multiworld)
    zulag4SligPathG = Region("Zulag 4 (Slig Path Post Grenades)", world.player, world.multiworld)
    zulag4S2 = Region("Zulag 4 (Secret Area 2)", world.player, world.multiworld)
    boardroom = Region("Boardroom", world.player, world.multiworld)

    regions = [zulag4, zulag4S1, zulag4SligPath, zulag4SligPathG, zulag4S2, boardroom]

    world.multiworld.regions += regions

def connect_rupturefarms_regions(world: NNTWorld) -> None:
    menu = world.get_region("Menu")
    rFarms = world.get_region("Rupture Farms")
    rFarmsS1 = world.get_region("Rupture Farms (Secret Area 1)")
    rFarmsS2 = world.get_region("Rupture Farms (Secret Area 2)")
    rFarmsS3 = world.get_region("Rupture Farms (Secret Area 3)")
    rFarmsS4 = world.get_region("Rupture Farms (Secret Area 4)")
    rFarmsInteractables = world.get_region("Rupture Farms (Interactables Tutorial)")
    rFarmsGameSpeak = world.get_region("Rupture Farms (GameSpeak Tutorial)")
    rFarmsS5 = world.get_region("Rupture Farms (Secret Area 5)")
    rFarmsBottlecap = world.get_region("Rupture Farms (Bottlecap Tutorial)")
    rFarmsShadow = world.get_region("Rupture Farms (Shadow Tutorial)")
    rFarmsUXB = world.get_region("Rupture Farms (UXB Tutorial)")
    rFarmsGrinder = world.get_region("Rupture Farms (Grinder Tutorial)")
    rFarmsZ2Access = world.get_region("Rupture Farms (Zulag 2 Access)")
    rFarmsS6 = world.get_region("Rupture Farms (Secret Area 6)")
    
    menu.connect(rFarms, "Menu to Rupture Farms")
    rFarms.connect(rFarmsS1, "Rupture Farms Secret Area 1 Access")
    rFarms.connect(rFarmsS2, "Rupture Farms Secret Area 2 Access")
    rFarms.connect(rFarmsS3, "Rupture Farms Secret Area 3 Access")
    rFarms.connect(rFarmsS4, "Rupture Farms Secret Area 4 Access")
    rFarms.connect(rFarmsInteractables, "Rupture Farms Interactables Tutorial")
    rFarmsInteractables.connect(rFarmsGameSpeak, "Rupture Farms GameSpeak Tutorial")
    rFarmsGameSpeak.connect(rFarmsS5, "Rupture Farms Secret Area 5 Access")
    rFarmsGameSpeak.connect(rFarmsBottlecap, "Rupture Farms Bottlecap Tutorial")
    rFarmsBottlecap.connect(rFarmsShadow, "Rupture Farms Shadow Tutorial")
    rFarmsShadow.connect(rFarmsUXB, "Rupture Farms UXB Tutorial")
    rFarmsShadow.connect(rFarmsGrinder, "Rupture Farms Grinder Tutorial")
    rFarmsGrinder.connect(rFarmsZ2Access, "Zulag 2 Access")
    rFarmsGrinder.connect(rFarmsS6, "Rupture Farms Secret Area 6 Access")

def connect_stockyards_regions(world: NNTWorld) -> None:
    menu = world.get_region("Menu")
    stockyards = world.get_region("Stockyards")
    stockyardsSecret = world.get_region("Stockyards (Secret Area)")
    ffZone = world.get_region("Free Fire Zone")
    ffZoneS1 = world.get_region("Free Fire Zone (Secret Area 1)")
    ffZoneS2 = world.get_region("Free Fire Zone (Secret Area 2)")
    ffZoneS3 = world.get_region("Free Fire Zone (Secret Area 3)")
    ffZoneRocks = world.get_region("Free Fire Zone (Rock Tutorial)")
    ffZoneS4 = world.get_region("Free Fire Zone (Secret Area 4)")
    ffZoneS5 = world.get_region("Free Fire Zone (Secret Area 5)")
    ffZoneS6 = world.get_region("Free Fire Zone (Secret Area 6)")
    
    menu.connect(stockyards, "Menu to Stockyards")
    stockyards.connect(stockyardsSecret, "Stockyards Secret Area Access")
    stockyards.connect(ffZone, "Free Fire Zone Access")
    ffZone.connect(ffZoneS1, "Free Fire Zone Secret Area 1 Access")
    ffZone.connect(ffZoneS2, "Free Fire Zone Secret Area 2 Access")
    ffZone.connect(ffZoneS3, "Free Fire Zone Secret Area 3 Access")
    ffZone.connect(ffZoneRocks, "Free Fire Zone Rock Tutorial")
    ffZoneRocks.connect(ffZoneS4, "Free Fire Zone Secret Area 4 Access")
    ffZoneRocks.connect(ffZoneS5, "Free Fire Zone Secret Area 5 Access")
    ffZoneRocks.connect(ffZoneS6, "Free Fire Zone Secret Area 6 Access")
    
def connect_paramonia_regions(world: NNTWorld) -> None:
    menu = world.get_region("Menu")
    paramonia = world.get_region("Paramonia")
    paramoniaTempleHub = world.get_region("Paramonian Temple HUB")
    paramoniaTrial1 = world.get_region("Paramonian Temple Trial 1")
    paramoniaTrial2 = world.get_region("Paramonian Temple Trial 2")
    paramoniaTrial3 = world.get_region("Paramonian Temple Trial 3")
    paramoniaTrial4 = world.get_region("Paramonian Temple Trial 4")
    paramoniaTrial5 = world.get_region("Paramonian Temple Trial 5")
    paramoniaTrial5Secret = world.get_region("Paramonian Temple Trial 5 (Secret Area)")
    paramoniaTrial6 = world.get_region("Paramonian Temple Trial 6")
    paramoniaNest = world.get_region("Paramonian Nests")
    
    menu.connect(paramonia, "Menu to Paramonia")
    paramonia.connect(paramoniaTempleHub, "Paramonia to Temple HUB")
    paramoniaTempleHub.connect(paramoniaTrial1, "Paramonia Temple HUB to Trial 1")
    paramoniaTempleHub.connect(paramoniaTrial2, "Paramonia Temple HUB to Trial 2")
    paramoniaTempleHub.connect(paramoniaTrial3, "Paramonia Temple HUB to Trial 3")
    paramoniaTempleHub.connect(paramoniaTrial4, "Paramonia Temple HUB to Trial 4")
    paramoniaTempleHub.connect(paramoniaTrial5, "Paramonia Temple HUB to Trial 5")
    paramoniaTrial5.connect(paramoniaTrial5Secret, "Paramonia Trial 5 Secret Area Access")
    paramoniaTempleHub.connect(paramoniaTrial6, "Paramonia Temple HUB to Trial 6")
    paramoniaTempleHub.connect(paramoniaNest, "Paramonia Temple HUB to Nests")
    
def connect_scrabania_regions(world: NNTWorld) -> None:
    menu = world.get_region("Menu")
    scrabania = world.get_region("Scrabania")
    scrabaniaStartSecret = world.get_region("Scrabanian Temple Entrance (Secret Area)")
    scrabaniaTempleHub = world.get_region("Scrabanian Temple HUB")
    scrabaniaTrial1 = world.get_region("Scrabanian Temple Trial 1")
    scrabaniaTrial2 = world.get_region("Scrabanian Temple Trial 2")
    scrabaniaTrial3 = world.get_region("Scrabanian Temple Trial 3")
    scrabaniaTrial4 = world.get_region("Scrabanian Temple Trial 4")
    scrabaniaTrial5 = world.get_region("Scrabanian Temple Trial 5")
    scrabaniaTrial6 = world.get_region("Scrabanian Temple Trial 6")
    scrabaniaTrial7 = world.get_region("Scrabanian Temple Trial 7")
    scrabaniaTrial7Secret = world.get_region("Scrabanian Temple Trial 7 (Secret Area)")
    scrabaniaTrial8 = world.get_region("Scrabanian Temple Trial 8")
    scrabaniaTrial8Secret = world.get_region("Scrabanian Temple Trial 8 (Secret Area)")
    scrabaniaNest = world.get_region("Scrabanian Nests")
    
    menu.connect(scrabania, "Menu to Scrabania")
    scrabania.connect(scrabaniaStartSecret, "Scrabania to Temple Entrance Secret")
    scrabania.connect(scrabaniaTempleHub, "Scrabania to Temple HUB")
    scrabaniaTempleHub.connect(scrabaniaTrial1, "Scrabania Temple HUB to Trial 1")
    scrabaniaTempleHub.connect(scrabaniaTrial2, "Scrabania Temple HUB to Trial 2")
    scrabaniaTempleHub.connect(scrabaniaTrial3, "Scrabania Temple HUB to Trial 3")
    scrabaniaTempleHub.connect(scrabaniaTrial4, "Scrabania Temple HUB to Trial 4")
    scrabaniaTempleHub.connect(scrabaniaTrial5, "Scrabania Temple HUB to Trial 5")
    scrabaniaTempleHub.connect(scrabaniaTrial6, "Scrabania Temple HUB to Trial 6")
    scrabaniaTempleHub.connect(scrabaniaTrial7, "Scrabania Temple HUB to Trial 7")
    scrabaniaTrial7.connect(scrabaniaTrial7Secret, "Scrabania Trial 7 Secret Area Access")
    scrabaniaTempleHub.connect(scrabaniaTrial8, "Scrabania Temple HUB to Trial 8")
    scrabaniaTrial8.connect(scrabaniaTrial8Secret, "Scrabania Trial 8 Secret Area Access")
    scrabaniaTempleHub.connect(scrabaniaNest, "Scrabania Temple HUB to Nests")
    
def connect_zulag1_regions(world: NNTWorld) -> None:
    menu = world.get_region("Menu")
    zulag1 = world.get_region("Zulag 1")
    zulag1Cargo = world.get_region("Zulag 1 (Cargo Lift)")
    zulag1Grinder = world.get_region("Zulag 1 (Grinder Tutorial)")
    zulag1Shadow = world.get_region("Zulag 1 (Shadow Tutorial)")
    zulag1SligLock = world.get_region("Zulag 1 (Slig Voice Lock)")
    zulag1Shrykull = world.get_region("Zulag 1 (Shrykull Portal Tutorial)")
    zulag1S1 = world.get_region("Zulag 1 (Secret Area 1)")
    zulag1GameSpeak = world.get_region("Zulag 1 (GameSpeak Tutorial)")
    zulag1Interactables = world.get_region("Zulag 1 (Interactables Tutorial)")
    zulag1S2 = world.get_region("Zulag 1 (Secret Area 2)")
    zulag1S3 = world.get_region("Zulag 1 (Secret Area 3)")
    zulag1S4 = world.get_region("Zulag 1 (Secret Area 4)")
    zulag1Backtrack = world.get_region("Zulag 1 (Backtrack End)")
    zulag1S5 = world.get_region("Zulag 1 (Secret Area 5)")
    zulag1Z2Access = world.get_region("Zulag 1 (Zulag 2 Access)")
    
    menu.connect(zulag1, "Menu to Zulag 1")
    zulag1.connect(zulag1Cargo, "Zulag 1 Cargo Lift")
    zulag1Cargo.connect(zulag1Grinder, "Zulag 1 Grinder Tutorial")
    zulag1Cargo.connect(zulag1Shadow, "Zulag 1 Shadow Tutorial")
    zulag1Shadow.connect(zulag1SligLock, "Zulag 1 Slig Voice Lock")
    zulag1SligLock.connect(zulag1Shrykull, "Zulag 1 Shrykull Portal Tutorial")
    zulag1SligLock.connect(zulag1S1, "Zulag 1 Secret Area 1 Access")
    zulag1SligLock.connect(zulag1GameSpeak, "Zulag 1 GameSpeak Tutorial")
    zulag1GameSpeak.connect(zulag1Interactables, "Zulag 1 Interactables Tutorial")
    zulag1Interactables.connect(zulag1S2, "Zulag 1 Secret Area 2 Access")
    zulag1Interactables.connect(zulag1S3, "Zulag 1 Secret Area 3 Access")
    zulag1Interactables.connect(zulag1S4, "Zulag 1 Secret Area 4 Access")
    zulag1Interactables.connect(zulag1Backtrack, "Zulag 1 Backtrack End")
    zulag1Backtrack.connect(zulag1S5, "Zulag 1 Secret Area 5 Access")
    zulag1Cargo.connect(zulag1Z2Access, "Zulag 1 Zulag 2 Access")
    
def connect_zulag2_regions(world: NNTWorld) -> None:
    menu = world.get_region("Menu")
    zulag2 = world.get_region("Zulag 2")
    zulag2Door1 = world.get_region("Zulag 2 (Door 1)")
    zulag2Door1Back = world.get_region("Zulag 2 (Door 1 Back Area)")
    zulag2Door2 = world.get_region("Zulag 2 (Door 2)")
    zulag2Door3 = world.get_region("Zulag 2 (Door 3)")
    
    menu.connect(zulag2, "Menu to Zulag 2")
    zulag2.connect(zulag2Door1, "Zulag 2 Door 1 Path")
    zulag2Door1.connect(zulag2Door1Back, "Zulag 2 Door 1 Back Area")
    zulag2.connect(zulag2Door2, "Zulag 2 Door 2 Path")
    zulag2.connect(zulag2Door3, "Zulag 2 Door 3 Path")
    
def connect_zulag3_regions(world: NNTWorld) -> None:
    menu = world.get_region("Menu")
    zulag3 = world.get_region("Zulag 3")
    zulag3Door1 = world.get_region("Zulag 3 (Door 1)")
    zulag3Door1Back = world.get_region("Zulag 3 (Door 1 Back Area)")
    zulag3Door2 = world.get_region("Zulag 3 (Door 2)")
    zulag3Door3 = world.get_region("Zulag 3 (Door 3)")
    zulag3Door3Back = world.get_region("Zulag 3 (Door 3 Back Area)")
    
    menu.connect(zulag3, "Menu to Zulag 3")
    zulag3.connect(zulag3Door1, "Zulag 3 Door 1 Path")
    zulag3Door1.connect(zulag3Door1Back, "Zulag 3 Door 1 Back Area")
    zulag3.connect(zulag3Door2, "Zulag 3 Door 2 Path")
    zulag3.connect(zulag3Door3, "Zulag 3 Door 3 Path")
    zulag3Door3.connect(zulag3Door3Back, "Zulag 3 Door 3 Back Area")
    
def connect_zulag4_regions(world: NNTWorld) -> None:
    menu = world.get_region("Menu")
    zulag4 = world.get_region("Zulag 4")
    zulag4S1 = world.get_region("Zulag 4 (Secret Area 1)")
    zulag4SligPath = world.get_region("Zulag 4 (Slig Path)")
    zulag4SligPathG = world.get_region("Zulag 4 (Slig Path Post Grenades)")
    zulag4S2 = world.get_region("Zulag 4 (Secret Area 2)")
    boardroom = world.get_region("Boardroom")
    
    menu.connect(zulag4, "Menu to Zulag 4")
    zulag4.connect(zulag4S1, "Zulag 4 Secret Area 1 Access")
    zulag4.connect(zulag4SligPath, "Zulag 4 Slig Path")
    zulag4SligPath.connect(zulag4SligPathG, "Zulag 4 Slig Path Post Grenades")
    zulag4SligPathG.connect(zulag4S2, "Zulag 4 Secret Area 2 Access")
    menu.connect(boardroom, "Menu to Boardroom")