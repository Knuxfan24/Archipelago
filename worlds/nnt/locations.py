from __future__ import annotations
from typing import TYPE_CHECKING
from BaseClasses import Location
from . import items
if TYPE_CHECKING:
    from .world import NNTWorld

# Create our location table, organised by:
# - Mudokons based on their internal IDs
# - Paramonian Trials
# - Scrabanian Trials
# - Zulag 2 Doors
# - Zulag 3 Doors
# - Area Clears
LOCATION_NAME_TO_ID = {
    "Rupture Farms Escape ~ Secret Area 1 - Mudokon 1": 1,
    "Rupture Farms Escape ~ Secret Area 1 - Mudokon 2": 2,
    "Rupture Farms Escape ~ Secret Area 1 - Mudokon 3": 3,
    "Rupture Farms Escape ~ Secret Area 2 - Mudokon 1": 4,
    "Rupture Farms Escape ~ Secret Area 2 - Mudokon 2": 5,
    "Rupture Farms Escape ~ Interactable Tutorial - Mudokon 1": 6,
    "Rupture Farms Escape ~ Secret Area 3 - Mudokon 1": 7,
    "Rupture Farms Escape ~ Secret Area 3 - Mudokon 2": 8,
    "Rupture Farms Escape ~ Interactable Tutorial - Mudokon 2": 9,
    "Rupture Farms Escape ~ Secret Area 4 - Mudokon 1": 10,
    "Rupture Farms Escape ~ GameSpeak Tutorial - Mudokon 1": 11,
    "Rupture Farms Escape ~ Bottlecap Tutorial - Mudokon 1": 12,
    "Rupture Farms Escape ~ Secret Area 5 - Mudokon 1": 13,
    "Rupture Farms Escape ~ Secret Area 5 - Mudokon 2": 14,
    "Rupture Farms Escape ~ Secret Area 5 - Mudokon 3": 15,
    "Rupture Farms Escape ~ Bottlecap Tutorial - Mudokon 2": 16,
    "Rupture Farms Escape ~ Shadow Tutorial - Mudokon 1": 17,
    "Rupture Farms Escape ~ Grinder Tutorial Mudokon": 18,
    "Rupture Farms Escape ~ Shadow Tutorial - Mudokon 2": 19,
    "Rupture Farms Escape ~ Zulag 2 Access - Mudokon 1": 20,
    "Rupture Farms Escape ~ Zulag 2 Access - Mudokon 2": 21,
    "Rupture Farms Escape ~ Zulag 2 Train Terminal Mudokon": 22,
    "Rupture Farms Escape ~ Zulag 2 Access - Mudokon 3": 23,
    "Rupture Farms Escape ~ Zulag 2 Access - Mudokon 4": 24,
    "Rupture Farms Escape ~ Zulag 2 Access - Mudokon 5": 25,
    "Rupture Farms Escape ~ Secret Area 6 - Mudokon 1": 26,
    "Rupture Farms Escape ~ Secret Area 6 - Mudokon 2": 27,
    "Rupture Farms Escape ~ Secret Area 6 - Mudokon 3": 28,
    "Stockyards ~ Introduction Mudokon": 29,
    "Stockyards ~ Secret Area - Mudokon 1": 30,
    "Stockyards ~ Secret Area - Mudokon 2": 31,
    "Free Fire Zone ~ Secret Area 4 - Mudokon 1": 32,
    "Free Fire Zone ~ Secret Area 4 - Mudokon 2": 33,
    "Free Fire Zone ~ Secret Area 1 - Mudokon 1": 34,
    "Free Fire Zone ~ Secret Area 3 - Mudokon 1": 35,
    "Free Fire Zone ~ Secret Area 3 - Mudokon 2": 36,
    "Free Fire Zone ~ Secret Area 1 - Mudokon 2": 37,
    "Free Fire Zone ~ Secret Area 2 - Mudokon 1": 38,
    "Free Fire Zone ~ Secret Area 5 - Mudokon 1": 39,
    "Free Fire Zone ~ Secret Area 6 - Mudokon 1": 40,
    "Paramonian Trial 5 ~ Secret Area - Mudokon 1": 41,
    "Paramonian Trial 5 ~ Secret Area - Mudokon 2": 42,
    "Paramonian Trial 5 ~ Secret Area - Mudokon 3": 43,
    "Scrabanian Temple Entrance ~ Secret Area - Mudokon 1": 44,
    "Scrabanian Temple Entrance ~ Secret Area - Mudokon 2": 45,
    "Scrabanian Trial 7 ~ Secret Area - Mudokon 1": 46,
    "Scrabanian Trial 8 ~ Secret Area - Mudokon 1": 47,
    "Scrabanian Trial 8 ~ Secret Area - Mudokon 2": 48,
    "Scrabanian Trial 8 ~ Secret Area - Mudokon 3": 49,
    "Zulag 1 ~ Entrance - Mudokon 1": 50,
    "Zulag 1 ~ Zulag 2 Access - Mudokon 1": 51,
    "Zulag 1 ~ Zulag 2 Access - Mudokon 2": 52,
    "Zulag 1 ~ Shadow Tutorial - Mudokon 1": 53,
    "Zulag 1 ~ Grinder Tutorial Mudokon": 54,
    "Zulag 1 ~ Shrykull Portal Tutorial - Mudokon 1": 55,
    "Zulag 1 ~ Shrykull Portal Tutorial - Mudokon 2": 56,
    "Zulag 1 ~ Secret Area 1 - Mudokon 1": 57,
    "Zulag 1 ~ Secret Area 1 - Mudokon 2": 58,
    "Zulag 1 ~ Secret Area 1 - Mudokon 3": 59,
    "Zulag 1 ~ GameSpeak Tutorial - Mudokon 1": 60,
    "Zulag 1 ~ GameSpeak Tutorial - Mudokon 2": 61,
    "Zulag 1 ~ Secret Area 2 - Mudokon 1": 62,
    "Zulag 1 ~ Secret Area 2 - Mudokon 2": 63,
    "Zulag 1 ~ Interactables Tutorial - Mudokon 1": 64,
    "Zulag 1 ~ Interactables Tutorial - Mudokon 2": 65,
    "Zulag 1 ~ Secret Area 3 - Mudokon 1": 66,
    "Zulag 1 ~ Secret Area 3 - Mudokon 2": 67,
    "Zulag 1 ~ Secret Area 4 - Mudokon 1": 68,
    "Zulag 1 ~ Secret Area 4 - Mudokon 2": 69,
    "Zulag 1 ~ Backtrack End - Mudokon 1": 70,
    "Zulag 1 ~ Backtrack End - Mudokon 2": 71,
    "Zulag 1 ~ Backtrack End - Mudokon 3": 72,
    "Zulag 1 ~ Secret Area 5 - Mudokon 1": 73,
    "Zulag 1 ~ Secret Area 5 - Mudokon 2": 74,
    "Zulag 2 ~ Door 1 - Mudokon 1": 75,
    "Zulag 2 ~ Door 1 - Mudokon 2": 76,
    "Zulag 2 ~ Door 1 - Mudokon 3": 77,
    "Zulag 2 ~ Door 1 (Back Area) - Mudokon 1": 78,
    "Zulag 2 ~ Door 1 (Back Area) - Mudokon 2": 79,
    "Zulag 2 ~ Door 2 - Mudokon 1": 80,
    "Zulag 2 ~ Door 2 - Mudokon 2": 81,
    "Zulag 2 ~ Door 3 - Mudokon 1": 82,
    "Zulag 1 ~ Entrance - Mudokon 2": 83,
    "Zulag 3 ~ Door 1 - Mudokon 1": 84,
    "Zulag 3 ~ Door 1 - Mudokon 2": 86,
    "Zulag 3 ~ Door 1 - Mudokon 3": 87,
    "Zulag 3 ~ Door 1 (Back Area) - Mudokon 1": 88,
    "Zulag 3 ~ Door 1 (Back Area) - Mudokon 2": 89,
    "Zulag 3 ~ Door 2 - Mudokon 1": 90,
    "Zulag 3 ~ Door 3 - Mudokon 1": 91,
    "Zulag 3 ~ Door 3 (Back Area) - Mudokon 1": 92,
    "Zulag 3 ~ Door 3 (Back Area) - Mudokon 2": 93,
    "Zulag 4 ~ Slig Path - Mudokon 1": 94,
    "Zulag 4 ~ Slig Path - Mudokon 2": 95,
    "Zulag 4 ~ Slig Path (Post Boom Machine) - Mudokon 1": 96,
    "Zulag 4 ~ Slig Path (Post Boom Machine) - Mudokon 2": 97,
    "Zulag 4 ~ Slig Path (Post Boom Machine) - Mudokon 3": 98,
    "Rupture Farms Escape ~ Secret Area 1 - Mudokon 4": 100,
    "Rupture Farms Escape ~ Secret Area 1 - Mudokon 5": 101,
    "Rupture Farms Escape ~ Secret Area 1 - Mudokon 6": 102,
    "Rupture Farms Escape ~ Secret Area 1 - Mudokon 7": 103,
    "Rupture Farms Escape ~ Secret Area 1 - Mudokon 8": 104,
    "Rupture Farms Escape ~ Secret Area 1 - Mudokon 9": 105,
    "Rupture Farms Escape ~ Secret Area 2 - Mudokon 3": 106,
    "Rupture Farms Escape ~ Secret Area 2 - Mudokon 4": 107,
    "Rupture Farms Escape ~ Secret Area 2 - Mudokon 5": 108,
    "Rupture Farms Escape ~ Secret Area 2 - Mudokon 6": 109,
    "Rupture Farms Escape ~ Secret Area 2 - Mudokon 7": 110,
    "Rupture Farms Escape ~ Secret Area 2 - Mudokon 8": 111,
    "Rupture Farms Escape ~ Secret Area 2 - Mudokon 9": 112,
    "Rupture Farms Escape ~ Secret Area 3 - Mudokon 3": 113,
    "Rupture Farms Escape ~ Secret Area 3 - Mudokon 4": 114,
    "Rupture Farms Escape ~ Secret Area 3 - Mudokon 5": 115,
    "Rupture Farms Escape ~ Secret Area 3 - Mudokon 6": 116,
    "Rupture Farms Escape ~ Secret Area 3 - Mudokon 7": 117,
    "Rupture Farms Escape ~ Secret Area 3 - Mudokon 8": 118,
    "Rupture Farms Escape ~ Secret Area 4 - Mudokon 2": 119,
    "Rupture Farms Escape ~ Secret Area 4 - Mudokon 3": 120,
    "Rupture Farms Escape ~ Secret Area 4 - Mudokon 4": 121,
    "Rupture Farms Escape ~ Secret Area 4 - Mudokon 5": 122,
    "Rupture Farms Escape ~ Secret Area 4 - Mudokon 6": 123,
    "Rupture Farms Escape ~ Secret Area 4 - Mudokon 7": 124,
    "Rupture Farms Escape ~ Secret Area 4 - Mudokon 8": 125,
    "Rupture Farms Escape ~ GameSpeak Tutorial - Mudokon 2": 126,
    "Rupture Farms Escape ~ GameSpeak Tutorial - Mudokon 3": 127,
    "Rupture Farms Escape ~ GameSpeak Tutorial - Mudokon 4": 128,
    "Rupture Farms Escape ~ Secret Area 5 - Mudokon 4": 129,
    "Rupture Farms Escape ~ Secret Area 5 - Mudokon 5": 130,
    "Rupture Farms Escape ~ Secret Area 5 - Mudokon 6": 131,
    "Rupture Farms Escape ~ Secret Area 5 - Mudokon 7": 132,
    "Rupture Farms Escape ~ Secret Area 5 - Mudokon 8": 133,
    "Rupture Farms Escape ~ Secret Area 6 - Mudokon 4": 134,
    "Rupture Farms Escape ~ Secret Area 6 - Mudokon 5": 135,
    "Rupture Farms Escape ~ Secret Area 6 - Mudokon 6": 136,
    "Rupture Farms Escape ~ Secret Area 6 - Mudokon 7": 137,
    "Stockyards ~ Secret Area - Mudokon 3": 138,
    "Stockyards ~ Secret Area - Mudokon 4": 139,
    "Stockyards ~ Secret Area - Mudokon 5": 140,
    "Free Fire Zone ~ Secret Area 4 - Mudokon 3": 141,
    "Free Fire Zone ~ Secret Area 4 - Mudokon 4": 142,
    "Free Fire Zone ~ Secret Area 4 - Mudokon 5": 143,
    "Free Fire Zone ~ Secret Area 3 - Mudokon 3": 144,
    "Free Fire Zone ~ Secret Area 1 - Mudokon 3": 145,
    "Free Fire Zone ~ Secret Area 1 - Mudokon 4": 146,
    "Free Fire Zone ~ Secret Area 1 - Mudokon 5": 147,
    "Free Fire Zone ~ Secret Area 1 - Mudokon 6": 148,
    "Free Fire Zone ~ Secret Area 1 - Mudokon 7": 149,
    "Free Fire Zone ~ Secret Area 1 - Mudokon 8": 150,
    "Free Fire Zone ~ Secret Area 1 - Mudokon 9": 151,
    "Free Fire Zone ~ Secret Area 2 - Mudokon 2": 152,
    "Free Fire Zone ~ Secret Area 2 - Mudokon 3": 153,
    "Free Fire Zone ~ Secret Area 6 - Mudokon 2": 154,
    "Free Fire Zone ~ Secret Area 6 - Mudokon 3": 155,
    "Free Fire Zone ~ Secret Area 6 - Mudokon 4": 156,
    "Free Fire Zone ~ Secret Area 6 - Mudokon 5": 157,
    "Free Fire Zone ~ Secret Area 6 - Mudokon 6": 158,
    "Free Fire Zone ~ Secret Area 6 - Mudokon 7": 159,
    "Free Fire Zone ~ Secret Area 5 - Mudokon 2": 160,
    "Free Fire Zone ~ Secret Area 5 - Mudokon 3": 161,
    "Free Fire Zone ~ Secret Area 5 - Mudokon 4": 162,
    "Free Fire Zone ~ Secret Area 5 - Mudokon 5": 163,
    "Free Fire Zone ~ Secret Area 5 - Mudokon 6": 164,
    "Free Fire Zone ~ Secret Area 5 - Mudokon 7": 165,
    "Free Fire Zone ~ Secret Area 5 - Mudokon 8": 166,
    "Paramonian Trial 5 ~ Secret Area - Mudokon 4": 167,
    "Paramonian Trial 5 ~ Secret Area - Mudokon 5": 168,
    "Paramonian Trial 5 ~ Secret Area - Mudokon 6": 169,
    "Paramonian Trial 5 ~ Secret Area - Mudokon 7": 170,
    "Paramonian Trial 5 ~ Secret Area - Mudokon 8": 171,
    "Paramonian Trial 5 ~ Secret Area - Mudokon 9": 172,
    "Scrabanian Temple Entrance ~ Secret Area - Mudokon 3": 173,
    "Scrabanian Temple Entrance ~ Secret Area - Mudokon 4": 174,
    "Scrabanian Trial 7 ~ Secret Area - Mudokon 2": 175,
    "Scrabanian Trial 7 ~ Secret Area - Mudokon 3": 176,
    "Scrabanian Trial 7 ~ Secret Area - Mudokon 4": 177,
    "Scrabanian Trial 7 ~ Secret Area - Mudokon 5": 178,
    "Scrabanian Trial 8 ~ Secret Area - Mudokon 4": 179,
    "Scrabanian Trial 8 ~ Secret Area - Mudokon 5": 180,
    "Scrabanian Trial 8 ~ Secret Area - Mudokon 6": 181,
    "Zulag 1 ~ Shadow Tutorial - Mudokon 2": 182,
    "Zulag 1 ~ Shadow Tutorial - Mudokon 3": 183,
    "Zulag 1 ~ Zulag 2 Access - Mudokon 3": 184,
    "Zulag 1 ~ Zulag 2 Access - Mudokon 4": 185,
    "Zulag 1 ~ Shadow Tutorial - Mudokon 4": 186,
    "Zulag 1 ~ Shrykull Portal Tutorial - Mudokon 3": 187,
    "Zulag 1 ~ Shrykull Portal Tutorial - Mudokon 4": 188,
    "Zulag 1 ~ Shrykull Portal Tutorial - Mudokon 5": 189,
    "Zulag 1 ~ Shrykull Portal Tutorial - Mudokon 6": 190,
    "Zulag 1 ~ GameSpeak Tutorial - Mudokon 3": 191,
    "Zulag 1 ~ GameSpeak Tutorial - Mudokon 4": 192,
    "Zulag 1 ~ GameSpeak Tutorial - Mudokon 5": 193,
    "Zulag 1 ~ GameSpeak Tutorial - Mudokon 6": 194,
    "Zulag 1 ~ GameSpeak Tutorial - Mudokon 7": 195,
    "Zulag 1 ~ Secret Area 1 - Mudokon 4": 196,
    "Zulag 1 ~ Secret Area 1 - Mudokon 5": 197,
    "Zulag 1 ~ Secret Area 1 - Mudokon 6": 198,
    "Zulag 1 ~ Interactables Tutorial - Mudokon 3": 199,
    "Zulag 1 ~ Interactables Tutorial - Mudokon 4": 200,
    "Zulag 1 ~ Interactables Tutorial - Mudokon 5": 201,
    "Zulag 1 ~ Backtrack End - Mudokon 4": 202,
    "Zulag 1 ~ Backtrack End - Mudokon 5": 203,
    "Zulag 1 ~ Backtrack End - Mudokon 6": 204,
    "Zulag 1 ~ Backtrack End - Mudokon 7": 205,
    "Zulag 1 ~ Entrance - Mudokon 3": 206,
    "Zulag 1 ~ Backtrack End - Mudokon 8": 207,
    "Zulag 1 ~ Backtrack End - Mudokon 9": 208,
    "Zulag 1 ~ Secret Area 2 - Mudokon 3": 209,
    "Zulag 1 ~ Secret Area 2 - Mudokon 4": 210,
    "Zulag 1 ~ Secret Area 2 - Mudokon 5": 211,
    "Zulag 1 ~ Secret Area 2 - Mudokon 6": 212,
    "Zulag 1 ~ Secret Area 2 - Mudokon 7": 213,
    "Zulag 1 ~ Secret Area 2 - Mudokon 8": 214,
    "Zulag 1 ~ Secret Area 3 - Mudokon 3": 215,
    "Zulag 1 ~ Secret Area 3 - Mudokon 4": 216,
    "Zulag 1 ~ Secret Area 3 - Mudokon 5": 217,
    "Zulag 1 ~ Secret Area 3 - Mudokon 6": 218,
    "Zulag 1 ~ Secret Area 3 - Mudokon 7": 219,
    "Zulag 1 ~ Secret Area 3 - Mudokon 8": 220,
    "Zulag 1 ~ Secret Area 4 - Mudokon 3": 222,
    "Zulag 1 ~ Secret Area 4 - Mudokon 4": 223,
    "Zulag 1 ~ Secret Area 5 - Mudokon 3": 226,
    "Zulag 1 ~ Secret Area 5 - Mudokon 4": 227,
    "Zulag 1 ~ Secret Area 5 - Mudokon 5": 228,
    "Zulag 1 ~ Secret Area 5 - Mudokon 6": 229,
    "Zulag 1 ~ Secret Area 5 - Mudokon 7": 230,
    "Zulag 1 ~ Secret Area 5 - Mudokon 8": 231,
    "Zulag 2 ~ Door 1 - Mudokon 4": 232,
    "Zulag 2 ~ Door 1 - Mudokon 5": 233,
    "Zulag 2 ~ Door 1 - Mudokon 6": 234,
    "Zulag 2 ~ Door 1 - Mudokon 7": 235,
    "Zulag 2 ~ Door 1 - Mudokon 8": 236,
    "Zulag 2 ~ Door 1 - Mudokon 9": 237,
    "Zulag 2 ~ Door 1 (Back Area) - Mudokon 3": 238,
    "Zulag 2 ~ Door 1 (Back Area) - Mudokon 4": 239,
    "Zulag 2 ~ Door 1 (Back Area) - Mudokon 5": 240,
    "Zulag 2 ~ Door 1 (Back Area) - Mudokon 6": 241,
    "Zulag 2 ~ Door 3 - Mudokon 2": 242,
    "Zulag 2 ~ Door 3 - Mudokon 3": 243,
    "Zulag 2 ~ Door 3 - Mudokon 4": 244,
    "Zulag 2 ~ Door 3 - Mudokon 5": 245,
    "Zulag 2 ~ Door 3 - Mudokon 6": 246,
    "Zulag 2 ~ Door 3 - Mudokon 7": 247,
    "Zulag 2 ~ Door 3 - Mudokon 8": 248,
    "Zulag 2 ~ Door 3 - Mudokon 9": 249,
    "Zulag 2 ~ Door 2 - Mudokon 3": 250,
    "Zulag 2 ~ Door 2 - Mudokon 4": 251,
    "Zulag 2 ~ Door 2 - Mudokon 5": 252,
    "Zulag 3 ~ Door 1 - Mudokon 4": 253,
    "Zulag 3 ~ Door 1 - Mudokon 5": 254,
    "Zulag 3 ~ Door 1 - Mudokon 6": 255,
    "Zulag 3 ~ Door 1 - Mudokon 7": 256,
    "Zulag 3 ~ Door 1 - Mudokon 8": 258,
    "Zulag 3 ~ Door 1 - Mudokon 9": 259,
    "Zulag 3 ~ Door 1 (Back Area) - Mudokon 3": 260,
    "Zulag 3 ~ Door 1 (Back Area) - Mudokon 4": 261,
    "Zulag 3 ~ Door 1 (Back Area) - Mudokon 5": 262,
    "Zulag 4 ~ Secret Area 1 - Mudokon 1": 263,
    "Zulag 4 ~ Secret Area 1 - Mudokon 2": 264,
    "Zulag 4 ~ Secret Area 1 - Mudokon 3": 265,
    "Zulag 3 ~ Door 2 - Mudokon 2": 266,
    "Zulag 3 ~ Door 2 - Mudokon 3": 267,
    "Zulag 3 ~ Door 2 - Mudokon 4": 268,
    "Zulag 3 ~ Door 2 - Mudokon 5": 269,
    "Zulag 3 ~ Door 3 - Mudokon 2": 270,
    "Zulag 3 ~ Door 3 - Mudokon 3": 271,
    "Zulag 3 ~ Door 3 - Mudokon 4": 272,
    "Zulag 3 ~ Door 3 - Mudokon 5": 273,
    "Zulag 3 ~ Door 3 - Mudokon 6": 274,
    "Zulag 3 ~ Door 3 - Mudokon 7": 275,
    "Zulag 3 ~ Door 3 - Mudokon 8": 276,
    "Zulag 3 ~ Door 3 - Mudokon 9": 277,
    "Zulag 3 ~ Door 3 (Back Area) - Mudokon 3": 278,
    "Zulag 3 ~ Door 3 (Back Area) - Mudokon 4": 279,
    "Zulag 3 ~ Door 3 (Back Area) - Mudokon 5": 280,
    "Zulag 3 ~ Door 3 (Back Area) - Mudokon 6": 281,
    "Zulag 3 ~ Door 3 (Back Area) - Mudokon 7": 282,
    "Zulag 3 ~ Door 3 (Back Area) - Mudokon 8": 283,
    "Zulag 4 ~ Slig Path - Mudokon 3": 284,
    "Zulag 4 ~ Slig Path - Mudokon 4": 285,
    "Zulag 4 ~ Slig Path - Mudokon 5": 286,
    "Zulag 4 ~ Slig Path - Mudokon 6": 287,
    "Zulag 4 ~ Slig Path - Mudokon 7": 288,
    "Zulag 4 ~ Slig Path - Mudokon 8": 289,
    "Zulag 4 ~ Slig Path - Mudokon 9": 290,
    "Zulag 4 ~ Slig Path (Post Boom Machine) - Mudokon 4": 291,
    "Zulag 4 ~ Slig Path (Post Boom Machine) - Mudokon 5": 292,
    "Zulag 4 ~ Secret Area 2 - Mudokon 1": 293,
    "Zulag 4 ~ Secret Area 2 - Mudokon 2": 294,
    "Zulag 4 ~ Secret Area 2 - Mudokon 3": 295,
    "Rupture Farms Escape ~ UXB Tutorial - Mudokon 1": 296,
    "Rupture Farms Escape ~ UXB Tutorial - Mudokon 2": 297,
    "Rupture Farms Escape ~ Shadow Tutorial - Mudokon 3": 298,
    "Rupture Farms Escape ~ Shadow Tutorial - Mudokon 4": 299,
    
    "Paramonian Trial 1": 1001,
    "Paramonian Trial 2": 1002,
    "Paramonian Trial 3": 1003,
    "Paramonian Trial 4": 1004,
    "Paramonian Trial 5": 1005,
    "Paramonian Trial 6": 1006,
    
    "Scrabanian Trial 1": 1011,
    "Scrabanian Trial 2": 1012,
    "Scrabanian Trial 3": 1013,
    "Scrabanian Trial 4": 1014,
    "Scrabanian Trial 5": 1015,
    "Scrabanian Trial 6": 1016,
    "Scrabanian Trial 7": 1017,
    "Scrabanian Trial 8": 1018,
    
    "Zulag 2 Door 1": 1021,
    "Zulag 2 Door 2": 1022,
    "Zulag 2 Door 3": 1023,
    
    "Zulag 3 Door 1": 1031,
    "Zulag 3 Door 2": 1032,
    "Zulag 3 Door 3": 1033,
    
    "Rupture Farms - Clear": 1041,
    "Stockyard Escape - Clear": 1042,
    "Monsaic Lines - Clear": 1043,
    "Paramonia - Clear": 1044,
    "Paramonian Nests - Clear": 1045,
    "Scrabania - Clear": 1046,
    "Scrabanian Nests - Clear": 1047,
    "Stockyard Return - Clear": 1048,
    "Zulag 1 - Clear": 1049,
    "Zulag 2 - Clear": 1050,
    "Zulag 3 - Clear": 1051,
    "Zulag 4 - Clear": 1052,
}

