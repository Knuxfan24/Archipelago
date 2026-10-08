from dataclasses import dataclass
from Options import OptionGroup, Choice, PerGameCommonOptions, Range, Toggle, DefaultOnToggle, OptionDict, OptionSet

class GoalStage(Choice):
    """Which stage should be the final one.
    Both require 32 Star Cards, but Weapon's Core also requires 13 Time Capsules.
    Selecting Merga as the goal completely removes Time Capsules from the item pool."""
    display_name = "Goal Stage"
    option_merga = 0
    option_weapons_core = 1
    default = 1

class Chapters(Choice):
    """Determines how stages should be unlocked.
    Individual = Stages unlock in sets, based on their grouping in the Adventure Mode.
    Progressive = Stages unlock in sets in a set order.
    Open = Stages unlock individually, without their Star Card requirements."""
    display_name = "Chapter Unlocks"
    option_individual = 0
    option_progressive = 1
    option_open = 2
    default = 2
    
class StarCardLocks(DefaultOnToggle):
    """If using the Individual or Progressive Chapter Unlocks, should stages beyond Globe Opera be locked by a Star Card requirement.
    
    Globe Opera and the Persua Episodes require 11 Star Cards, while the Bakunawa Episode requires 23."""
    display_name = "Star Card Locks"
    
class ExtraStarCards(Range):
    """How many extra Progression Flagged Star Cards should be added to the Item Pool. """
    display_name = "Extra Progression Star Cards"
    range_start = 0
    range_end = 64
    default = 16
    
class ExtraTimeCapsules(Range):
    """How many extra Progression Flagged Time Capsules should be added to the Item Pool. """
    display_name = "Extra Progression Time Capsules"
    range_start = 0
    range_end = 32
    default = 8
    
class FillerStarCards(DefaultOnToggle):
    """Allow extra Star Cards to be added as Filler Items. Unlike the extra Progression Flagged ones, these can be overwritten with traps."""
    display_name = "Filler Star Cards"

class FillerTimeCapsules(DefaultOnToggle):
    """Allow extra Time Capsules to be added as Filler Items. Unlike the extra Progression Flagged ones, these can be overwritten with traps."""
    display_name = "Filler Time Capsules"
    
class RainbowSRank(Toggle):
    """Makes getting Rainbow S-Ranks into locations."""
    display_name = "Enable Rainbow S-Ranks"
    
class SRank(Toggle):
    """Makes getting S-Ranks into locations.
    Obtaining a Rainbow S-Rank will also send the S-Rank location."""
    display_name = "Enable S-Ranks"
    
class SRankRequiresBraveStone(DefaultOnToggle):
    """Only adds S-Ranks to logic when at least one Brave Stone is acquired.
    If disabled, then S-Ranking a stage via completing it without taking damage will be logically expected."""
    display_name = "S-Ranks Logically Require Brave Stones"
    
class ARank(DefaultOnToggle):
    """Makes getting A-Ranks into locations.
    Obtaining an S-Rank or Rainbow S-Rank will also send the A-Rank location."""
    display_name = "Enable A-Ranks"

class Chests(DefaultOnToggle):
    """Makes opening chests into checks, adding 82 locations."""
    display_name = "Enable Item Chests"

class ChestTracers(DefaultOnToggle):
    """Enables the drawing of arrows that point to any unopened chests in the level (can be toggled with F9 or Select)."""
    display_name = "Enable Chest Tracers"

class ChestTracerItems(Choice):
    """Locks each stage's chest tracer behind an item, either globally or per stage.
    If enabled, then the chests for each stage will not be logically required without the stage's tracer."""
    display_name = "Enable Chest Tracer Items"
    option_disabled = 0
    option_perstage = 1
    option_global = 2
    default = 0

class StrictChestLock(Toggle):
    """Require a stage's Chest Tracer to be able to open its chests at all."""
    display_name = "Strict Chest Locks"

class MillasShop(DefaultOnToggle):
    """Makes buying items from Milla's shop on the level select into checks, adding as many locations as specified in the next option."""
    display_name = "Enable Milla's Shop"

