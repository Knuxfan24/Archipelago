from dataclasses import dataclass
from Options import Choice, PerGameCommonOptions, Range, Toggle

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

# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class NNTOptions(PerGameCommonOptions):
    goal: Goal
    muds_required: MudokonRequirement
    death_link: DeathLink
    death_link_amnesty: DeathLinkAmnesty
