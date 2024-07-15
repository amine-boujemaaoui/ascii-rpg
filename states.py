import enemies as en

gs = {
    'map': 'null',
    'player': {
        'name': '',
        'stats': {
            'hp': 100,
            'max_hp': 100,
            'attack': 10,
            'defense': 10,
            'speed': 10,
            'level': 1,
            'exp': 0,
            'next_lvl_exp': en.exp_table.get(1),
            'gold': 0,
        },
        'equipment': {
            'weapons': 'fists',
            'armor': 'none',
            'potions': [
                {
                    'name': 'healing',
                    'amount': 2,
                },
                {
                    'name': 'mana',
                    'amount': 2,
                },
            ]
        },
        'inventory': [
            {
                'type': 'weapon',
                'name': 'sword',
                'attack': 10,
            },
            {
                'type': 'weapon',
                'name': 'axe',
                'attack': 15,
            },
            {
                'type': 'armor',
                'name': 'leather',
                'defense': 10,
            }
        ],
        'pos': {
            'x': 0,
            'y': 0,
        }
    },
    'menu': False,
    'rules': False,
    'play': True,
    'run': True,
    'fight': False,
    'standing': False,
    'shop': False,
    'inventory': False,
    'help': False,
    'enemy': '',
    'enemy_stats': {
        'hp': 0,
        'atk': 0,
        'exp': 0,
        'gold': 0,
        'weapon': {
            'name': '',
            'attack': 0,
        },
        'armor': {
            'name': '',
            'defense': 0,
        },
    },
    'dest': "",
    'notifications': [
            {"text": "Welcome to the game!", "color": "yellow"},
            {"text": "", "color": "white"},
            {"text": "", "color": "white"},
            {"text": "", "color": "white"},
            {"text": "", "color": "white"},
            {"text": "", "color": "white"}
        ],
    'lastInput': "",
}