class MillaShopAmount(Range):
    """How many locations Milla's shop will have."""
    display_name = "Milla Shop Location Count"
    range_start = 8
    range_end = 1000
    default = 30

class MillaShopPrice(Range):
    """The cost that the items in Milla's shop will be set to, in Gold Gems."""
    display_name = "Milla Shop Price"
    range_start = 1
    range_end = 100
    default = 1

class GoldGemCrystalCost(Range):
    """How many Crystal Shards are required to make a Gold Gem."""
    display_name = "Gold Gem Crystal Cost"
    range_start = 100
    range_end = 10000
    default = 1000

class GoldGemCoreCost(Range):
    """How many Robot Cores are required to make a Gold Gem."""
    display_name = "Gold Gem Core Cost"
    range_start = 5
    range_end = 100
    default = 20

class VinylShop(DefaultOnToggle):
    """Makes buying the vinyls from the shop on the level select into checks, adding as many locations as specified in the next option."""
    display_name = "Enable Vinyl Shop"

class VinylShopAmount(Range):
    """How many locations the Vinyl shop will have."""
    display_name = "Vinyl Shop Location Count"
    range_start = 8
    range_end = 1000
    default = 60

class VinylShopPrice(Range):
    """The cost that the items in the Vinyl shop will be set to, in Crystal Shards."""
    display_name = "Vinyl Shop Price"
    default = 100
    range_start = 100
    range_end = 30000

class EnemySanity(DefaultOnToggle):
    """Makes killing each enemy type into checks, adding 72 locations."""
    display_name = "Enemy Sanity"

class BossSanity(DefaultOnToggle):
    """Makes killing each boss type into checks, adding 44 locations."""
    display_name = "Boss Sanity"
    
class ItemBoxSanity(Toggle):
    """Adds the various item boxes found in stages to the location pool.
    Currently experimental with a severe lack of logic."""
    display_name = "Item Box Sanity"
    
class ItemBoxCrystal(DefaultOnToggle):
    """Include Crystal Item Boxes in the Item Box Sanity."""
    display_name = "Item Box Sanity (Crystals)"
    
class ItemBoxPetal(DefaultOnToggle):
    """Include Petal Item Boxes in the Item Box Sanity."""
    display_name = "Item Box Sanity (Petals)"
    
class ItemBoxShield(DefaultOnToggle):
    """Include Shield Item Boxes in the Item Box Sanity."""
    display_name = "Item Box Sanity (Shields)"
    
class ItemBoxGoldGem(DefaultOnToggle):
    """Include Gold Gem Item Boxes in the Item Box Sanity."""
    display_name = "Item Box Sanity (Gold Gem)"

class ExtraItems(DefaultOnToggle):
    """Adds the unused extra item/potion slots to the item pool."""
    display_name = "Include Extra Item Slots"

class DangerousTimeLimit(Toggle):
    """Make the Time Limit Brave Stone kill the player upon the timer running out."""
    display_name = "Dangerous Time Limit"

class FastWeaponsCore(Toggle):
    """Skips the actual stage of Weapon's Core and goes straight to the Bakunawa Fusion fight."""
    display_name = "Fast Weapon's Core"

class TrapChance(Range):
    """ How many fillers will be replaced with traps. 0 means no additional traps, 100 means all fillers are traps. """
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 0
    
class SonicModCompatibility(Toggle):
    """ Adds seven Chaos Emerald items to the item pool. When all seven are collected the Chaos Emeralds item from the Sonic mod will be added to the player's inventory, allowing usage of a character's Super Form."""
    display_name = "Sonic Mod Compatibility"
    
class PotionSellerModCompatibility(Toggle):
    """Adds the items from the Potion Seller mod to the item pool."""
    display_name = "Potion Seller Mod Compatibility"
    
class LightningModCompatibility(Toggle):
    """Adds the Step Booster from the Lightning mod to the item pool."""
    display_name = "Lightning Mod Compatibility"

class DeathLink(Choice):
    """When you die, everyone dies. Of course the reverse is true too.
    If survive is enabled, then you can revive on the spot as normal."""
    display_name = "DeathLink"
    option_disable = 0
    option_enable = 1
    option_enable_survive = 2

