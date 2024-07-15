e = {
    "slime": {
        "min_hp": 5,
        "max_hp": 10,
        "min_atk": 1,
        "max_atk": 2,
        "min_exp": 1,
        "max_exp": 2,
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
        "min_exp": 2,
        "max_exp": 4,
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
     "Orc": {
        "min_hp": 20,
        "max_hp": 40,
        "min_atk": 4,
        "max_atk": 8,
        "min_exp": 4,
        "max_exp": 8,
        "min_gold": 4,
        "max_gold": 8,
        
        "possible_weapons": [
            {
                "name": "axe",
                "percent": 10,
            },
        ],
        "possible_armors": [
            {
                "name": "leather",
                "percent": 40,
            },
            {
                "name": "chainmail",
                "percent": 20,
            },
        ],
    },
    "Troll" :{
        "min_hp": 40,
        "max_hp": 80,
        "min_atk": 8,
        "max_atk": 16,
        "min_exp": 8,
        "max_exp": 16,
        "min_gold": 8,
        "max_gold": 16,
        
        "possible_weapons": [
            {
                "name": "chainmail",
                "percent": 40,
            },
        ],
        
    },
    "Dragon": {
        "min_hp": 80,
        "max_hp": 160,
        "min_atk": 16,
        "max_atk": 32,
        "min_exp": 16,
        "max_exp": 32,
        "min_gold": 16,
        "max_gold": 32,
        
        "possible_weapons": [],
        "possible_armors": [],
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