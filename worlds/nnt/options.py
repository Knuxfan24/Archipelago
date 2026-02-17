from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions, Range, Toggle, DefaultOnToggle

class Goal(Choice):
    """
    Whether the final area will be The Boardroom or the Alf's Escape DLC.
    """

    display_name = "Goal"

    option_the_boardroom = 0
    option_alfs_escape = 1

    default = option_the_boardroom

class MudokonRequirement(Range):
    """
    The percentage of the Mudokons in the multiworld that need to be rescued before access is granted to The Boardroom or Alf's Escape.
    """
    display_name = "Mudokons Required"
    range_start = 25
    range_end = 100
    default = 50
    
class AreaClears(DefaultOnToggle):
    """
    Whether completing an area should send a check.
    """
    display_name = "Area Clear Checks"
    
class ExtraAreaClears(Toggle):
    """
    Adds extra area clear checks for the Monsaic Lines, Paramonia, Scrabania and Stockyard Return, which are otherwise completely excluded due to having no Mudokons to rescue.
    """
    display_name = "Extra Area Clear Checks"

class TrapChance(Range):
    """
    How many filler Mudokons will be replaced with traps. 0 means no additional traps, 100 means all filler Mudokons are traps.
    """
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 0
    
class DeathLink(Toggle):
    """When you die, everyone who enabled DeathLink dies. Of course, the reverse is true too."""
    display_name = "DeathLink"
    
class DeathLinkAmnesty(Range):
    """Amount of forgiven deaths before sending a DeathLink.
    0 means that every death will send a DeathLink."""
    display_name = "DeathLink Amnesty"
    range_start = 0
    range_end = 20
    default = 10

class JokeRingLink(Toggle):
    """Makes saving a Mudokon also send out a single Ring to other RingLink games, while a Mudokon dying will take a Ring from other RingLink games.
    This option is purely for the sake of a joke."""
    display_name = "Joke RingLink"

# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class NNTOptions(PerGameCommonOptions):
    goal: Goal
    muds_required: MudokonRequirement
    area_clears: AreaClears
    extra_area_clears: ExtraAreaClears
    filler_traps: TrapChance
    death_link: DeathLink
    death_link_amnesty: DeathLinkAmnesty
    ring_link: JokeRingLink
