import os
import ui
import colors as c
import states as s
import time
import json
import mapInfos as m
import random
import enemies as en
import objects as obj
from map import Map

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def change_state(last_state: str, new_state: str):
    s.gs['lastUI'] = last_state
    s.gs[last_state] = False
    s.gs[new_state] = True
    
def i(string: str = ""):
    if string == "": 
        return input(f"{ui.prompt}")
    return input(f"{ui.prompt}{c.c['yellow']}{string}{c.r}\n{ui.prompt}")

def level_up():
    player = s.gs['player']
    current_level = player['stats']['level']
    current_exp = player['stats']['exp']
    
    if current_exp >= en.exp_table[current_level]:
        player['stats']['level'] += 1
        player['stats']['max_hp'] += 10  # Augmente les HP max du joueur à chaque niveau
        player['stats']['attack'] += 2   # Augmente l'attaque du joueur à chaque niveau
        player['stats']['defense'] += 2  # Augmente la défense du joueur à chaque niveau
        player['stats']['speed'] += 1    # Augmente la vitesse du joueur à chaque niveau
        add_notification(f"└─> You leveled up to level {player['stats']['level']}!", "gray")
        add_notification(f"┬>Congratulation !", "green")
        
        current_level = player['stats']['level']
        if current_level in en.exp_table:
            player['stats']['next_lvl_exp'] = en.exp_table[current_level]
        else:
            player['stats']['next_lvl_exp'] = float('inf')  # Plus de niveaux à atteindre

    
def rules():
    ui.print_game()
    i(f"{c.c['gray']}{c.s['italic']}Press enter to return to the main menu.{c.r}")
    change_state('rules', 'menu')

def title_screen():
    cls()
    print(ui.title)
    print(ui.title_screen)
    choice = input(ui.prompt)
    return choice

def new_game():
    cls()
    print(ui.title)
    print(ui.bottom)
    s.gs['player']['name'] = i("What is your name?")
    while len(s.gs['player']['name']) > 12:
        cls()
        print(ui.title)
        print(f"{c.c['red']}Name must be 12 characters or less. Please try again.{c.r}")
        s.gs['player']['name'] = i("What is your name?")
        
    if s.gs['player']['name'] == "cancel":
        change_state('menu', 'menu')
        return
        
    change_state('menu', 'play')

def menu():
    while s.gs['menu']:
        if s.gs['rules']:
            s.gs['rules'] = rules()
        else:
            choice = title_screen()
            match choice:
                case "1" | "new":
                    new_game()
                case "2" | "load":
                    load_saved_game()
                case "3" | "rules":
                    change_state('menu', 'rules')
                case "4" | "quit":
                    quit()
                case "help":
                    change_state('menu', 'help')
                    help()
                case _:
                    print(f"{c.c['red']}Invalid choice!{c.r}")
                    time.sleep(2)


import json

def save_game():
    with open("save.txt", "w") as file:
        map_data = s.gs['map'].to_dict() if isinstance(s.gs['map'], Map) else s.gs['map']
        game_state = s.gs.copy()
        game_state['map'] = map_data
        json.dump(game_state, file, indent=4, sort_keys=True)


        
def load_game():
    with open("save.txt", "r") as file:
        saved_data = json.load(file)

    # Reconstruire l'instance de Map à partir du dictionnaire
    if isinstance(saved_data['map'], dict):
        s.gs['map'] = Map.from_dict(saved_data['map'])
    else:
        s.gs['map'] = Map()  # Initialisation par défaut si la carte n'est pas un dictionnaire

    # Charger les autres données de l'état du jeu
    for key, value in saved_data.items():
        if key != 'map':
            s.gs[key] = value    

    
def get_biome():
    return s.gs['map'].map[s.gs['player']['pos']['y']][s.gs['player']['pos']['x']]

def load_saved_game():
    try:
        load_game()
        change_state('menu', 'play')
    except FileNotFoundError:
        print(f"{c.c['red']}Failed to load the game.{c.r}")
        time.sleep(2)

        
def add_notification(new_notification_text, new_notification_color="white"):
    if 'notifications' not in s.gs:
        s.gs['notifications'] = []

    new_notification = {"text": new_notification_text, "color": new_notification_color}
    s.gs['notifications'].insert(0, new_notification)
    s.gs['notifications'] = s.gs['notifications'][:6]
    ui.print_game()

def check_tile():
    current_map = s.gs['map']
    player_pos_x = s.gs['player']['pos']['x']
    player_pos_y = s.gs['player']['pos']['y']
    current_tile = current_map.map[player_pos_y][player_pos_x]

    if current_tile.biome['name'] == 'shop':
        add_notification(f"You entered a shop.", "magenta")
        time.sleep(2)
        change_state('play', 'shop')
        shop()

