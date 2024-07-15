import colors as c
import random

bioms = {
    'g': {
        'name': 'grass',
        'color': c.c['green'],
        'emoji': '🌱',
        'enemy': False,
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
        'symbol': 's',
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
        'color': c.c['dark_green'],
        'emoji': '🌲',
        'enemy': True,
        'symbol': '*',
    },
    'shop': {
        'name': 'shop',
        'color': c.c['magenta'],
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
        "  __  ",
        " /  \\ ",
        "|    |",
        "|_||_|"
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
        "|_  _|",
        "|    |",
        "|_||_|"
    ]
}