class NNTLocation(Location):
    game = "New 'n' Tasty"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

# TODO: Fiddle with these, as they feel a bit messy.
def create_all_locations(world: NNTWorld) -> None:
    create_rupturefarms_locations(world)
    create_stockyards_locations(world)
    create_paramonia_locations(world)
    create_scrabania_locations(world)
    create_zulag1_locations(world)
    create_zulag2_locations(world)
    create_zulag3_locations(world)
    create_zulag4_locations(world)
    
    if world.options.area_clears == 1:
        create_areaclear_locations(world)
        
    # Remove the extra Mudokon locations if the no_nnt_muds option is on.
    if world.options.no_nnt_muds == 1:
        for region in world.get_regions():
            locations_to_remove = []
            region_locations = region.get_locations()
            
            # Loop through each location in this region and check its address. If its between 100 and 300, then flag it for removal.
            for location in region_locations:
                if location.address != None:
                    if (int(location.address) >= 100 and int(location.address < 300)):
                        locations_to_remove.append(location)
                        
            # Loop through and remove each location we've flagged.
            for location in locations_to_remove:
                region.locations.remove(location)
    

def create_rupturefarms_locations(world: NNTWorld) -> None:
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
    
    rFarmsInteractablesMuds = get_location_names_with_ids(
        [
        "Rupture Farms Escape ~ Interactable Tutorial - Mudokon 1",
        "Rupture Farms Escape ~ Interactable Tutorial - Mudokon 2",
        ]
    )
    
    rFarmsGameSpeakMuds = get_location_names_with_ids(
        [
        "Rupture Farms Escape ~ GameSpeak Tutorial - Mudokon 1",
        "Rupture Farms Escape ~ GameSpeak Tutorial - Mudokon 2",
        "Rupture Farms Escape ~ GameSpeak Tutorial - Mudokon 3",
        "Rupture Farms Escape ~ GameSpeak Tutorial - Mudokon 4",
        ]
    )
    
    rFarmsBottlecapMuds = get_location_names_with_ids(
        [
        "Rupture Farms Escape ~ Bottlecap Tutorial - Mudokon 1",
        "Rupture Farms Escape ~ Bottlecap Tutorial - Mudokon 2",
        ]
    )
    
    rFarmsShadowMuds = get_location_names_with_ids(
        [
        "Rupture Farms Escape ~ Shadow Tutorial - Mudokon 1",
        "Rupture Farms Escape ~ Shadow Tutorial - Mudokon 2",
        "Rupture Farms Escape ~ Shadow Tutorial - Mudokon 3",
        "Rupture Farms Escape ~ Shadow Tutorial - Mudokon 4",
        ]
    )
    
    rFarmsUXBMuds = get_location_names_with_ids(
        [
        "Rupture Farms Escape ~ UXB Tutorial - Mudokon 1",
        "Rupture Farms Escape ~ UXB Tutorial - Mudokon 2",
        ]
    )
    
    rFarmsGrinderMud = get_location_names_with_ids(
        [
        "Rupture Farms Escape ~ Grinder Tutorial Mudokon",
        ]
    )
    
    rFarmsZ2AccessMuds = get_location_names_with_ids(
        [
        "Rupture Farms Escape ~ Zulag 2 Access - Mudokon 1",
        "Rupture Farms Escape ~ Zulag 2 Access - Mudokon 2",
        "Rupture Farms Escape ~ Zulag 2 Access - Mudokon 3",
        "Rupture Farms Escape ~ Zulag 2 Access - Mudokon 4",
        "Rupture Farms Escape ~ Zulag 2 Access - Mudokon 5",
        "Rupture Farms Escape ~ Zulag 2 Train Terminal Mudokon",
        ]
    )
    
    rFarmsS1Muds = get_location_names_with_ids(
        [
            "Rupture Farms Escape ~ Secret Area 1 - Mudokon 1",
            "Rupture Farms Escape ~ Secret Area 1 - Mudokon 2",
            "Rupture Farms Escape ~ Secret Area 1 - Mudokon 3",
            "Rupture Farms Escape ~ Secret Area 1 - Mudokon 4",
            "Rupture Farms Escape ~ Secret Area 1 - Mudokon 5",
            "Rupture Farms Escape ~ Secret Area 1 - Mudokon 6",
            "Rupture Farms Escape ~ Secret Area 1 - Mudokon 7",
            "Rupture Farms Escape ~ Secret Area 1 - Mudokon 8",
            "Rupture Farms Escape ~ Secret Area 1 - Mudokon 9",
        ]
    )
    
    rFarmsS2Muds = get_location_names_with_ids(
        [
            "Rupture Farms Escape ~ Secret Area 2 - Mudokon 1",
            "Rupture Farms Escape ~ Secret Area 2 - Mudokon 2",
            "Rupture Farms Escape ~ Secret Area 2 - Mudokon 3",
            "Rupture Farms Escape ~ Secret Area 2 - Mudokon 4",
            "Rupture Farms Escape ~ Secret Area 2 - Mudokon 5",
            "Rupture Farms Escape ~ Secret Area 2 - Mudokon 6",
            "Rupture Farms Escape ~ Secret Area 2 - Mudokon 7",
            "Rupture Farms Escape ~ Secret Area 2 - Mudokon 8",
            "Rupture Farms Escape ~ Secret Area 2 - Mudokon 9",
        ]
    )
    
    rFarmsS3Muds = get_location_names_with_ids(
        [
            "Rupture Farms Escape ~ Secret Area 3 - Mudokon 1",
            "Rupture Farms Escape ~ Secret Area 3 - Mudokon 2",
            "Rupture Farms Escape ~ Secret Area 3 - Mudokon 3",
            "Rupture Farms Escape ~ Secret Area 3 - Mudokon 4",
            "Rupture Farms Escape ~ Secret Area 3 - Mudokon 5",
            "Rupture Farms Escape ~ Secret Area 3 - Mudokon 6",
            "Rupture Farms Escape ~ Secret Area 3 - Mudokon 7",
            "Rupture Farms Escape ~ Secret Area 3 - Mudokon 8",
        ]
    )
    
    rFarmsS4Muds = get_location_names_with_ids(
        [
            "Rupture Farms Escape ~ Secret Area 4 - Mudokon 1",
            "Rupture Farms Escape ~ Secret Area 4 - Mudokon 2",
            "Rupture Farms Escape ~ Secret Area 4 - Mudokon 3",
            "Rupture Farms Escape ~ Secret Area 4 - Mudokon 4",
            "Rupture Farms Escape ~ Secret Area 4 - Mudokon 5",
            "Rupture Farms Escape ~ Secret Area 4 - Mudokon 6",
            "Rupture Farms Escape ~ Secret Area 4 - Mudokon 7",
            "Rupture Farms Escape ~ Secret Area 4 - Mudokon 8",
        ]
    )
        
    rFarmsS5Muds = get_location_names_with_ids(
        [
        "Rupture Farms Escape ~ Secret Area 5 - Mudokon 1",
        "Rupture Farms Escape ~ Secret Area 5 - Mudokon 2",
        "Rupture Farms Escape ~ Secret Area 5 - Mudokon 3",
        "Rupture Farms Escape ~ Secret Area 5 - Mudokon 4",
        "Rupture Farms Escape ~ Secret Area 5 - Mudokon 5",
        "Rupture Farms Escape ~ Secret Area 5 - Mudokon 6",
        "Rupture Farms Escape ~ Secret Area 5 - Mudokon 7",
        "Rupture Farms Escape ~ Secret Area 5 - Mudokon 8",
        ]
    )
    
    rFarmsS6Muds = get_location_names_with_ids(
        [
            "Rupture Farms Escape ~ Secret Area 6 - Mudokon 1",
            "Rupture Farms Escape ~ Secret Area 6 - Mudokon 2",
            "Rupture Farms Escape ~ Secret Area 6 - Mudokon 3",
            "Rupture Farms Escape ~ Secret Area 6 - Mudokon 4",
            "Rupture Farms Escape ~ Secret Area 6 - Mudokon 5",
            "Rupture Farms Escape ~ Secret Area 6 - Mudokon 6",
            "Rupture Farms Escape ~ Secret Area 6 - Mudokon 7",
        ]
    )
    
    rFarmsS1.add_locations(rFarmsS1Muds, NNTLocation)
    rFarmsS2.add_locations(rFarmsS2Muds, NNTLocation)
    rFarmsS3.add_locations(rFarmsS3Muds, NNTLocation)
    rFarmsS4.add_locations(rFarmsS4Muds, NNTLocation)
    rFarmsInteractables.add_locations(rFarmsInteractablesMuds, NNTLocation)
    rFarmsGameSpeak.add_locations(rFarmsGameSpeakMuds, NNTLocation)
    rFarmsS5.add_locations(rFarmsS5Muds, NNTLocation)
    rFarmsBottlecap.add_locations(rFarmsBottlecapMuds, NNTLocation)
    rFarmsShadow.add_locations(rFarmsShadowMuds, NNTLocation)
    rFarmsUXB.add_locations(rFarmsUXBMuds, NNTLocation)
    rFarmsGrinder.add_locations(rFarmsGrinderMud, NNTLocation)
    rFarmsZ2Access.add_locations(rFarmsZ2AccessMuds, NNTLocation)
    rFarmsS6.add_locations(rFarmsS6Muds, NNTLocation)
    
