e = {
    "slime": {
        "min_hp": 5,
        "max_hp": 10,
        "min_atk": 1,
        "max_atk": 2,
        "min_exp": 5,
        "max_exp": 10,
        "min_gold": 1,
        "max_gold": 2,
        
        "possible_weapons": [],
        "possible_armors": [],
    },
    "Goblin": {
        "min_hp": 10,
        "max_hp": 20,
        "min_atk": 2,
        "max_atk": 4,
        "min_exp": 20,
        "max_exp": 40,
        "min_gold": 2,
        "max_gold": 4,
        
        "possible_weapons": [
            {
                "name": "sword",
                "percent": 10,
            },
        ],
        "possible_armors": [
            {
                "name": "leather",
                "percent": 20,
            },
        ],
    },
}

exp_table = {
    1: 100,
    2: 200,
    3: 400,
    4: 800,
    5: 1600,
    6: 3200,
    7: 6400,
    8: 12800,
    9: 25600,
    10: 51200,
}