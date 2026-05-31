# Empty world specifically so that the Link Tester can only be used on generations that want it.
from worlds.AutoWorld import World

class TesterWorld(World):
    game = "Link Tester"
    hidden = False
    item_name_to_id = {}
    location_name_to_id = {}