def create_stockyards_locations(world: NNTWorld) -> None:
    stockyardsIntro = world.get_region("Stockyards")
    stockyardsSecret = world.get_region("Stockyards (Secret Area)")
    ffZoneS1 = world.get_region("Free Fire Zone (Secret Area 1)")
    ffZoneS2 = world.get_region("Free Fire Zone (Secret Area 2)")
    ffZoneS3 = world.get_region("Free Fire Zone (Secret Area 3)")
    ffZoneS4 = world.get_region("Free Fire Zone (Secret Area 4)")
    ffZoneS5 = world.get_region("Free Fire Zone (Secret Area 5)")
    ffZoneS6 = world.get_region("Free Fire Zone (Secret Area 6)")
    
    stockyardsIntroMud = get_location_names_with_ids(
        [
        "Stockyards ~ Introduction Mudokon",
        ]
    )
    
    stockyardsSecretMuds = get_location_names_with_ids(
        [
        "Stockyards ~ Secret Area - Mudokon 1",
        "Stockyards ~ Secret Area - Mudokon 2",
        "Stockyards ~ Secret Area - Mudokon 3",
        "Stockyards ~ Secret Area - Mudokon 4",
        "Stockyards ~ Secret Area - Mudokon 5",
        ]
    )
    
    ffZoneS1Muds = get_location_names_with_ids(
        [
        "Free Fire Zone ~ Secret Area 1 - Mudokon 1",
        "Free Fire Zone ~ Secret Area 1 - Mudokon 2",
        "Free Fire Zone ~ Secret Area 1 - Mudokon 3",
        "Free Fire Zone ~ Secret Area 1 - Mudokon 4",
        "Free Fire Zone ~ Secret Area 1 - Mudokon 5",
        "Free Fire Zone ~ Secret Area 1 - Mudokon 6",
        "Free Fire Zone ~ Secret Area 1 - Mudokon 7",
        "Free Fire Zone ~ Secret Area 1 - Mudokon 8",
        "Free Fire Zone ~ Secret Area 1 - Mudokon 9",
        ]
    )
    
    ffZoneS2Muds = get_location_names_with_ids(
        [
        "Free Fire Zone ~ Secret Area 2 - Mudokon 1",
        "Free Fire Zone ~ Secret Area 2 - Mudokon 2",
        "Free Fire Zone ~ Secret Area 2 - Mudokon 3",
        ]
    )
    
    ffZoneS3Muds = get_location_names_with_ids(
        [
        "Free Fire Zone ~ Secret Area 3 - Mudokon 1",
        "Free Fire Zone ~ Secret Area 3 - Mudokon 2",
        "Free Fire Zone ~ Secret Area 3 - Mudokon 3",
        ]
    )
    
    ffZoneS4Muds = get_location_names_with_ids(
        [
        "Free Fire Zone ~ Secret Area 4 - Mudokon 1",
        "Free Fire Zone ~ Secret Area 4 - Mudokon 2",
        "Free Fire Zone ~ Secret Area 4 - Mudokon 3",
        "Free Fire Zone ~ Secret Area 4 - Mudokon 4",
        "Free Fire Zone ~ Secret Area 4 - Mudokon 5",
        ]
    )
    
    ffZoneS5Muds = get_location_names_with_ids(
        [
        "Free Fire Zone ~ Secret Area 5 - Mudokon 1",
        "Free Fire Zone ~ Secret Area 5 - Mudokon 2",
        "Free Fire Zone ~ Secret Area 5 - Mudokon 3",
        "Free Fire Zone ~ Secret Area 5 - Mudokon 4",
        "Free Fire Zone ~ Secret Area 5 - Mudokon 5",
        "Free Fire Zone ~ Secret Area 5 - Mudokon 6",
        "Free Fire Zone ~ Secret Area 5 - Mudokon 7",
        "Free Fire Zone ~ Secret Area 5 - Mudokon 8",
        ]
    )
    
    ffZoneS6Muds = get_location_names_with_ids(
        [
        "Free Fire Zone ~ Secret Area 6 - Mudokon 1",
        "Free Fire Zone ~ Secret Area 6 - Mudokon 2",
        "Free Fire Zone ~ Secret Area 6 - Mudokon 3",
        "Free Fire Zone ~ Secret Area 6 - Mudokon 4",
        "Free Fire Zone ~ Secret Area 6 - Mudokon 5",
        "Free Fire Zone ~ Secret Area 6 - Mudokon 6",
        "Free Fire Zone ~ Secret Area 6 - Mudokon 7",
        ]
    )
    
    stockyardsIntro.add_locations(stockyardsIntroMud, NNTLocation)
    stockyardsSecret.add_locations(stockyardsSecretMuds, NNTLocation)
    ffZoneS1.add_locations(ffZoneS1Muds, NNTLocation)
    ffZoneS2.add_locations(ffZoneS2Muds, NNTLocation)
    ffZoneS3.add_locations(ffZoneS3Muds, NNTLocation)
    ffZoneS4.add_locations(ffZoneS4Muds, NNTLocation)
    ffZoneS5.add_locations(ffZoneS5Muds, NNTLocation)
    ffZoneS6.add_locations(ffZoneS6Muds, NNTLocation)
    