def shop():
    change_state('play', 'shop')
    while s.gs['shop']:
        ui.print_game()
        s.gs['lastInput'] = i()
        
        match s.gs['lastInput']:
            case "exit":
                add_notification("You left the shop.", "magenta")
                change_state('shop', 'play')
                time.sleep(2)
            case "inventory":
                change_state('shop', 'inventory')
            case _:
                handle_shop_interaction()

            
def handle_shop_interaction():
    user_input = s.gs['lastInput'].split()
    if len(user_input) != 2:
        add_notification("- Use 'buy <item>' or 'sell <item>'.", "gray")
        add_notification("Invalid command.", "red")
        return
    
    command, item_name = user_input
    if command == "buy":
        buy_item(item_name)
    elif command == "sell":
        sell_item(item_name)
    else:
        add_notification("Invalid command. Use 'buy <item>' or 'sell <item>'.", "red")

        
                
def buy_item(item_name):
    player_gold = s.gs['player']['stats']['gold']
    available_weapons = [
        {'type': 'weapon', 'name': 'sword', 'attack': 10, 'price': 100},
        {'type': 'weapon', 'name': 'axe', 'attack': 15, 'price': 150},
        {'type': 'weapon', 'name': 'bow', 'attack': 20, 'price': 200}
    ]
    available_armors = [
        {'type': 'armor', 'name': 'leather', 'defense': 10, 'price': 50},
        {'type': 'armor', 'name': 'chainmail', 'defense': 15, 'price': 100},
        {'type': 'armor', 'name': 'iron', 'defense': 20, 'price': 150}
    ]
    item_to_buy = None

    for weapon in available_weapons:
        if weapon['name'].lower() == item_name.lower():
            item_to_buy = weapon
            break

    if item_to_buy is None:
        for armor in available_armors:
            if armor['name'].lower() == item_name.lower():
                item_to_buy = armor
                break

    if item_to_buy is None:
        add_notification(f"{item_name} is not available for purchase.", "red")
        return

    if player_gold >= item_to_buy['price']:
        s.gs['player']['stats']['gold'] -= item_to_buy['price']
        
        # Remove price key before adding to inventory
        item_to_add = item_to_buy.copy()
        del item_to_add['price']

        s.gs['player']['inventory'].append(item_to_add)
        add_notification(f"You bought {item_name}.", "green")
    else:
        add_notification("You don't have enough gold.", "red")


def sell_item(item_name):
    player_inventory = s.gs['player']['inventory']
    item_to_sell = None
    
    for item in player_inventory:
        if item['name'] == item_name:
            item_to_sell = item
            break
    
    if item_to_sell is None:
        add_notification(f"You don't have {item_name} to sell.", "red")
        return
    
    sell_price = 0
    if item_to_sell['type'] == 'weapon':
        sell_price = item_to_sell['attack'] * 10
    elif item_to_sell['type'] == 'armor':
        sell_price = item_to_sell['defense'] * 10
    
    s.gs['player']['stats']['gold'] += sell_price
    s.gs['player']['inventory'].remove(item_to_sell)
    add_notification(f"You sold {item_name} for {sell_price} gold.", "green")
    
    
def equip_item(item_name):
    if item_name == "fists":
        s.gs['player']['equipment']['weapons'] = 'fists'
        s.gs['player']['stats']['attack'] = 5
        add_notification("You equipped fists as your weapon.", "green")
        return
    elif item_name == "":
        add_notification("- Use 'equip <item>'.", "gray")
        add_notification("Please specify an item to equip.", "red")
        return
    
    player = s.gs['player']
    inventory = player['inventory']

    item_to_equip = next((item for item in inventory if item['name'].lower() == item_name.lower()), None)

    if item_to_equip:
        if item_to_equip['type'] == 'weapon':
            player['equipment']['weapons'] = item_to_equip['name']
            player['stats']['attack'] = item_to_equip['attack']
            add_notification(f"You equipped {item_name} as your weapon.", "green")
        elif item_to_equip['type'] == 'armor':
            player['equipment']['armor'] = item_to_equip['name']
            player['stats']['defense'] = item_to_equip['defense']
            add_notification(f"You equipped {item_name} as your armor.", "green")
        else:
            add_notification(f"{item_name} is not a valid item to equip.", "red")
    else:
        add_notification(f"{item_name} not found in your inventory.", "red")

        

