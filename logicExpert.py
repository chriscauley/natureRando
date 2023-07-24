from typing import ClassVar

from connection_data import area_doors_unpackable
from door_logic import canOpen
from item_data import items_unpackable, Items
from loadout import Loadout
from logicInterface import AreaLogicType, LocationLogicType, LogicInterface
from logic_shortcut import LogicShortcut

# TODO: There are a bunch of places where where Expert logic needed energy tanks even if they had Varia suit.
# Need to make sure everything is right in those places.
# (They will probably work right when they're combined like this,
#  but they wouldn't have worked right when casual was separated from expert.)

# TODO: There are also a bunch of places where casual used icePod, where expert only used Ice. Is that right?

(
    CraterR, SunkenNestL, RuinedConcourseBL, RuinedConcourseTR, CausewayR,
    SporeFieldTR, SporeFieldBR, OceanShoreR, EleToTurbidPassageR, PileAnchorL,
    ExcavationSiteL, WestCorridorR, FoyerR, ConstructionSiteL, AlluringCenoteR,
    FieldAccessL, TransferStationR, CellarR, SubbasementFissureL,
    WestTerminalAccessL, MezzanineConcourseL, VulnarCanyonL, CanyonPassageR,
    ElevatorToCondenserL, LoadingDockSecurityAreaL, ElevatorToWellspringL,
    NorakBrookL, NorakPerimeterTR, NorakPerimeterBL, VulnarDepthsElevatorEL,
    VulnarDepthsElevatorER, HiveBurrowL, SequesteredInfernoL,
    CollapsedPassageR, MagmaPumpL, ReservoirMaintenanceTunnelR, IntakePumpR,
    ThermalReservoir1R, GeneratorAccessTunnelL, ElevatorToMagmaLakeR,
    MagmaPumpAccessR, FieryGalleryL, RagingPitL, HollowChamberR, PlacidPoolR,
    SporousNookL, RockyRidgeTrailL, TramToSuziIslandR
) = area_doors_unpackable

(
    Missile, Super, PowerBomb, Morph, Springball, Bombs, HiJump,
    GravitySuit, Varia, Wave, SpeedBooster, Spazer, Ice, Grapple,
    Plasma, Screw, Charge, SpaceJump, Energy, Reserve, Burst
) = items_unpackable

energy200 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) + loadout.count(Items.Reserve) >= 1
))

energy300 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) + loadout.count(Items.Reserve) >= 2
))
energy400 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) + loadout.count(Items.Reserve) >= 3
))
energy500 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) + loadout.count(Items.Reserve) >= 4
))
energy600 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) + loadout.count(Items.Reserve) >= 5
))
energy700 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) + loadout.count(Items.Reserve) >= 6
))
energy900 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) + loadout.count(Items.Reserve) >= 8
))
energy1000 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) + loadout.count(Items.Reserve) >= 9
))
energy1200 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) + loadout.count(Items.Reserve) >= 11
))
energy1500 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Energy) + loadout.count(Items.Reserve) >= 14
))


hellrun1 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy200 in loadout)
))
hellrun2 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy300 in loadout)
))
hellrun3 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy400 in loadout)
))
hellrun4 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy500 in loadout)
))
hellrun5 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy600 in loadout)
))
hellrun6 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy700 in loadout)
))
hellrun8 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy900 in loadout)
))
hellrun9 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy1000 in loadout)
))
hellrun11 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy1200 in loadout)
))
hellrun14 = LogicShortcut(lambda loadout: (
    (Varia in loadout) or
    (energy1500 in loadout)
))