def create_paramonia_locations(world: NNTWorld) -> None:
    paramoniaTrial1 = world.get_region("Paramonian Temple Trial 1")
    paramoniaTrial2 = world.get_region("Paramonian Temple Trial 2")
    paramoniaTrial3 = world.get_region("Paramonian Temple Trial 3")
    paramoniaTrial4 = world.get_region("Paramonian Temple Trial 4")
    paramoniaTrial5 = world.get_region("Paramonian Temple Trial 5")
    paramoniaTrial5Secret = world.get_region("Paramonian Temple Trial 5 (Secret Area)")
    paramoniaTrial6 = world.get_region("Paramonian Temple Trial 6")
    
    paramoniaTrial1.add_locations(get_location_names_with_ids(["Paramonian Trial 1"]), NNTLocation)
    paramoniaTrial2.add_locations(get_location_names_with_ids(["Paramonian Trial 2"]), NNTLocation)
    paramoniaTrial3.add_locations(get_location_names_with_ids(["Paramonian Trial 3"]), NNTLocation)
    paramoniaTrial4.add_locations(get_location_names_with_ids(["Paramonian Trial 4"]), NNTLocation)
    paramoniaTrial5.add_locations(get_location_names_with_ids(["Paramonian Trial 5"]), NNTLocation)
    paramoniaTrial5Secret.add_locations(get_location_names_with_ids(
        [
        "Paramonian Trial 5 ~ Secret Area - Mudokon 1",
        "Paramonian Trial 5 ~ Secret Area - Mudokon 2",
        "Paramonian Trial 5 ~ Secret Area - Mudokon 3",
        "Paramonian Trial 5 ~ Secret Area - Mudokon 4",
        "Paramonian Trial 5 ~ Secret Area - Mudokon 5",
        "Paramonian Trial 5 ~ Secret Area - Mudokon 6",
        "Paramonian Trial 5 ~ Secret Area - Mudokon 7",
        "Paramonian Trial 5 ~ Secret Area - Mudokon 8",
        "Paramonian Trial 5 ~ Secret Area - Mudokon 9",
        ]
    ))
    paramoniaTrial6.add_locations(get_location_names_with_ids(["Paramonian Trial 6"]), NNTLocation)
    
