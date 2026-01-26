from dataclasses import dataclass
from Options import OptionGroup, Choice, PerGameCommonOptions, Range, Toggle, DefaultOnToggle

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

class FillerStarCards(DefaultOnToggle):
    """Allow extra Star Cards to be added as Filler Items."""
    display_name = "Filler Star Cards"

class FillerTimeCapsules(DefaultOnToggle):
    """Allow extra Time Capsules to be added as Filler Items."""
    display_name = "Filler Time Capsules"

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

class ShopInfo(Choice):
    """How much information about an item should be shown in the shops, Battlesphere challenge list and end of stage Star Card.
    Full = The item's name and flags will be shown. As will its sprite and description if one is given.
    Flags = The item's name (and sprite and description if one is given) will be hidden, but the AP trap/progression sprites will still be shown.
    Hidden = No information about the item other than the receiver will be given.
    Nothing = Gives no information about the item at all."""
    display_name = "Show Item Names in Shops"
    option_full = 0
    option_flags = 1
    option_hidden = 2
    option_nothing = 3

class EnemySanity(DefaultOnToggle):
    """Makes killing each enemy type into checks, adding 72 locations."""
    display_name = "Enemy Sanity"

class BossSanity(DefaultOnToggle):
    """Makes killing each boss type into checks, adding 44 locations."""
    display_name = "Boss Sanity"
    
class ItemBoxSanity(Toggle):
    """Adds the various item boxes found in stages to the location pool."""
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

class TrapBraveStones(Toggle):
    """Treat negative Brave Stones as traps and auto activate them upon receiving."""
    display_name = "Trap Brave Stones"

class DangerousTimeLimit(Toggle):
    """Make the Time Limit Brave Stone kill the player upon the timer running out."""
    display_name = "Dangerous Time Limit"

class BaseTrapWeight(Choice):
    """Base class for trap weights.
    The available options are 0 (off), 1 (low), 2 (medium), and 3 (high).
    2 and 3 add an extra copy to the list, hopefully increasing the chances of the generator picking it. 3 adds a second copy on top of the first."""
    option_none = 0
    option_low = 1
    option_medium = 2
    option_high = 3
    default = 1
    
class SwapTrapWeight(BaseTrapWeight):
    """Likelihood of receiving a trap that swaps the player character."""
    display_name = "Swap Trap Weight"
    
class MirrorTrapWeight(BaseTrapWeight):
    """Likelihood of receiving a trap that mirrors the stage for thirty seconds."""
    display_name = "Mirror Trap Weight"
    
class PieTrapWeight(BaseTrapWeight):
    """Likelihood of receiving a trap that spawns one of Acrabelle's pies on the player."""
    display_name = "Pie Trap Weight"
    
class SpringTrapWeight(BaseTrapWeight):
    """Likelihood of receiving a trap that spawns a spring in front of the player.."""
    display_name = "Spring Trap Weight"
    
class PowerPointTrapWeight(BaseTrapWeight):
    """Likelihood of receiving a trap that locks the game to fifteen frames per second for thirty seconds."""
    display_name = "PowerPoint Trap Weight"
    
class ZoomTrapWeight(BaseTrapWeight):
    """Likelihood of receiving a trap that zooms the screen in for thirty seconds."""
    display_name = "Zoom Trap Weight"
    
class AaaTrapWeight(BaseTrapWeight):
    """Likelihood of receiving a trap of Aaa screaming for a while."""
    display_name = "Aaa Trap Weight"
    
class SpikeBallTrapWeight(BaseTrapWeight):
    """Likelihood of receiving a trap that spawns multiple spike balls moving towards the player."""
    display_name = "Spike Ball Trap Weight"
    
class PixellationTrapWeight(BaseTrapWeight):
    """Likelihood of receiving a trap that pixellates the screen for thirty seconds."""
    display_name = "Pixellation Trap Weight"
    
class RailTrapWeight(BaseTrapWeight):
    """Likelihood of receiving a trap that turns every surface in the stage into a rail."""
    display_name = "Rail Trap Weight"
    
class SpamTrapWeight(BaseTrapWeight):
    """Likelihood of receiving a trap that puts random spam messages onto the screen to distract the player."""
    display_name = "Spam Trap Weight"
    
class SyntaxJumpscareTrapWeight(BaseTrapWeight):
    """Likelihood of receiving a trap that suddenly spawns a large Syntax on the screen."""
    display_name = "Syntax Jumpscare Trap Weight"

class FastWeaponsCore(Toggle):
    """Skips the actual stage of Weapon's Core and goes straight to the Bakunawa Fusion fight."""
    display_name = "Fast Weapon's Core"

class TrapChance(Range):
    """
    How many fillers will be replaced with traps. 0 means no additional traps, 100 means all fillers are traps.
    """
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 0

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

option_groups = [
    OptionGroup(
        "Extra Filler Options",
        [FillerStarCards, FillerTimeCapsules],
    ),
    OptionGroup(
        "Chest Options",
        [Chests, ChestTracers, ChestTracerItems, StrictChestLock],
    ),
    OptionGroup(
        "Shop Options",
        [MillasShop, MillaShopAmount, MillaShopPrice, VinylShop, VinylShopAmount, VinylShopPrice, ShopInfo],
    ),
    OptionGroup(
        "Sanity Options",
        [EnemySanity, BossSanity, ItemBoxSanity, ItemBoxCrystal, ItemBoxPetal, ItemBoxShield, ItemBoxGoldGem],
    ),
    OptionGroup(
        "Trap Options",
        [TrapChance, TrapBraveStones, DangerousTimeLimit, TrapLink],
    ),
    OptionGroup(
        "Trap Weight Options",
        [SwapTrapWeight, MirrorTrapWeight, PieTrapWeight, SpringTrapWeight, PowerPointTrapWeight, ZoomTrapWeight, AaaTrapWeight, SpikeBallTrapWeight, PixellationTrapWeight, RailTrapWeight, SpamTrapWeight, SyntaxJumpscareTrapWeight],
    ),
]

@dataclass
class FP2Options(PerGameCommonOptions):
    chapters: Chapters
    filler_star_cards: FillerStarCards
    filler_time_capsules: FillerTimeCapsules
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
    shop_information: ShopInfo
    enemies: EnemySanity
    bosses: BossSanity
    item_boxes: ItemBoxSanity
    item_boxes_crystals: ItemBoxCrystal
    item_boxes_petals: ItemBoxPetal
    item_boxes_shields: ItemBoxShield
    item_boxes_goldgems: ItemBoxGoldGem
    extra_items: ExtraItems
    trap_stones: TrapBraveStones
    dangerous_time_limit: DangerousTimeLimit
    swap_trap_weight: SwapTrapWeight
    mirror_trap_weight: MirrorTrapWeight
    pie_trap_weight: PieTrapWeight
    spring_trap_weight: SpringTrapWeight
    powerpoint_trap_weight: PowerPointTrapWeight
    zoom_trap_weight: ZoomTrapWeight
    aaa_trap_weight: AaaTrapWeight
    spikeball_trap_weight: SpikeBallTrapWeight
    pixellation_trap_weight: PixellationTrapWeight
    rail_trap_weight: RailTrapWeight
    spam_trap_weight: SpamTrapWeight
    syntax_jumpscare_trap_weight: SyntaxJumpscareTrapWeight
    fast_weapons_core: FastWeaponsCore
    filler_traps: TrapChance
    death_link: DeathLink
    ring_link: RingLink
    trap_link: TrapLink