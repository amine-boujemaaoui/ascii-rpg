import colors as c
import random

bioms = {
    'g': {
        'name': 'grass',
        'color': c.c['green'],
        'emoji': '🌱',
        'enemy': True,
        'symbol': '.',
    },
    'w': {
        'name': 'water',
        'color': c.c['blue'],
        'emoji': '🌊',
        'enemy': False,
        'symbol': '~',
    },
    's': {
        'name': 'sand',
        'color': c.c['yellow'],
        'emoji': '🏖️',
        'enemy': False,
        'symbol': 'S',
    },
    'm': {
        'name': 'mountain',
        'color': c.c['gray'],
        'emoji': '⛰️',
        'enemy': True,
        'symbol': '^',
    },
    'f': {
        'name': 'forest',
        'color': c.c['green'],
        'emoji': '🌲',
        'enemy': True,
        'symbol': '*',
    },
    'shop': {
        'name': 'shop',
        'color': c.c['cyan'],
        'emoji': '🏪',
        'enemy': False,
        'symbol': '$',
    },
    'castle': {
        'name': 'castle',
        'color': c.c['yellow'],
        'emoji': '🏰',
        'enemy': False,
        'symbol': 'C',
    },
    'player': {
        'name': 'player',
        'color': c.c['red'],
        'emoji': '🧑',
        'enemy': False,
        'symbol': 'P',
        
    },
}

ascii_art = {
        'grass': [
            "  ,,,   ",
            " (o o)  ",
            " /_=_\\ ",
            "  / \\  "
        ],
        'water': [
            "  ~~~  ",
            " ~~~~~ ",
            " ~~~~~ ",
            "  ~~~  "
        ],
        'sand': [
            "  ...  ",
            " ..... ",
            " ..... ",
            "  ...  "
        ],
        'mountain': [
            "  /\\  ",
            " /  \\ ",
            "/____\\",
            "       "
        ],
        'forest': [
            "   f   ",
            "  fff  ",
            " fffff ",
            "   f   "
        ],
        'shop': [
            "._____.",
            "|  _  |",
            "|  $  |",
            "|_____|"
        ],
        'castle': [
            "  / \  ",
            " /   \ ",
            "|  C  |",
            "|_____|"
        ],
    }

def generate_map(width=38, height=22):
    biomes_keys = list(bioms.keys())
    biomes_keys.remove('player')
    generated_map = [[random.choice(biomes_keys) for _ in range(width)] for _ in range(height)]
    return generated_map


map = generate_map()