def create_scrabania_locations(world: NNTWorld) -> None:
    scrabaniaStartSecret = world.get_region("Scrabanian Temple Entrance (Secret Area)")
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
    
    scrabaniaStartSecret.add_locations(get_location_names_with_ids(
        [
        "Scrabanian Temple Entrance ~ Secret Area - Mudokon 1",
        "Scrabanian Temple Entrance ~ Secret Area - Mudokon 2",
        "Scrabanian Temple Entrance ~ Secret Area - Mudokon 3",
        "Scrabanian Temple Entrance ~ Secret Area - Mudokon 4",
        ]
    ))
    
    scrabaniaTrial1.add_locations(get_location_names_with_ids(["Scrabanian Trial 1"]), NNTLocation)
    scrabaniaTrial2.add_locations(get_location_names_with_ids(["Scrabanian Trial 2"]), NNTLocation)
    scrabaniaTrial3.add_locations(get_location_names_with_ids(["Scrabanian Trial 3"]), NNTLocation)
    scrabaniaTrial4.add_locations(get_location_names_with_ids(["Scrabanian Trial 4"]), NNTLocation)
    scrabaniaTrial5.add_locations(get_location_names_with_ids(["Scrabanian Trial 5"]), NNTLocation)
    scrabaniaTrial6.add_locations(get_location_names_with_ids(["Scrabanian Trial 6"]), NNTLocation)
    scrabaniaTrial7.add_locations(get_location_names_with_ids(["Scrabanian Trial 7"]), NNTLocation)
    scrabaniaTrial7Secret.add_locations(get_location_names_with_ids(
        [
        "Scrabanian Trial 7 ~ Secret Area - Mudokon 1",
        "Scrabanian Trial 7 ~ Secret Area - Mudokon 2",
        "Scrabanian Trial 7 ~ Secret Area - Mudokon 3",
        "Scrabanian Trial 7 ~ Secret Area - Mudokon 4",
        "Scrabanian Trial 7 ~ Secret Area - Mudokon 5",
        ]
    ))
    scrabaniaTrial8.add_locations(get_location_names_with_ids(["Scrabanian Trial 8"]), NNTLocation)
    scrabaniaTrial8Secret.add_locations(get_location_names_with_ids(
        [
        "Scrabanian Trial 8 ~ Secret Area - Mudokon 1",
        "Scrabanian Trial 8 ~ Secret Area - Mudokon 2",
        "Scrabanian Trial 8 ~ Secret Area - Mudokon 3",
        "Scrabanian Trial 8 ~ Secret Area - Mudokon 4",
        "Scrabanian Trial 8 ~ Secret Area - Mudokon 5",
        "Scrabanian Trial 8 ~ Secret Area - Mudokon 6",
        ]
    ))
    
