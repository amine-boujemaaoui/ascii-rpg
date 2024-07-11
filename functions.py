import os
import ui
import colors as c
import states as s
import time
import json
import map as m
import random
import enemies as en

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def i(string: str = ""):
    if string == "": 
        return input(f"{ui.prompt}")
    return input(f"{ui.prompt}{c.c['yellow']}{string}{c.r}\n{ui.prompt}")
    
def rules():
    cls()
    print(ui.title)
    print(ui.rules)
    i(f"{c.c['gray']}{c.s['italic']}Press enter to return to the main menu.{c.r}")
    return False

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
    while len(s.gs['player']['name']) >= 10:
        cls()
        print(ui.title)
        print(f"{c.c['red']}Name must be 10 characters or less. Please try again.{c.r}")
        s.gs['player']['name'] = i("What is your name?")
        
    if s.gs['player']['name'] == "cancel":
        s.gs['menu'] = True
        return
            
    s.gs['play'] = True
    s.gs['menu'] = False

def menu():
    while s.gs['menu']:
        if s.gs['rules']:
            s.gs['rules'] = rules()
        else:
            choice = title_screen()
            match choice:
                case "1":
                    new_game()
                case "2":
                    load_saved_game()
                case "3":
                    s.gs['rules'] = True
                case "4":
                    s.gs['run'] = False
                    s.gs['menu'] = False
                case _:
                    print(f"{c.c['red']}Invalid choice!{c.r}")
                    time.sleep(2)


def save_game(game_state):
    with open("save.txt", "w") as file:
        json.dump(game_state, file, indent=4, sort_keys=True)

def load_game():
    try:
        with open("save.txt", "r") as file:
            game_state = json.load(file)
            return game_state
    except FileNotFoundError:
        print("Save file not found.")
        return None
    
def get_biome():
    return m.map[s.gs['player']['pos']['y']][s.gs['player']['pos']['x']]

def load_saved_game():
    loaded_game_state = load_game()
    if loaded_game_state:
        s.gs.update(loaded_game_state)
        s.gs['menu'] = False
        s.gs['play'] = True
    else:
        print(f"{c.c['red']}Failed to load the game.{c.r}")
        time.sleep(2)
        
def add_notification(new_notification_text, new_notification_color="white"):
    if 'notifications' not in s.gs:
        s.gs['notifications'] = []
        
    nb_notifications = len(s.gs['notifications'])

    new_notification = {"text": new_notification_text, "color": new_notification_color}
    s.gs['notifications'].insert(0, new_notification)
    s.gs['notifications'] = s.gs['notifications'][:6]

def move():
    match s.gs['dest']:
        case "w":
            if s.gs['player']['pos']['y'] > 0:
                s.gs['player']['pos']['y'] -= 1
                add_notification("You moved north.")
        case "s":
            if s.gs['player']['pos']['y'] < len(m.map) - 1:
                s.gs['player']['pos']['y'] += 1
                add_notification("You moved south.")
        case "a":
            if s.gs['player']['pos']['x'] > 0:
                s.gs['player']['pos']['x'] -= 1
                add_notification("You moved west.")
        case "d":
            if s.gs['player']['pos']['x'] < len(m.map[0]) - 1:
                s.gs['player']['pos']['x'] += 1
                add_notification("You moved east.")
                
def battle():
    if not s.gs['standing'] and m.bioms[get_biome()]['enemy'] and random.randint(0, 100) <= 25:
        s.gs['enemy'] = random.choice(list(en.e.keys()))
        add_notification(f"You encountered a {s.gs['enemy']}!", "red")
        ui.print_game()
        time.sleep(2)
        s.gs['play'] = False
        s.gs['fight'] = True
        s.gs['standing'] = True

def play():
    save_game(s.gs)
    while s.gs['play']:
        cls()
        ui.print_game()
        s.gs['lastInput'] = i()
        
        match s.gs['lastInput']:
            case "w" | "s" | "a" | "d":
                s.gs['dest'] = s.gs['lastInput']
                move()
                battle()
            
            case "save":
                save_game(s.gs)
                add_notification("Game saved.", "green")
            
            case "quit":
                add_notification("Quiting game...", "red")
                ui.print_game()
                time.sleep(2)
                s.gs['play'] = False
                s.gs['menu'] = True
                
            case "life":
                add_notification(f"You have {s.gs['player']['stats']['hp']} HP.", "green")
            
            
def fight():
    
    while s.gs['fight']:
        cls()
        print(f"{c.c['red']}You are fighting a {s.gs['enemy']}!{c.r}")
        i("Press enter to attack.")