missile10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 10
))
missile15 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Missile) * 5 >= 15
))
super10 = LogicShortcut(lambda loadout: (
    loadout.count(Items.Super) * 3 >= 10
))
powerBomb4 = LogicShortcut(lambda loadout: (
    loadout.count(Items.PowerBomb) * 2 >= 4
))
powerBomb8 = LogicShortcut(lambda loadout: (
    loadout.count(Items.PowerBomb) * 2 >= 8
))
powerBomb15 = LogicShortcut(lambda loadout: (
    loadout.count(Items.PowerBomb) * 2 >= 15
))
pinkDoor = LogicShortcut(lambda loadout: (
    (Missile in loadout) or
    (Super in loadout)
))
canUseBombs = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    ((Bombs in loadout) or (PowerBomb in loadout))
))
canUsePB = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (PowerBomb in loadout)
))
canIBJ = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Bombs in loadout)
))
canBreakBlocks = LogicShortcut(lambda loadout: (
    #with bombs or screw attack, maybe without morph
    (canUseBombs in loadout) or
    (Screw in loadout)
))
norfair = LogicShortcut(lambda loadout: (
    (inBrinstar in loadout) and
    (pinkDoor in loadout) #can get to kraid with just PBs
))
shipFront = LogicShortcut(lambda loadout: (
    (canUsePB in loadout) and
    (
        (pinkDoor in loadout) or
        (
            (
                (SpaceJump in loadout) or
                (canIBJ in loadout) or
                (Ice in loadout)
                ) and
            (
                (HiJump in loadout) or
                (GravitySuit in loadout)
                )
            )
        )   
))
inBrinstar = LogicShortcut(lambda loadout: (
    (canUsePB in loadout) and
    (
        (Wave in loadout) or
        (pinkDoor in loadout) or
        (shipFront in loadout)
        )
))
hotNorfair = LogicShortcut(lambda loadout: (
    (inBrinstar in loadout) and
    (pinkDoor in loadout) and
    (Varia in loadout)
))
beatGT = LogicShortcut(lambda loadout: (
    (hotNorfair in loadout) and
    (Super in loadout) and
    (Charge in loadout)
))
maridia = LogicShortcut(lambda loadout: (
    (inBrinstar in loadout) and 
    (
        (SpaceJump in loadout) or
        (Ice in loadout) or
        (canIBJ in loadout) or
        (Springball in loadout)
        ) #this gets you to the tube
))
innerMaridia = LogicShortcut(lambda loadout: (
    (maridia in loadout) and
    (
        (
            (GravitySuit in loadout) and
                (
                    (SpeedBooster in loadout) and
                    (SpaceJump in loadout)
                    ) or
                (Super in loadout)
                ) or
        (
            (   #Suitless
                (HiJump in loadout) and
                (Springball in loadout) and
                (Super in loadout) and
                (Wave in loadout)
                )
            )
        )
))
midMaridia = LogicShortcut(lambda loadout: (
    (maridia in loadout) and
    (
        (GravitySuit in loadout) or
        (   #Suitless
            (HiJump in loadout) and
            (Springball in loadout) and
            (Super in loadout)
            )
        )
))
draygon = LogicShortcut(lambda loadout: (
    #to reach draygon
    (innerMaridia in loadout) and
    (Super in loadout) and
    (Wave in loadout) and
    (
        (GravitySuit in loadout) or
        (Ice in loadout)
        )
))
defeatDraygon = LogicShortcut(lambda loadout: (
    (draygon in loadout) and
    (energy300 in loadout) and
    (
        (Missile in loadout) or
        (Charge in loadout) or
        (Grapple in loadout) or
        (
            (GravitySuit in loadout) and
            (SpeedBooster in loadout)
            )
        )
))
# This is complicated. Going to leave it disabled for now
# might add it back in as a challenge setting
canStoreShinespark = LogicShortcut(lambda loadout: False)

canSBJ = LogicShortcut(lambda loadout: (
    (Morph in loadout) and
    (Springball in loadout)
))

waterJump6 = LogicShortcut(lambda loadout: (
    (GravitySuit in loadout) or
    (HiJump in loadout) or
    (canSBJ in loadout) or
    (canStoreShinespark in loadout)
))
phantoon = LogicShortcut(lambda loadout: (
    (inBrinstar in loadout) and
    (Missile in loadout) and
    (Super in loadout)  and
    (
        (waterJump6 in loadout) or
        (Ice in loadout) # freeze covern
    )
))
bowling = LogicShortcut(lambda loadout: (
    (phantoon in loadout) and
    (
        (Grapple in loadout) or
        (energy200 in loadout)
        ) and
    (
        (canIBJ in loadout) or
        (SpaceJump in loadout) or
        (Grapple in loadout) or
        (SpeedBooster in loadout)
        )
))
crocBlocks = LogicShortcut(lambda loadout: (
    (norfair in loadout) and
    (hellrun1 in loadout) and
    (
        (SpeedBooster in loadout) or
        (Grapple in loadout)
        )
))
croc = LogicShortcut(lambda loadout: (
    (crocBlocks in loadout) and
    (hellrun4 in loadout) and
    (
        (missile10 in loadout) or
        (Charge in loadout)
        )
))