def create_zulag1_locations(world: NNTWorld) -> None:
    zulag1 = world.get_region("Zulag 1")
    zulag1Grinder = world.get_region("Zulag 1 (Grinder Tutorial)")
    zulag1Shadow = world.get_region("Zulag 1 (Shadow Tutorial)")
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
    
    zulag1EntranceMuds = get_location_names_with_ids(
        [
        "Zulag 1 ~ Entrance - Mudokon 1",
        "Zulag 1 ~ Entrance - Mudokon 2",
        "Zulag 1 ~ Entrance - Mudokon 3",
        ]
    )
    zulag1ShadowMuds = get_location_names_with_ids(
        [
        "Zulag 1 ~ Shadow Tutorial - Mudokon 1",
        "Zulag 1 ~ Shadow Tutorial - Mudokon 2",
        "Zulag 1 ~ Shadow Tutorial - Mudokon 3",
        "Zulag 1 ~ Shadow Tutorial - Mudokon 4",
        ]
    )
    zulag1ShrykullMuds = get_location_names_with_ids(
        [
        "Zulag 1 ~ Shrykull Portal Tutorial - Mudokon 1",
        "Zulag 1 ~ Shrykull Portal Tutorial - Mudokon 2",
        "Zulag 1 ~ Shrykull Portal Tutorial - Mudokon 3",
        "Zulag 1 ~ Shrykull Portal Tutorial - Mudokon 4",
        "Zulag 1 ~ Shrykull Portal Tutorial - Mudokon 5",
        "Zulag 1 ~ Shrykull Portal Tutorial - Mudokon 6",
        ]
    )
    zulag1S1Muds = get_location_names_with_ids(
        [
        "Zulag 1 ~ Secret Area 1 - Mudokon 1",
        "Zulag 1 ~ Secret Area 1 - Mudokon 2",
        "Zulag 1 ~ Secret Area 1 - Mudokon 3",
        "Zulag 1 ~ Secret Area 1 - Mudokon 4",
        "Zulag 1 ~ Secret Area 1 - Mudokon 5",
        "Zulag 1 ~ Secret Area 1 - Mudokon 6",
        ]
    )
    zulag1GameSpeakMuds = get_location_names_with_ids(
        [
        "Zulag 1 ~ GameSpeak Tutorial - Mudokon 1",
        "Zulag 1 ~ GameSpeak Tutorial - Mudokon 2",
        "Zulag 1 ~ GameSpeak Tutorial - Mudokon 3",
        "Zulag 1 ~ GameSpeak Tutorial - Mudokon 4",
        "Zulag 1 ~ GameSpeak Tutorial - Mudokon 5",
        "Zulag 1 ~ GameSpeak Tutorial - Mudokon 6",
        "Zulag 1 ~ GameSpeak Tutorial - Mudokon 7",
        ]
    )
    zulag1InteractablesMuds = get_location_names_with_ids(
        [
        "Zulag 1 ~ Interactables Tutorial - Mudokon 1",
        "Zulag 1 ~ Interactables Tutorial - Mudokon 2",
        "Zulag 1 ~ Interactables Tutorial - Mudokon 3",
        "Zulag 1 ~ Interactables Tutorial - Mudokon 4",
        "Zulag 1 ~ Interactables Tutorial - Mudokon 5",
        ]
    )
    zulag1S2Muds = get_location_names_with_ids(
        [
        "Zulag 1 ~ Secret Area 2 - Mudokon 1",
        "Zulag 1 ~ Secret Area 2 - Mudokon 2",
        "Zulag 1 ~ Secret Area 2 - Mudokon 3",
        "Zulag 1 ~ Secret Area 2 - Mudokon 4",
        "Zulag 1 ~ Secret Area 2 - Mudokon 5",
        "Zulag 1 ~ Secret Area 2 - Mudokon 6",
        "Zulag 1 ~ Secret Area 2 - Mudokon 7",
        "Zulag 1 ~ Secret Area 2 - Mudokon 8",
        ]
    )
    zulag1S3Muds = get_location_names_with_ids(
        [
        "Zulag 1 ~ Secret Area 3 - Mudokon 1",
        "Zulag 1 ~ Secret Area 3 - Mudokon 2",
        "Zulag 1 ~ Secret Area 3 - Mudokon 3",
        "Zulag 1 ~ Secret Area 3 - Mudokon 4",
        "Zulag 1 ~ Secret Area 3 - Mudokon 5",
        "Zulag 1 ~ Secret Area 3 - Mudokon 6",
        "Zulag 1 ~ Secret Area 3 - Mudokon 7",
        "Zulag 1 ~ Secret Area 3 - Mudokon 8",
        ]
    )
    zulag1S4Muds = get_location_names_with_ids(
        [
        "Zulag 1 ~ Secret Area 4 - Mudokon 1",
        "Zulag 1 ~ Secret Area 4 - Mudokon 2",
        "Zulag 1 ~ Secret Area 4 - Mudokon 3",
        "Zulag 1 ~ Secret Area 4 - Mudokon 4",
        ]
    )
    zulag1BacktrackMuds = get_location_names_with_ids(
        [
        "Zulag 1 ~ Backtrack End - Mudokon 1",
        "Zulag 1 ~ Backtrack End - Mudokon 2",
        "Zulag 1 ~ Backtrack End - Mudokon 3",
        "Zulag 1 ~ Backtrack End - Mudokon 4",
        "Zulag 1 ~ Backtrack End - Mudokon 5",
        "Zulag 1 ~ Backtrack End - Mudokon 6",
        "Zulag 1 ~ Backtrack End - Mudokon 7",
        "Zulag 1 ~ Backtrack End - Mudokon 8",
        "Zulag 1 ~ Backtrack End - Mudokon 9",
        ]
    )
    zulag1S5Muds = get_location_names_with_ids(
        [
        "Zulag 1 ~ Secret Area 5 - Mudokon 1",
        "Zulag 1 ~ Secret Area 5 - Mudokon 2",
        "Zulag 1 ~ Secret Area 5 - Mudokon 3",
        "Zulag 1 ~ Secret Area 5 - Mudokon 4",
        "Zulag 1 ~ Secret Area 5 - Mudokon 5",
        "Zulag 1 ~ Secret Area 5 - Mudokon 6",
        "Zulag 1 ~ Secret Area 5 - Mudokon 7",
        "Zulag 1 ~ Secret Area 5 - Mudokon 8",
        ]
    )
    zulag1Z2AccessMuds = get_location_names_with_ids(
        [
        "Zulag 1 ~ Zulag 2 Access - Mudokon 1",
        "Zulag 1 ~ Zulag 2 Access - Mudokon 2",
        "Zulag 1 ~ Zulag 2 Access - Mudokon 3",
        "Zulag 1 ~ Zulag 2 Access - Mudokon 4",
        ]
    )
    
    zulag1.add_locations(zulag1EntranceMuds, NNTLocation)
    zulag1Grinder.add_locations(get_location_names_with_ids(["Zulag 1 ~ Grinder Tutorial Mudokon"]), NNTLocation)
    zulag1Shadow.add_locations(zulag1ShadowMuds, NNTLocation)
    zulag1Shrykull.add_locations(zulag1ShrykullMuds, NNTLocation)
    zulag1S1.add_locations(zulag1S1Muds, NNTLocation)
    zulag1GameSpeak.add_locations(zulag1GameSpeakMuds, NNTLocation)
    zulag1Interactables.add_locations(zulag1InteractablesMuds, NNTLocation)
    zulag1S2.add_locations(zulag1S2Muds, NNTLocation)
    zulag1S3.add_locations(zulag1S3Muds, NNTLocation)
    zulag1S4.add_locations(zulag1S4Muds, NNTLocation)
    zulag1Backtrack.add_locations(zulag1BacktrackMuds, NNTLocation)
    zulag1S5.add_locations(zulag1S5Muds, NNTLocation)
    zulag1Z2Access.add_locations(zulag1Z2AccessMuds, NNTLocation)
    
