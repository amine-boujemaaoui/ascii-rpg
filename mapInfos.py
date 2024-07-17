import colors as c
import random

bioms = {
    'g': {
        'name': 'grass',
        'color': c.c['gray'],
        'emoji': '🌱',
        'enemy': False,
        'symbol': '.',
        'solid': False,
    },
    'w': {
        'name': 'water',
        'color': c.c['blue'],
        'emoji': '🌊',
        'enemy': False,
        'symbol': '~',
        'solid': True,
    },
    's': {
        'name': 'sand',
        'color': c.c['yellow'],
        'emoji': '🏖️',
        'enemy': False,
        'symbol': 's',
        'solid': False,
    },
    'm': {
        'name': 'mountain',
        'color': c.c['light_gray'],
        'emoji': '⛰️',
        'enemy': True,
        'symbol': '^',
        'solid': False,
    },
    'f': {
        'name': 'forest',
        'color': c.c['dark_green'],
        'emoji': '🌲',
        'enemy': True,
        'symbol': '*',
        'solid': False,
    },
    'shop': {
        'name': 'shop',
        'color': c.c['magenta'],
        'emoji': '🏪',
        'enemy': False,
        'symbol': '$',
        'solid': False,
    },
    'castle': {
        'name': 'castle',
        'color': c.c['yellow'],
        'emoji': '🏰',
        'enemy': False,
        'symbol': 'C',
        'solid': False,
    },
    'player': {
        'name': 'player',
        'color': c.c['red'],
        'emoji': '🧑',
        'enemy': False,
        'symbol': 'P',
        'solid': False,
    },
}

ascii_art = {
    'grass': [
        "  __   ",
        " /  \  ",
        "|    | ",
        "|_||_| "
    ],
    'water': [
        " ~ ~ ~ ",
        "~ ~ ~ ~",
        " ~ ~ ~ ",
        "~ ~ ~ ~"
    ],
    'sand': [
        " ..... ",
        ": : : :",
        " ..... ",
        ": : : :"
    ],
    'mountain': [
        "  /\\  ",
        " /  \\ ",
        "/ /\\ \\",
        "/____\\"
    ],
    'forest': [
        "  |||  ",
        " ||||| ",
        "|||||||",
        "  |||  "
    ],
    'shop': [
        " _____ ",
        "|[---]|",
        "|  |  |",
        "|__|__|"
    ],
    'castle': [
        "|¯¯|¯¯|",
        "|_   _|",
        "|  _  |",
        "|_| |_|"
    ]
}