class RingLink(Toggle):
    """Whether picking up a crystal shard will also send one to other RingLink players."""
    display_name = "RingLink"
    
class TrapLink(Toggle):
    """Whether your received traps are linked to other players."""
    display_name = "TrapLink"
    
class DamageLink(Toggle):
    """Any damage you take is also sent to other players with DamageLink enabled.
    Of course the reverse is true too."""
    display_name = "DamageLink"

class TrapBraveStones(Toggle):
    """Treat negative Brave Stones as traps, allowing the copies specified in Trap Weights (Brave Stones) to be added to the item pool along the always placed ones and auto activating them upon receiving."""
    display_name = "Trap Brave Stones"
   
class TrapWeightsBraveStones(OptionDict):
    """How likely it is to receive an extra copy of a negative Brave Stone as a trap. Valid options are:
    none
    low
    medium
    high
    
    These will only be added if the Trap Brave Stones option is enabled.
    In addition, the Invisibility Cloak, Madstone, Explosive Finale, Idol of Greed and Gravity Boots will only be added if the Potion Seller Mod Compatibility is enabled."""
    display_name = "Trap Weights (Brave Stones)"
    default = {
        "No Stocks": "low",
        "Expensive Stocks": "low",
        "Double Damage": "low",
        "No Revivals": "low",
        "No Guarding": "low",
        "No Petals": "low",
        "Time Limit": "low",
        "Items To Bombs": "low",
        "Life Oscillation": "low",
        "One Hit KO": "low",
        "Invisibility Cloak": "low",
        "Madstone": "low",
        "Explosive Finale": "low",
        "Idol of Greed": "low",
        "Gravity Boots": "low",
    }
    valid_values = ["low", "medium", "high"]
    
class TrapWeightsAnnoyance(OptionDict):
    """How likely it is to receive a trap designed primarly to annoy the player. Valid options are:
    none
    low
    medium
    high"""
    display_name = "Trap Weights (Annoyance)"
    default = {
        "PowerPoint Trap": "low",
        "Aaa Trap": "low",
        "Pixellation Trap": "low",
        "Spam Trap": "low",
        "Syntax Jumpscare Trap": "low",
        "Scott The Woz Trap": "low",
    }
    valid_values = ["low", "medium", "high"]
    
class TrapWeightsGameplay(OptionDict):
    """How likely it is to receive a trap designed to impact gameplay. Valid options are:
    none
    low
    medium
    high"""
    display_name = "Trap Weights (Gameplay)"
    default = {
        "Swap Trap": "low",
        "Mirror Trap": "low",
        "Pie Trap": "low",
        "Spring Trap": "low",
        "Zoom Trap": "low",
        "Spike Ball Trap": "low",
        "Rail Trap": "low",
        "Mach Speed Trap": "low",
    }
    valid_values = ["low", "medium", "high"]
    
class TrapWeightsMiniGame(OptionDict):
    """How likely it is to receive a trap that forces the player to play a life or death mini-game. Valid options are:
    none
    low
    medium
    high"""
    display_name = "Trap Weights (Mini-Game)"
    default = {
        "Trivia Trap": "low",
        "Wordle Trap": "low"
    }
    valid_values = ["low", "medium", "high"]

class ValidStartingStages(OptionSet):
    """Stages that the generator can choose to be the starting stage if using the Open Chapters option."""
    display_name = "Valid Starting Stages"
    default = frozenset({
        "Dragon Valley",
        "Shenlin Park",
        "Tiger Falls",
        "Robot Graveyard",
        "Shade Armory",
        "Avian Museum",
        "Airship Sigwada",
        "Phoenix Highway",
        "Zao Land",
        "Globe Opera 1",
        "Globe Opera 2",
        "Palace Courtyard",
        "Tidal Gate",
        "Sky Bridge",
        "Lightning Tower",
        "Zulon Jungle",
        "Nalao Lake",
        "Ancestral Forge",
        "Magma Starscape",
        "Gravity Bubble",
        "Bakunawa Chase",
        "Bakunawa Rush",
        "Clockwork Arboretum",
        "Inversion Dynamo",
        "Lunar Cannon",
    })

