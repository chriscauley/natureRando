from can import ALL_SKILLS
from connection_data import VanillaAreas
from game import Game, GameOptions
from loadout import Loadout
from location_data import pullCSV
from item_data import all_items
import logicExpert
from Main import Main, args_to_options

name_by_slug = {
    'bomb': 'Bombs',
    'spring-ball': 'Springball',
    'grappling-beam': 'Grapple Beam',
    'hi-jump-boots': 'HiJump',
    'spazer-beam': 'Spazer',
}

item_by_name = {}
item_by_slug = {}

SKIPS = ['draygon', 'phantoon', 'kraid', 'ridley']

for name, item in all_items.items():
    slug = name.lower().replace(' ', '-')
    name_by_slug[slug] = name
    item_by_name[name] = item
    item_by_slug[slug] = item

def get_logic(slug):
    return logicExpert


def randomize(options):
    return Main(options)


def get_locations(game_options):
    game = Game(
        game_options,
        game_options.logic,
        pullCSV(), # all locations
        False, # area rando
        VanillaAreas(), # connections
    )
    loadout = Loadout(game)
    for slug, quantity in game_options._inventory.items():
        if slug in SKIPS:
            continue
        name = name_by_slug[slug]
        item = item_by_name[name]
        loadout.contents[item] = quantity
    locations = {}
    for name, func in game.logic.location_logic.items():
        locations[name] = func(loadout)
    return locations

def get_schema():
    schema = {
        'type': 'object',
        'required': ['logic', 'can'],
        'properties': {
            'logic': {
                'type': 'string',
                'enum': ['expert'],
                'default': 'expert',
            },
            'can': {
                'type': 'array',
                'default': [],
                'items': {
                    'type': 'string',
                    'enum': list(ALL_SKILLS.keys()),
                    'enumNames': list(ALL_SKILLS.values()),
                }
            }
        }
    }
    return schema


if __name__ == '__main__':
    import json
    import sys
    args = sys.argv[1:]
    options = args_to_options(args)
    print(json.dumps({
        'args': args,
        'locations': get_locations(options),
        'schema': get_schema(),
        'can': options.can,
    }))