def create_zulag2_locations(world: NNTWorld) -> None:
    zulag2Door1 = world.get_region("Zulag 2 (Door 1)")
    zulag2Door1Back = world.get_region("Zulag 2 (Door 1 Back Area)")
    zulag2Door2 = world.get_region("Zulag 2 (Door 2)")
    zulag2Door3 = world.get_region("Zulag 2 (Door 3)")
    
    zulag2Door1Muds = get_location_names_with_ids(
        [
        "Zulag 2 ~ Door 1 - Mudokon 1",
        "Zulag 2 ~ Door 1 - Mudokon 2",
        "Zulag 2 ~ Door 1 - Mudokon 3",
        "Zulag 2 ~ Door 1 - Mudokon 4",
        "Zulag 2 ~ Door 1 - Mudokon 5",
        "Zulag 2 ~ Door 1 - Mudokon 6",
        "Zulag 2 ~ Door 1 - Mudokon 7",
        "Zulag 2 ~ Door 1 - Mudokon 8",
        "Zulag 2 ~ Door 1 - Mudokon 9",
        "Zulag 2 Door 1"
        ]
    )
    
    zulag2Door1BackMuds = get_location_names_with_ids(
        [
        "Zulag 2 ~ Door 1 (Back Area) - Mudokon 1",
        "Zulag 2 ~ Door 1 (Back Area) - Mudokon 2",
        "Zulag 2 ~ Door 1 (Back Area) - Mudokon 3",
        "Zulag 2 ~ Door 1 (Back Area) - Mudokon 4",
        "Zulag 2 ~ Door 1 (Back Area) - Mudokon 5",
        "Zulag 2 ~ Door 1 (Back Area) - Mudokon 6",
        ]
    )
    
    zulag2Door2Muds = get_location_names_with_ids(
        [
        "Zulag 2 ~ Door 2 - Mudokon 1",
        "Zulag 2 ~ Door 2 - Mudokon 2",
        "Zulag 2 ~ Door 2 - Mudokon 3",
        "Zulag 2 ~ Door 2 - Mudokon 4",
        "Zulag 2 ~ Door 2 - Mudokon 5",
        "Zulag 2 Door 2"
        ]
    )
    
    zulag2Door3Muds = get_location_names_with_ids(
        [
        "Zulag 2 ~ Door 3 - Mudokon 1",
        "Zulag 2 ~ Door 3 - Mudokon 2",
        "Zulag 2 ~ Door 3 - Mudokon 3",
        "Zulag 2 ~ Door 3 - Mudokon 4",
        "Zulag 2 ~ Door 3 - Mudokon 5",
        "Zulag 2 ~ Door 3 - Mudokon 6",
        "Zulag 2 ~ Door 3 - Mudokon 7",
        "Zulag 2 ~ Door 3 - Mudokon 8",
        "Zulag 2 ~ Door 3 - Mudokon 9",
        "Zulag 2 Door 3"
        ]
    )
    
    zulag2Door1.add_locations(zulag2Door1Muds, NNTLocation)
    zulag2Door1Back.add_locations(zulag2Door1BackMuds, NNTLocation)
    zulag2Door2.add_locations(zulag2Door2Muds, NNTLocation)
    zulag2Door3.add_locations(zulag2Door3Muds, NNTLocation)
    