class ValidStartingBosses(OptionSet):
    """Bosses that the generator can choose to be the starting stage if using the Open Chapters option.
    Merga is only a valid option if the goal is set to Weapon's Core."""
    display_name = "Valid Starting Bosses"
    default = frozenset({
        "Snowfields",
        "Auditorium",
        "Diamond Point",
        "Refinery Room",
        "Merga"
    })


option_groups = [
    OptionGroup(
        "Goal Options",
        [GoalStage, Chapters, ValidStartingStages, ValidStartingBosses]
    ),
    OptionGroup(
        "Links",
        [DeathLink, RingLink, TrapLink, DamageLink],
    ),
    OptionGroup(
        "Extra Progression Items",
        [ExtraStarCards, ExtraTimeCapsules, FillerStarCards, FillerTimeCapsules],
    ),
    OptionGroup(
        "Rank Sanity Options",
        [RainbowSRank, SRank, SRankRequiresBraveStone, ARank],
    ),
    OptionGroup(
        "Shop Options",
        [MillasShop, MillaShopAmount, MillaShopPrice, GoldGemCrystalCost, GoldGemCoreCost, VinylShop, VinylShopAmount, VinylShopPrice],
    ),
    OptionGroup(
        "Object Sanity Options",
        [Chests, StrictChestLock, EnemySanity, BossSanity, ItemBoxSanity, ItemBoxCrystal, ItemBoxPetal, ItemBoxShield, ItemBoxGoldGem],
    ),
    OptionGroup(
        "Chest Tracer Options",
        [ChestTracers, ChestTracerItems],
    ),
    OptionGroup(
        "Trap Options",
        [TrapChance, TrapBraveStones, DangerousTimeLimit, TrapWeightsBraveStones, TrapWeightsAnnoyance, TrapWeightsGameplay, TrapWeightsMiniGame],
    ),
    OptionGroup(
        "Mod Compatibility Options",
        [SonicModCompatibility, PotionSellerModCompatibility, LightningModCompatibility]
    ),
]

@dataclass
class FP2Options(PerGameCommonOptions):
    goal: GoalStage
    chapters: Chapters
    star_locks: StarCardLocks
    extra_star_cards: ExtraStarCards
    extra_time_capsules: ExtraTimeCapsules
    filler_star_cards: FillerStarCards
    filler_time_capsules: FillerTimeCapsules
    rainbow_s_rank: RainbowSRank
    s_rank: SRank
    s_rank_brave_stones: SRankRequiresBraveStone
    a_rank: ARank
    chests: Chests
    chest_tracers: ChestTracers
    chest_tracer_items: ChestTracerItems
    chest_tracer_strict: StrictChestLock
    milla_shop: MillasShop
    vinyl_shop: VinylShop
    milla_shop_amount: MillaShopAmount
    vinyl_shop_amount: VinylShopAmount
    milla_shop_price: MillaShopPrice
    vinyl_shop_price: VinylShopPrice
    gold_gem_crystal_cost: GoldGemCrystalCost
    gold_gem_core_cost: GoldGemCoreCost
    enemies: EnemySanity
    bosses: BossSanity
    item_boxes: ItemBoxSanity
    item_boxes_crystals: ItemBoxCrystal
    item_boxes_petals: ItemBoxPetal
    item_boxes_shields: ItemBoxShield
    item_boxes_goldgems: ItemBoxGoldGem
    extra_items: ExtraItems
    trap_stones: TrapBraveStones
    trap_weight_brave_stones: TrapWeightsBraveStones
    trap_weight_annoyance: TrapWeightsAnnoyance
    trap_weight_gameplay: TrapWeightsGameplay
    trap_weight_minigame: TrapWeightsMiniGame
    dangerous_time_limit: DangerousTimeLimit
    fast_weapons_core: FastWeaponsCore
    filler_traps: TrapChance
    sonic_mod: SonicModCompatibility
    potion_seller_mod: PotionSellerModCompatibility
    lightning_mod: LightningModCompatibility
    death_link: DeathLink
    ring_link: RingLink
    trap_link: TrapLink
    damage_link: DamageLink
    starting_stages: ValidStartingStages
    starting_bosses: ValidStartingBosses