area_logic: AreaLogicType = {
    "Early": {
        # using SunkenNestL as the hub for this area, so we don't need a path from every door to every other door
        # just need at least a path with sunken nest to and from every other door in the area
        ("CraterR", "SunkenNestL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "CraterR"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseBL"): lambda loadout: (
            True
        ),
        ("SunkenNestL", "RuinedConcourseTR"): lambda loadout: (
            True
            # TODO: Expert needs energy and casual doesn't? And Casual can do it with supers, but expert can't?
        ),   
    },
}


location_logic: LocationLogicType = {
    "Morph Ball": lambda loadout: (
        True
    ),
    "Ceiling Energy Tank": lambda loadout: (
        True
    ),
    "Alpha Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Beta Missile": lambda loadout: (
        (Morph in loadout)
    ),
    "Meme Route Energy": lambda loadout: (
        (SpeedBooster in loadout) or
        (
            (pinkDoor in loadout) and
            (canUsePB in loadout)
            )
    ),
    "Right of Ship Missile": lambda loadout: (
        (canUseBombs in loadout) and
        (shipFront in loadout)
    ),
    "Parlor Fleas": lambda loadout: (
        (pinkDoor in loadout)
    ),
    "Lower Parlor Chozo": lambda loadout: (
        (canIBJ in loadout) or
        (HiJump in loadout) or
        (SpaceJump in loadout) or
        (Ice in loadout) or
        (
            (Morph in loadout) and
            (Springball in loadout)
            )
    ),
    "Bomb Torizo": lambda loadout: (
        (pinkDoor in loadout) or
        (shipFront in loadout)
    ),
    "Across from Bomb Torizo": lambda loadout: (
        (pinkDoor in loadout) or
        (shipFront in loadout)
    ),
    "Crater Super": lambda loadout: (
        (canIBJ in loadout) or
        (SpaceJump in loadout) or
        (SpeedBooster in loadout)
    ),
    "Mushroom Top Missile": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Mushroom Top Energy Tank": lambda loadout: (
        (canUseBombs in loadout) and
        (SpeedBooster in loadout)
    ),
    "Mushroom Middle Missile": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Mushroom Bottom Missile": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Green Right Missile": lambda loadout: (
        (canUseBombs in loadout) and
        (pinkDoor in loadout)
    ),
    "Green Left Missile": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Green Main Energy": lambda loadout: (
        (canUseBombs in loadout)
    ),
    "Pink Top Missile": lambda loadout: (
        (
            (pinkDoor in loadout) and
            (canUseBombs in loadout)
            ) or
        (canUsePB in loadout)
    ),
    "Pink PB Cell Super": lambda loadout: (
        (canUsePB in loadout)
    ),
    "Brinstar Reserve": lambda loadout: (
        (inBrinstar in loadout) and
        (pinkDoor in loadout)
    ),
    "Springball": lambda loadout: (
        (inBrinstar in loadout)
    ),
    "Dachora Energy": lambda loadout: (
        (inBrinstar in loadout) and
        (pinkDoor in loadout) and
        (SpeedBooster in loadout)
    ),
    "Spore Open Energy": lambda loadout: (
        (inBrinstar in loadout) and
        (pinkDoor in loadout)
    ),
    "Spore Ceiling Chozo": lambda loadout: (
        (inBrinstar in loadout) and
        (
            (SpaceJump in loadout) or
            (canIBJ in loadout)
            )
    ),

    "Charge Beam": lambda loadout: (
        (canUsePB in loadout)
    ),
    "Charge Missile": lambda loadout: (
        (canUsePB in loadout) and
        (SpeedBooster in loadout)
    ),
    "Top Red Tower": lambda loadout: (
        (inBrinstar in loadout)
    ),
    "Red Entry Hidden": lambda loadout: (
        (inBrinstar in loadout)
    ),
    "Pink-Red Power Bomb": lambda loadout: (
        (inBrinstar in loadout)
    ),
    "Pink Lowest Missile": lambda loadout: (
        (inBrinstar in loadout) and
        (pinkDoor in loadout)
    ),
    "Pink Speed Super": lambda loadout: (
        (inBrinstar in loadout) and
        (SpeedBooster in loadout)
    ),
    "Pink Z Missile": lambda loadout: (
        (inBrinstar in loadout)
    ),
    "Red Crumble Missile": lambda loadout: (
        (inBrinstar in loadout)
    ),
    "Kraid Energy Tank": lambda loadout: (
        (inBrinstar in loadout) and
        (Super in loadout)
    ),
    "Kraid Super Blocks Super": lambda loadout: (
        (inBrinstar in loadout) and
        (Super in loadout)
    ),
    "Varia Suit": lambda loadout: (
        (inBrinstar in loadout) and
        (   #can get to kraid with just PBs
            (Missile in loadout) or
            (Charge in loadout)
            )
    ),
    "Spore Spawn Super": lambda loadout: (
        (inBrinstar in loadout) and
        (Super in loadout)
    ),
    "Spore Spawn Top Missile": lambda loadout: (
        (inBrinstar in loadout) and
        (pinkDoor in loadout)
    ),
    "Red Gates Missile": lambda loadout: (
        (inBrinstar in loadout) and
        (
            (pinkDoor in loadout) or
            (Springball in loadout) or
            (Ice in loadout) or
            (SpaceJump in loadout) or
            (HiJump in loadout)
            )
    ),
    "Red Gates Power Bomb": lambda loadout: (
        (inBrinstar in loadout) and
        (
            (pinkDoor in loadout) or
            (Springball in loadout) or
            (Ice in loadout) or
            (SpaceJump in loadout) or
            (HiJump in loadout)
            )
    ),
    "Red Crumble Power Bomb": lambda loadout: (
        (inBrinstar in loadout) and
        (
            (pinkDoor in loadout) or
            (Springball in loadout) or
            (Ice in loadout) or
            (SpaceJump in loadout) or
            (HiJump in loadout)
            )
    ),
    "Low Maridia Tunnel Missile": lambda loadout: (
        (inBrinstar in loadout) and
        (SpeedBooster in loadout) and
        (
            (pinkDoor in loadout) or
            (Springball in loadout) or
            (Ice in loadout) or
            (SpaceJump in loadout) or
            (HiJump in loadout)
            )
    ),
    "Norfair Entry Crumble Missile": lambda loadout: (
        (norfair in loadout) and
        (hellrun2 in loadout)
    ),
    "Bubble Mountain Entry Rippers Missile": lambda loadout: (
        (norfair in loadout) and
        (hellrun5 in loadout)
    ),
    "Bubble Mountain Missile": lambda loadout: (
        (norfair in loadout) and
        (hellrun4 in loadout)
    ),
    "Bubble Mountain Super": lambda loadout: (
        (norfair in loadout) and
        (hellrun6 in loadout)
    ),
    "Speed Booster": lambda loadout: (
        (norfair in loadout) and
        (hellrun9 in loadout)
    ),
    "Speed Power Bomb": lambda loadout: (
        (norfair in loadout) and
        (hellrun9 in loadout)
    ),
    "Burst Beam": lambda loadout: (
        (norfair in loadout) and
        (hellrun14 in loadout)
    ),
    "Ripper Cavern Missile": lambda loadout: (
        (norfair in loadout) and
        (
            (
                (hellrun11 in loadout) and
                (powerBomb8 in loadout)
                ) or
            (
                (hellrun5 in loadout) and
                (Grapple in loadout) and
                (powerBomb4 in loadout)
                ) or
            (
                (hellrun5 in loadout) and
                (SpeedBooster in loadout)
                )
            ) and
        (
            (Grapple in loadout) or
            (SpaceJump in loadout)
            )
    ),
    "Croc Speed Crumble Missile": lambda loadout: (
        (crocBlocks in loadout) and
        (SpeedBooster in loadout) and
        (
            (HiJump in loadout) or
            (SpaceJump in loadout) or
            (
                (Varia in loadout) and
                (canIBJ in loadout)
                )
            ) and
        (hellrun6 in loadout)
    ),
    "Croc Power Bomb": lambda loadout: (
        (croc in loadout)
    ),
    "Spazer": lambda loadout: (
        (croc in loadout)
    ),
    "Croc Right Missile": lambda loadout: (
        (crocBlocks in loadout)
    ),
    "LN Entry Power Bomb": lambda loadout: (
        (hotNorfair in loadout) and
        (
            (canIBJ in loadout) or
            (SpaceJump in loadout)
            )
    ),
    "LN Super": lambda loadout: (
        (hotNorfair in loadout) and
        (Super in loadout)
    ),
    "GT Missile": lambda loadout: (
        (beatGT in loadout)
    ),
    "GT Power Bomb": lambda loadout: (
        (hotNorfair in loadout) and
        (Super in loadout)
    ),
    "Screw Attack": lambda loadout: (
        (beatGT in loadout)
    ),
    "LN Fireflea Missile": lambda loadout: (
        (beatGT in loadout)
    ),
    "Norfair Reserve": lambda loadout: (
        (hotNorfair in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout)
    ),
    "LN Escape Lava Missile": lambda loadout: (
        (hotNorfair in loadout) and
        (GravitySuit in loadout)
    ),
    "LN Escape Acid Missile": lambda loadout: (
        (hotNorfair in loadout) and
        (GravitySuit in loadout) and
        (energy300 in loadout)
    ),
    "Ampitheater Missile": lambda loadout: (
        (beatGT in loadout)
    ),
    "HiJump Energy": lambda loadout: (
        (inBrinstar in loadout) and
        (SpeedBooster in loadout)
    ),
    "HiJump": lambda loadout: (
        (inBrinstar in loadout)
    ),
    "Mama Turtle Energy Tank": lambda loadout: (
        (maridia in loadout) and
        (
            (GravitySuit in loadout) or
            (Springball in loadout)
            )
    ),
    "Mama Turtle Missile": lambda loadout: (
        (maridia in loadout) and
        (GravitySuit in loadout) #possible to PB and grav jump
    ),
    "Maridia Above Phony Chozo Missile": lambda loadout: (
        (midMaridia in loadout) #multi springball jump
    ),
    "Maridia Phony Chozo Missile": lambda loadout: (
        (midMaridia in loadout)
    ),
    "Plasma Speed Missile": lambda loadout: (
        (innerMaridia in loadout) and
        (SpeedBooster in loadout) and
        (GravitySuit in loadout)
    ),
    "Plasma Power Bomb": lambda loadout: (
        (innerMaridia in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout)
    ),
    "Wave Beam": lambda loadout: (
        (innerMaridia in loadout) and
        (GravitySuit in loadout) and
        (Charge in loadout) and
        (SpeedBooster in loadout) and
        (Super in loadout)
    ),
    "Mirror Energy": lambda loadout: (
        (innerMaridia in loadout) and
        (Super in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout)
    ),
    "Botwoon Escape Missile": lambda loadout: (
        (innerMaridia in loadout) and
        (GravitySuit in loadout) and
        (SpeedBooster in loadout) and
        (
            (HiJump in loadout) or
            (SpaceJump in loadout) or
            (Ice in loadout)
            )
    ),
    "After Draygon Missile": lambda loadout: (
        (innerMaridia in loadout)
    ),
    "Above Draygon Energy": lambda loadout: (
        (draygon in loadout)
    ),
    "Maridia Reserve": lambda loadout: (
        (draygon in loadout) and
        (energy300 in loadout) and
        (
            (Charge in loadout) or
            (Grapple in loadout)
            )
    ),
    "Space Jump Energy": lambda loadout: (
        (maridia in loadout) and
        (GravitySuit in loadout) and
        (
            (SpaceJump in loadout) or
            (energy300 in loadout)
            )
    ),
    "Space Jump": lambda loadout: (
        (maridia in loadout) and
        (
            (
                (GravitySuit in loadout) and
                (SpaceJump in loadout) or
                    (
                        (Grapple in loadout) and
                        (Super in loadout)
                        )
                    ) or
            (
                (HiJump in loadout) and
                (Grapple in loadout) and
                (Super in loadout) #infinite sbj option?
                )
            )
    ),
    "Low Maridia Dead End Missile": lambda loadout: (
        (midMaridia in loadout)
    ),
    "Plasma Beam": lambda loadout: (
        (draygon in loadout) and
        (
            (Plasma in loadout) or
            (
                (Charge in loadout) and
                (energy400 in loadout)
                )
            ) and
        (
            (SpaceJump in loadout) or
            (canIBJ in loadout)
            )
    ),
    "Plasma Missile": lambda loadout: (
        (innerMaridia in loadout) and
        (
            (Plasma in loadout) or
            (
                (Charge in loadout) and
                (energy400 in loadout)
                )
            )
    ),
    "Forgotten Highway Super": lambda loadout: (
        (midMaridia in loadout) and
        (Ice in loadout)
    ),
    "WS Speedball Missile": lambda loadout: (
        (GravitySuit in loadout) and
        (SpeedBooster in loadout) and
        (
            (midMaridia in loadout) or
            (phantoon in loadout)
            )
    ),
    "Wrecked Ship Speed Super": lambda loadout: (
        (canUsePB in loadout) and
        (Super in loadout) and
        (SpeedBooster in loadout)
    ),
    "Wrecked Ship Reserve": lambda loadout: (
        (phantoon in loadout) and
        (Grapple in loadout)
    ),
    "Moat Missile": lambda loadout: (
        (shipFront in loadout) and
        (
            (canIBJ in loadout) or
            (SpaceJump in loadout) or
            (Grapple in loadout) or
            (SpeedBooster in loadout)
            )
    ),
    "Wrecked Ship Right Super": lambda loadout: (
        (bowling in loadout)
    ),
    "WS Power Bomb": lambda loadout: (
        (GravitySuit in loadout) and
        (SpeedBooster in loadout) and
        (bowling in loadout)
    ),
    "Gravity Suit": lambda loadout: (
        (bowling in loadout)
    ),
    "Moat Power Bomb": lambda loadout: (
        (shipFront in loadout) and
        (SpeedBooster in loadout)
    ),
    "Spark Across Moat Energy": lambda loadout: (
        (shipFront in loadout) and
        (SpeedBooster in loadout)
    ),
    "Ice Beam": lambda loadout: (
        (inBrinstar in loadout) and
        (hellrun6 in loadout) and
        (Super in loadout)
    ),
    "Ice Missile": lambda loadout: (
        (inBrinstar in loadout) and
        (hellrun6 in loadout) and
        (Super in loadout) and
        (
            (SpaceJump in loadout) or
            (canIBJ in loadout) or
            (Ice in loadout)
            )
    ),
    "Grapple Beam": lambda loadout: (
        (crocBlocks in loadout) and
        (
            (
                (hellrun4 in loadout) and
                (
                    (HiJump in loadout) or
                    (Grapple in loadout) or
                    (SpaceJump in loadout)
                    )
                ) or
            (
                (Varia in loadout) and
                (canIBJ in loadout)
                )
            )
    ),
    "Croc Speed Wall Missile": lambda loadout: (
        (crocBlocks in loadout) and
        (SpeedBooster in loadout) and
        (hellrun2 in loadout)
    ),
    "Precious Missile": lambda loadout: (
        (innerMaridia in loadout) and
        (GravitySuit in loadout) and
        (Wave in loadout) and
        (SpeedBooster in loadout)
    ),
    "Coliseum Missile": lambda loadout: (
        (innerMaridia in loadout) and
        (Wave in loadout) and
        (
            (GravitySuit in loadout) or
            (Ice in loadout)
            )
    ),

}


class Expert(LogicInterface):
    area_logic: ClassVar[AreaLogicType] = area_logic
    location_logic: ClassVar[LocationLogicType] = location_logic

    @staticmethod
    def can_fall_from_spaceport(loadout: Loadout) -> bool:
        return True