def move():
    current_map = s.gs['map']
    width = current_map.width
    height = current_map.height
    
    match s.gs['dest']:
        case "w":
            if s.gs['player']['pos']['y'] > 0:
                s.gs['player']['pos']['y'] -= 1
            else:
                s.gs['map'] = Map(width, height)
                s.gs['player']['pos']['y'] = height - 1
                add_notification("You reached the northern edge.")
        case "s":
            if s.gs['player']['pos']['y'] < height - 1:
                s.gs['player']['pos']['y'] += 1
            else:
                s.gs['map'] = Map(width, height)
                s.gs['player']['pos']['y'] = 0
                add_notification("You reached the southern edge.")
        case "a":
            if s.gs['player']['pos']['x'] > 0:
                s.gs['player']['pos']['x'] -= 1
            else:
                s.gs['map'] = Map(width, height)
                s.gs['player']['pos']['x'] = width - 1
                add_notification("You reached the western edge.")
        case "d":
            if s.gs['player']['pos']['x'] < width - 1:
                s.gs['player']['pos']['x'] += 1
            else:
                s.gs['map'] = Map(width, height)
                s.gs['player']['pos']['x'] = 0
                add_notification("You reached the eastern edge.")
    check_tile()
                
                
                
def battle():
    if not s.gs['standing'] and get_biome().biome['enemy'] and random.randint(0, 100) <= 30:
        s.gs['enemy'] = random.choice(list(en.e.keys()))
        add_notification(f"/!\ You encountered a {s.gs['enemy']}!", "red")
        time.sleep(2)
        s.gs['play'] = False
        s.gs['fight'] = True
        s.gs['standing'] = True

def play():
    if s.gs['map'] == 'null':
        s.gs['map'] = Map()
        s.gs['player']['pos']['x'] = random.randint(0, s.gs['map'].width - 1)
        s.gs['player']['pos']['y'] = random.randint(0, s.gs['map'].height - 1)
        
    save_game()
    
    while s.gs['play']:
        cls()
        ui.print_game()
        s.gs['lastInput'] = i()
        
        match s.gs['lastInput'].split():
            case ["w"] | ["s"] | ["a"] | ["d"]:
                s.gs['dest'] = s.gs['lastInput']
                move()
                battle()
            
            case ["save"]:
                save_game()
                add_notification("Game saved.", "green")
            
            case ["quit"]:
                add_notification("Quiting game...", "magenta")
                time.sleep(2)
                change_state('play', 'menu')
            
            case ["life"]:
                add_notification(f"You have {s.gs['player']['stats']['hp']} HP.", "green")
            
            case ["equip", *item_name_parts]:
                item_name = " ".join(item_name_parts)  # Joindre les parties du nom de l'article avec des espaces
                equip_item(item_name)
            
            case ["inventory"]:
                change_state('play', 'inventory')
                inventory()
                
            case ["help"]:
                change_state('play', 'help')
                s.gs['lastUI'] = "play"
                help()

            case _:
                add_notification("Invalid command.", "red")


def assign_enemy_weapon():
    s.gs['enemy_stats']['weapon'] = {'name': '', 'attack': 0}
    possible_weapons = en.e[s.gs['enemy']].get('possible_weapons', [])
    
    for weapon in possible_weapons:
        if random.randint(1, 100) <= weapon['percent']:
            weapon_name = weapon['name']
            for w in obj.weapons:
                if w['name'] == weapon_name:
                    s.gs['enemy_stats']['weapon'] = w
                    break
            break
        
def assign_enemy_armor():
    s.gs['enemy_stats']['armor'] = {'name': '', 'defense': 0}
    possible_armors = en.e[s.gs['enemy']].get('possible_armors', [])
    
    for armor in possible_armors:
        if random.randint(1, 100) <= armor['percent']:
            armor_name = armor['name']
            for a in obj.armors:
                if a['name'] == armor_name:
                    s.gs['enemy_stats']['armor'] = a
                    break
            break
        
def add_to_inventory(item):
    s.gs['player']['inventory'].append(item)
    add_notification(f"You picked up a {item['name']}.", "green")
    
def remove_from_inventory(item_name):
    inventory = s.gs['player']['inventory']
    for item in inventory:
        if item['name'] == item_name:
            inventory.remove(item)
            add_notification(f"You removed a {item_name} from your inventory.", "red")
            return
    add_notification(f"{item_name} not found in inventory.", "red")
            
