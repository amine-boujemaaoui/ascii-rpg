import enemies as en

gs = {
    'player': {
        'name': '',
        'stats': {
            'hp': 10,
            'max_hp': 100,
            'attack': 10,
            'defense': 10,
            'speed': 10,
            'level': 1,
            'exp': 75,
            'next_lvl_exp': en.exp_table.get(1),
            'gold': 23456,
        },
        'inventory': {
            'weapons': 'fists',
            'armor': 'none',
            'potions': [
                {
                    'name': 'healing',
                    'amount': 4,
                },
                {
                    'name': 'mana',
                    'amount': 2,
                },
            ]
        },
        'pos': {
            'x': 0,
            'y': 0,
        }
    },
    'menu': True,
    'rules': False,
    'play': False,
    'run': True,
    'fight': False,
    'standing': False,
    'enemy': '',
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
