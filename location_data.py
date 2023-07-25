import csv
from typing import Optional, TypedDict, cast

from item_data import Item
import os

# other unused columns in Location:
# "roomid", "area", "xy","plmtypename","state","roomname","alternateroomid"
class Location(TypedDict):
    fullitemname: str
    locids: list[int]
    plmtypeid: int
    plmparamhi: int
    plmparamlo: int
    hiddenness: str
    alternateroomlocids: list[int]
    alternateroomdifferenthiddenness: str
    inlogic: bool
    item: Optional[Item]


spacePortLocs = ["Ready Room",
                 "Torpedo Bay",
                 "Extract Storage",
                 "Gantry",
                 "Docking Port 4",
                 "Docking Port 3",
                 "Weapon Locker",
                 "Aft Battery",
                 "Forward Battery"]

majorLocs = frozenset([
    "Morph Ball",
    "Ceiling Energy Tank",
    "Meme Route Energy",
    "Bomb Torizo",
    "Across from Bomb Torizo",
    "Mushroom Top Energy Tank",
    "Green Main Energy",
    "Brinstar Reserve",
    "Springball",
    "Dachora Energy",
    "Spore Open Energy",
    "Charge Beam",
    "Kraid Energy Tank",
    "Varia Suit",
    "Speed Booster",
    "Burst Beam",
    "Spazer",
    "Screw Attack",
    "Norfair Reserve",
    "HiJump Energy",
    "HiJump",
    "Mama Turtle Energy Tank",
    "Wave Beam",
    "Mirror Energy",
    "Above Draygon Energy",
    "Maridia Reserve",
    "Space Jump Energy",
    "Space Jump",
    "Plasma Beam",
    "Wrecked Ship Reserve",
    "Gravity Suit",
    "Spark Across Moat Energy",
    "Ice Beam",
    "Grapple Beam",
])


def pullCSV() -> dict[str, Location]:
    csvdict: dict[str, Location] = {}

    def commentfilter(line: str) -> bool:
        return (line[0] != '#')

    dir_path = os.path.dirname(os.path.realpath(__file__))
    nature_csv = os.path.join(dir_path, 'nature.csv')
    with open(nature_csv, 'r') as csvfile:
        reader = csv.DictReader(filter(commentfilter, csvfile))
        for row in reader:
            # commas within fields -> array
            row['locids'] = row['locids'].split(',')
            row['alternateroomlocids'] = row['alternateroomlocids'].split(',')
            # hex fields we want to use -> int
            row['locids'] = [int(locstr, 16)
                             for locstr in row['locids'] if locstr != '']
            row['alternateroomlocids'] = [
                int(locstr, 16) for locstr in row['alternateroomlocids'] if locstr != '']
            row['plmtypeid'] = int(row['plmtypeid'], 16)
            row['plmparamhi'] = int(row['plmparamhi'], 16)
            row['plmparamlo'] = int(row['plmparamlo'], 16)
            # new key: 'inlogic'
            row['inlogic'] = False
            # the item that we place in this location
            row["item"] = None
            csvdict[row['fullitemname']] = cast(Location, row)
    return csvdict