def create_zulag3_locations(world: NNTWorld) -> None:
    zulag3Door1 = world.get_region("Zulag 3 (Door 1)")
    zulag3Door1Back = world.get_region("Zulag 3 (Door 1 Back Area)")
    zulag3Door2 = world.get_region("Zulag 3 (Door 2)")
    zulag3Door3 = world.get_region("Zulag 3 (Door 3)")
    zulag3Door3Back = world.get_region("Zulag 3 (Door 3 Back Area)")
    
    zulag3Door1Muds = get_location_names_with_ids(
        [
        "Zulag 3 ~ Door 1 - Mudokon 1",
        "Zulag 3 ~ Door 1 - Mudokon 2",
        "Zulag 3 ~ Door 1 - Mudokon 3",
        "Zulag 3 ~ Door 1 - Mudokon 4",
        "Zulag 3 ~ Door 1 - Mudokon 5",
        "Zulag 3 ~ Door 1 - Mudokon 6",
        "Zulag 3 ~ Door 1 - Mudokon 7",
        "Zulag 3 ~ Door 1 - Mudokon 8",
        "Zulag 3 ~ Door 1 - Mudokon 9",
        "Zulag 3 Door 1"
        ]
    )
    
    zulag3Door1BackMuds = get_location_names_with_ids(
        [
        "Zulag 3 ~ Door 1 (Back Area) - Mudokon 1",
        "Zulag 3 ~ Door 1 (Back Area) - Mudokon 2",
        "Zulag 3 ~ Door 1 (Back Area) - Mudokon 3",
        "Zulag 3 ~ Door 1 (Back Area) - Mudokon 4",
        "Zulag 3 ~ Door 1 (Back Area) - Mudokon 5",
        ]
    )
    
    zulag3Door2Muds = get_location_names_with_ids(
        [
        "Zulag 3 ~ Door 2 - Mudokon 1",
        "Zulag 3 ~ Door 2 - Mudokon 2",
        "Zulag 3 ~ Door 2 - Mudokon 3",
        "Zulag 3 ~ Door 2 - Mudokon 4",
        "Zulag 3 ~ Door 2 - Mudokon 5",
        "Zulag 3 Door 2"
        ]
    )
    
    zulag3Door3Muds = get_location_names_with_ids(
        [
        "Zulag 3 ~ Door 3 - Mudokon 1",
        "Zulag 3 ~ Door 3 - Mudokon 2",
        "Zulag 3 ~ Door 3 - Mudokon 3",
        "Zulag 3 ~ Door 3 - Mudokon 4",
        "Zulag 3 ~ Door 3 - Mudokon 5",
        "Zulag 3 ~ Door 3 - Mudokon 6",
        "Zulag 3 ~ Door 3 - Mudokon 7",
        "Zulag 3 ~ Door 3 - Mudokon 8",
        "Zulag 3 ~ Door 3 - Mudokon 9",
        ]
    )
    
    zulag3Door3BackMuds = get_location_names_with_ids(
        [
        "Zulag 3 ~ Door 3 (Back Area) - Mudokon 1",
        "Zulag 3 ~ Door 3 (Back Area) - Mudokon 2",
        "Zulag 3 ~ Door 3 (Back Area) - Mudokon 3",
        "Zulag 3 ~ Door 3 (Back Area) - Mudokon 4",
        "Zulag 3 ~ Door 3 (Back Area) - Mudokon 5",
        "Zulag 3 ~ Door 3 (Back Area) - Mudokon 6",
        "Zulag 3 ~ Door 3 (Back Area) - Mudokon 7",
        "Zulag 3 ~ Door 3 (Back Area) - Mudokon 8",
        "Zulag 3 Door 3"
        ]
    )
    
    zulag3Door1.add_locations(zulag3Door1Muds, NNTLocation)
    zulag3Door1Back.add_locations(zulag3Door1BackMuds, NNTLocation)
    zulag3Door2.add_locations(zulag3Door2Muds, NNTLocation)
    zulag3Door3.add_locations(zulag3Door3Muds, NNTLocation)
    zulag3Door3Back.add_locations(zulag3Door3BackMuds, NNTLocation)
    
def create_zulag4_locations(world: NNTWorld) -> None:
    zulag4S1 = world.get_region("Zulag 4 (Secret Area 1)")
    zulag4SligPath = world.get_region("Zulag 4 (Slig Path)")
    zulag4SligPathG = world.get_region("Zulag 4 (Slig Path Post Grenades)")
    zulag4S2 = world.get_region("Zulag 4 (Secret Area 2)")
    
    zulag4S1Muds = get_location_names_with_ids(
        [
        "Zulag 4 ~ Secret Area 1 - Mudokon 1",
        "Zulag 4 ~ Secret Area 1 - Mudokon 2",
        "Zulag 4 ~ Secret Area 1 - Mudokon 3",
        ]
    )
    
    zulag4SligPathMuds = get_location_names_with_ids(
        [
        "Zulag 4 ~ Slig Path - Mudokon 1",
        "Zulag 4 ~ Slig Path - Mudokon 2",
        "Zulag 4 ~ Slig Path - Mudokon 3",
        "Zulag 4 ~ Slig Path - Mudokon 4",
        "Zulag 4 ~ Slig Path - Mudokon 5",
        "Zulag 4 ~ Slig Path - Mudokon 6",
        "Zulag 4 ~ Slig Path - Mudokon 7",
        "Zulag 4 ~ Slig Path - Mudokon 8",
        "Zulag 4 ~ Slig Path - Mudokon 9",
        ]
    )
    
    zulag4SligPathGMuds = get_location_names_with_ids(
        [
        "Zulag 4 ~ Slig Path (Post Boom Machine) - Mudokon 1",
        "Zulag 4 ~ Slig Path (Post Boom Machine) - Mudokon 2",
        "Zulag 4 ~ Slig Path (Post Boom Machine) - Mudokon 3",
        "Zulag 4 ~ Slig Path (Post Boom Machine) - Mudokon 4",
        "Zulag 4 ~ Slig Path (Post Boom Machine) - Mudokon 5",
        ]
    )
    
    zulag4S2Muds = get_location_names_with_ids(
        [
        "Zulag 4 ~ Secret Area 2 - Mudokon 1",
        "Zulag 4 ~ Secret Area 2 - Mudokon 2",
        "Zulag 4 ~ Secret Area 2 - Mudokon 3",
        ]
    )
    
    zulag4S1.add_locations(zulag4S1Muds, NNTLocation)
    zulag4SligPath.add_locations(zulag4SligPathMuds, NNTLocation)
    zulag4SligPathG.add_locations(zulag4SligPathGMuds, NNTLocation)
    zulag4S2.add_locations(zulag4S2Muds, NNTLocation)
    
    if world.options.goal == 0:
        boardroom = world.get_region("Boardroom")
        boardroom.add_event("Boardroom - Complete", "Rupture Farms Destroyed", location_type=NNTLocation, item_type=items.NNTItem)
    
    if world.options.goal == 1:
        alf = world.get_region("Alf's Escape")
        alf.add_event("Alf's Escape - Complete", "Alf Rescued", location_type=NNTLocation, item_type=items.NNTItem)
        
def create_areaclear_locations(world: NNTWorld):
    rFarms = world.get_region("Rupture Farms")
    rFarms.add_locations(get_location_names_with_ids(["Rupture Farms - Clear"]), NNTLocation)
    
    stockyards = world.get_region("Stockyards")
    stockyards.add_locations(get_location_names_with_ids(["Stockyard Escape - Clear"]), NNTLocation)
    if (world.options.extra_area_clears == 1): stockyards.add_locations(get_location_names_with_ids(["Stockyard Return - Clear"]), NNTLocation)
    
    if (world.options.extra_area_clears == 1):
        mLines = world.get_region("Monsaic Lines")
        mLines.add_locations(get_location_names_with_ids(["Monsaic Lines - Clear"]), NNTLocation)
        
    if (world.options.extra_area_clears == 1):
        paramonia = world.get_region("Paramonia")
        paramonia.add_locations(get_location_names_with_ids(["Paramonia - Clear"]), NNTLocation)
    
    paramoniaNest = world.get_region("Paramonian Nests")
    paramoniaNest.add_locations(get_location_names_with_ids(["Paramonian Nests - Clear"]), NNTLocation)
    
    if (world.options.extra_area_clears == 1):
        scrabania = world.get_region("Scrabania")
        scrabania.add_locations(get_location_names_with_ids(["Scrabania - Clear"]), NNTLocation)
    
    scrabaniaNest = world.get_region("Scrabanian Nests")
    scrabaniaNest.add_locations(get_location_names_with_ids(["Scrabanian Nests - Clear"]), NNTLocation)
    
    zulag1Z2Access = world.get_region("Zulag 1")
    zulag1Z2Access.add_locations(get_location_names_with_ids(["Zulag 1 - Clear"]), NNTLocation)
    
    zulag2 = world.get_region("Zulag 2")
    zulag2.add_locations(get_location_names_with_ids(["Zulag 2 - Clear"]), NNTLocation)
    
    zulag3 = world.get_region("Zulag 3")
    zulag3.add_locations(get_location_names_with_ids(["Zulag 3 - Clear"]), NNTLocation)
    
    zulag4 = world.get_region("Zulag 4")
    zulag4.add_locations(get_location_names_with_ids(["Zulag 4 - Clear"]), NNTLocation)