def fight():
    save_game()
    
    s.gs['enemy_stats']['max_hp'] = random.randint(en.e[s.gs['enemy']]['min_hp'], en.e[s.gs['enemy']]['max_hp'])
    s.gs['enemy_stats']['hp'] = s.gs['enemy_stats']['max_hp']
    s.gs['enemy_stats']['atk'] = random.randint(en.e[s.gs['enemy']]['min_atk'], en.e[s.gs['enemy']]['max_atk'])
    s.gs['enemy_stats']['exp'] = random.randint(en.e[s.gs['enemy']]['min_exp'], en.e[s.gs['enemy']]['max_exp'])
    s.gs['enemy_stats']['gold'] = random.randint(en.e[s.gs['enemy']]['min_gold'], en.e[s.gs['enemy']]['max_gold'])
    
    assign_enemy_weapon()
    assign_enemy_armor()
        
    while s.gs['fight']:
        cls()
        print(s.gs['enemy_stats']['weapon'])
        ui.print_game()
        s.gs['lastInput'] = i()
        
        choice = s.gs['lastInput']
        match choice:
            case "1":
                choice = "attack"
            case "2":
                choice = "heal"
            case "3":
                choice = "mana"
            case "4":
                choice = "escape"
            case "inventory":
                change_state('fight', 'inventory')
        
        match choice:
            case "attack":
                player_attack = random.randint(1, s.gs['player']['stats']['attack'])
                enemy_attack = random.randint(en.e[s.gs['enemy']]['min_atk'], en.e[s.gs['enemy']]['max_atk'])
                s.gs['enemy_stats']['hp'] -= player_attack
                add_notification(f"- You inflicted {player_attack} damage !", "white")
                if s.gs['enemy_stats']['hp'] <= 0:
                    s.gs['player']['stats']['exp'] += s.gs['enemy_stats']['exp']
                    s.gs['player']['stats']['gold'] += s.gs['enemy_stats']['gold']
                    add_notification(f"└─> You gained {s.gs['enemy_stats']['exp']} experience", "yellow")
                    add_notification(f"├─> You gained {s.gs['enemy_stats']['gold']} gold", "yellow")
                    add_notification(f"┬> You defeated the {s.gs['enemy']}!", "green")
                    level_up()
                    change_state('fight', 'play')
                    s.gs['standing'] = False
                    time.sleep(2)
                else:
                    s.gs['player']['stats']['hp'] -= enemy_attack
                    add_notification(f"! The {s.gs['enemy']} attacked you for {enemy_attack} damage", "red")
                
                if s.gs['player']['stats']['hp'] <= 0:
                    add_notification(f"You died! Game over !", "red")
                    change_state('fight', 'menu')
                    s.gs['standing'] = False
                    time.sleep(2)
                
            case "heal":
                healing_potion = next((p for p in s.gs['player']['equipment']['potions'] if p['name'] == 'healing'), None)
                if healing_potion and healing_potion['amount'] > 0:
                    if (s.gs['player']['stats']['hp'] + 20) <= s.gs['player']['stats']['max_hp']:
                        s.gs['player']['stats']['hp'] += 20
                    else:
                        s.gs['player']['stats']['hp'] = s.gs['player']['stats']['max_hp']

                    healing_potion['amount'] -= 1
                    add_notification("- You used a health potion.", "green")
                else:
                    add_notification("- You don't have any health potions.", "red")
                    
                enemy_attack = random.randint(en.e[s.gs['enemy']]['min_atk'], en.e[s.gs['enemy']]['max_atk'])
                s.gs['player']['stats']['hp'] -= enemy_attack
                add_notification(f"! The {s.gs['enemy']} attacked you for {enemy_attack} damage", "red")
                                
            case "save":
                save_game()
                add_notification("Game saved.", "green")
            
            case "quit":
                add_notification("Quiting game...", "magenta")
                ui.print_game()
                time.sleep(2)
                s.gs['play'] = False
                s.gs['menu'] = True
                
            case "life":
                add_notification(f"You have {s.gs['player']['stats']['hp']} HP.", "green")
            
def inventory():
    s.gs['inventory'] = True
    while s.gs['inventory']:
        cls()
        ui.print_game()
        s.gs['lastInput'] = i()
        
        match s.gs['lastInput'].split():
            case ["exit"]:
                change_state('inventory', 'play')
            case ["equip", item_name]:
                item_name = " ".join(item_name)  # In case item_name consists of multiple words
                equip_item(item_name)
            case ["help"]:
                change_state('inventory', 'help')
                help()
            case _:
                add_notification("Invalid command.", "red")
            
                
def help():
    s.gs['help'] = True
    while s.gs['help']:
        cls()
        ui.print_game()
        i(f"{c.c['gray']}{c.s['italic']}Press enter to return to the main menu.{c.r}")
        change_state('help', s.gs['lastUI'])
