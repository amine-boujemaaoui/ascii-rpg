import colors as c
import states as s
import mapInfos as m
import functions as f
import enemies as en

title_screen = f"""{c.c['cyan']}│{c.r}                        ┌────────────────────┐                       {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                        │  1. New Game       │                       {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                        │  2. Load Game      │                       {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                        │  3. Rules          │                       {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                        │  4. Quit Game      │                       {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                        └────────────────────┘                       {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                                                                     {c.c['cyan']}│{c.r}
{c.c['cyan']}└─────────────────────────────────────────────────────────────────────┘{c.r}"""

rules = f"""{c.c['cyan']}│{c.r}                         ┌────────────────────┐                      {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                         │       RULES        │                      {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                         └────────────────────┘                      {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                                                                     {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}    1. Rule one description.                                         {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}    2. Rule two description.                                         {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}    3. Rule three description.                                       {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                                                                     {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                                                                     {c.c['cyan']}│{c.r}
{c.c['cyan']}└─────────────────────────────────────────────────────────────────────┘{c.r}"""

prompt = f"{c.c['green']}gonis > {c.r}"


title = f"""{c.c['cyan']}┌─────────────────────────────────────────────────────────────────────┐{c.r}
{c.c['cyan']}│{c.r}                                                                     {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                  ██████╗  ██████╗ ███╗   ██╗██╗███████╗             {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                 ██╔════╝ ██╔═══██╗████╗  ██║██║██╔════╝             {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                 ██║  ███╗██║   ██║██╔██╗ ██║██║███████╗             {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                 ██║   ██║██║   ██║██║╚██╗██║██║╚════██║             {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                 ╚██████╔╝╚██████╔╝██║ ╚████║██║███████║             {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                  ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝╚══════╝             {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                                                                     {c.c['cyan']}│{c.r}"""

bottom = f"{c.c['cyan']}└─────────────────────────────────────────────────────────────────────┘{c.r}"

empty_line = f"{c.c['cyan']}│{c.r}                                                                     {c.c['cyan']}│{c.r}"


def draw_directions():
    directions = [ 
        f"{c.c['cyan']}┌───────────┐{c.r}",
        f"{c.c['cyan']}│           │{c.r}",
        f"{c.c['cyan']}│{c.r} {c.s['bold']}help     {c.r} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} {c.s['bold']}save     {c.r} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} {c.s['bold']}exit     {c.r} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} {c.s['bold']}equip    {c.r} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│           │{c.r}",
        f"{c.c['cyan']}└───────────┘{c.r}",
    ]
    return directions

def draw_notifications():
    nb_notifications = len(s.gs['notifications'])
    notifications = s.gs['notifications'][-nb_notifications:]
    t = 'text'
    co = 'color'

    notification_box = [
        f"{c.c['cyan']}┌─────────────────────────────────────────┐{c.r}",
        f"{c.c['cyan']}│{c.r}{c.c[notifications[-6][co]]} {notifications[-6][t].ljust(39)}{c.r} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r}{c.c[notifications[-5][co]]} {notifications[-5][t].ljust(39)}{c.r} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r}{c.c[notifications[-4][co]]} {notifications[-4][t].ljust(39)}{c.r} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r}{c.c[notifications[-3][co]]} {notifications[-3][t].ljust(39)}{c.r} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r}{c.c[notifications[-2][co]]} {notifications[-2][t].ljust(39)}{c.r} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r}{c.c[notifications[-1][co]]} {notifications[-1][t].ljust(39)}{c.r} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}└─────────────────────────────────────────┘{c.r}",
    ]

    return notification_box

def format_stat_line(label, value, line_length, value_column_start):
    label_length = len(label) + 2
    value_str = str(value)
    value_length = len(value_str)

    if value_column_start > label_length:
        padding_before_value = value_column_start - label_length
    else:
        padding_before_value = 1
    
    padding_total = line_length - (label_length + padding_before_value + value_length)
    
    return f"{c.c['gray']}{label}:{c.r} {' ' * padding_before_value}{value_str}{' ' * padding_total}"

def draw_label_line(label, line_length):
    label_length = len(label)
    padding_total = line_length - label_length + 9
    return f"{c.c['white']}{label}{c.r}{' ' * padding_total}"



def draw_bar(value, value_max, size, fillColor, emptyColor, fill='█', empty='░'):
    value_ratio = min(max(value / value_max, 0.0), 1.0)
    
    filled_size = int(size * value_ratio)
    empty_size = size - filled_size

    filled_bar = f"{fillColor}{fill * filled_size}{c.r}"
    empty_bar = f"{emptyColor}{empty * empty_size}{c.r}"
    
    bar = f"{filled_bar}{empty_bar}"
    return bar
    
    
def draw_hp_bar(value, value_max, size):
    value_ratio = value / value_max
    
    if value_ratio > 0.75:
        fillColor = c.c['green']
    elif value_ratio > 0.5:
        fillColor = c.c['yellow']
    elif value_ratio > 0.25:
        fillColor = c.c['orange']
    else:
        fillColor = c.c['red']
    
    return draw_bar(value, value_max, size, fillColor, fillColor)


def draw_outlines(title, content, line_length=20):
    table = [
        f"{c.c['cyan']}┌{'─' * (line_length + 2)}┐{c.r}",
        f"{c.c['cyan']}│{c.r} {c.s['bold']}{title.center(line_length)}{c.r} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}├{'─' * (line_length + 2)}┤{c.r}",
    ]
    for line in content:
        table.append(f"{c.c['cyan']}│{c.r} {line} {c.c['cyan']}│{c.r}")
    table.append(f"{c.c['cyan']}└{'─' * (line_length + 2)}┘{c.r}")
    return table

def draw_map():
    player_pos_x = s.gs['player']['pos']['x']
    player_pos_y = s.gs['player']['pos']['y']
    map_data = s.gs['map'].map
    map_width = len(map_data[0])
    title = "🗺️ Map"
    
    map_lines = []
    line_length = map_width
    
    for y, row in enumerate(map_data):
        line = f""
        for x, cell in enumerate(row):
            if x == player_pos_x and y == player_pos_y:
                player_symbol = m.bioms['player']['symbol']
                player_color = m.bioms['player']['color']
                line += f"{player_color}{player_symbol}{c.r}"
            else:
                biom = cell.biome
                line += f"{biom['color']}{biom['symbol']}{c.r}"
        map_lines.append(line)
    
    return draw_outlines(title, map_lines, line_length)

def draw_stats():
    line_length = 24  # Adjust the line length as needed
    value_column_start = 10  # Column where the value starts
    player = s.gs['player']
    stats = player['stats']
    
    hp_bar = draw_hp_bar(stats['hp'], stats['max_hp'], line_length - 10)
    exp_bar = draw_bar(stats['exp'], stats['next_lvl_exp'], line_length - 10, c.c['cyan'], c.c['cyan'])
    empty_line = f"{' ' * (line_length)}"

    title = "Player Stats"
    stats_lines = [
        f"{format_stat_line('Name', f"{c.bg['white']}{c.c['black']} {player['name']} {c.r}", line_length + 14, value_column_start)}",
        f"{format_stat_line('HP', hp_bar, line_length, value_column_start)}",
        f"{format_stat_line('Exp', exp_bar, line_length, value_column_start)}",
        empty_line,
        f"{format_stat_line('Attack', stats['attack'], line_length, value_column_start)}",
        f"{format_stat_line('Defense', stats['defense'], line_length, value_column_start)}",
        f"{format_stat_line('Speed', stats['speed'], line_length, value_column_start)}",
        f"{format_stat_line('Level', stats['level'], line_length, value_column_start)}",
        f"{format_stat_line('Gold', f"{c.c['yellow']}{stats['gold']}{c.r}$", line_length + 9, value_column_start)}",
        empty_line,
        f"{format_stat_line('XY', f'{player["pos"]["x"]}, {player["pos"]["y"]}', line_length, value_column_start)}",
    ]

    return draw_outlines(title, stats_lines, line_length)

def draw_equipment():
    line_length = 24  # Adjust the line length as needed
    value_column_start = 14  # Column where the value starts
    player = s.gs['player']
    equipment = player['equipment']
    
    title = "equipment"
    equipment_lines = [
        f"{format_stat_line('Weapon', equipment['weapons'], line_length, value_column_start)}",
        f"{format_stat_line('Armor', equipment['armor'], line_length, value_column_start)}",
        f"{c.c['gray']}Potions:{c.r} {' ' * (line_length - 9)}",
    ]
    
    for potion in equipment['potions']:
        potion_label = f"  {potion['name']}"
        equipment_lines.append(
            f"{format_stat_line(potion_label, potion['amount'], line_length, value_column_start)}"
        )
    
    return draw_outlines(title, equipment_lines, line_length)

def current_biome():
    biome = f.get_biome().biome
    art = m.ascii_art.get(biome['name'], [""] * 4)

    current_biome_box = [
        f"{art[0].center(9)}",
        f"{art[1].center(9)}",
        f"{art[2].center(9)}",
        f"{art[3].center(9)}",
    ]

    return draw_outlines(biome['name'], current_biome_box, 9)

def print_play():
    f.cls()
    map_lines = draw_map()
    stats_lines = draw_stats()
    equipment_lines = draw_equipment()
    current_biome_lines = current_biome()

    combined_stats_equipment_lines = stats_lines + equipment_lines

    max_lines = max(len(map_lines), len(combined_stats_equipment_lines))
    
    if len(map_lines) < max_lines:
        map_lines.extend([' ' * (len(map_lines[0]) - 9)] * (max_lines - len(map_lines)))
    
    if len(combined_stats_equipment_lines) < max_lines:
        combined_stats_equipment_lines.extend([' ' * 24] * (max_lines - len(combined_stats_equipment_lines)))

    for map_line, stats_equipment_line in zip(map_lines, combined_stats_equipment_lines):
        print(f"{map_line} {stats_equipment_line}")
    
    directions = draw_directions()
    notification_box = draw_notifications()

    max_length = max(len(directions), len(notification_box), len(current_biome_lines))

    # Extend lists to match the maximum length
    directions.extend([''] * (max_length - len(directions)))
    notification_box.extend([''] * (max_length - len(notification_box)))
    current_biome_lines.extend([''] * (max_length - len(current_biome_lines)))

    for i in range(max_length):
        print(f"{directions[i]:<14} {notification_box[i]:<50} {current_biome_lines[i]}")        
        
def draw_fight():
    line_length = 38  # Length of the lines for the fight screen
    empty_line = f"{' ' * (line_length)}"
    
    enemy_name = s.gs['enemy']
    enemy_stats = s.gs['enemy_stats']
    enemy_hp = enemy_stats['hp']
    enemy_max_hp = enemy_stats['max_hp']
    enemy_hp_bar = draw_hp_bar(enemy_hp, enemy_max_hp, line_length)
    
    enemy_weapon = enemy_stats['weapon']['name']
    if enemy_weapon == '':
        enemy_weapon = "None"
    enemy_weapon_attack = enemy_stats['weapon']['attack']
    
    enemy_armor = enemy_stats['armor']['name']
    if enemy_armor == '':
        enemy_armor = "None"
    enemy_armor_defense = enemy_stats['armor']['defense']

    fight_screen = [
        empty_line,
        f"{draw_label_line(f"{c.c['red']}Enemy: {enemy_name}{c.r}", line_length)}",
        f"{enemy_hp_bar}{c.r}",
        empty_line,
        f"{format_stat_line('Max HP', enemy_max_hp, line_length, 15)}",
        f"{format_stat_line('Attack', enemy_stats['atk'], line_length, 15)}",
        empty_line,
        f"{format_stat_line('Weapon', "", line_length, 10)}",
        f"{format_stat_line('  - Name', enemy_weapon, line_length, 15)}",
        f"{format_stat_line('  - Attack', enemy_weapon_attack, line_length, 15)}",
        empty_line,
        f"{format_stat_line('Armor', "", line_length, 10)}",
        f"{format_stat_line('  - Name', enemy_armor, line_length, 15)}",
        f"{format_stat_line('  - Deffense', enemy_armor_defense, line_length, 9)}",
        empty_line,
        empty_line,
        empty_line,
        empty_line,
        empty_line,
        empty_line,
    ]

    return draw_outlines("⚔️ Fight !", fight_screen, line_length)

def draw_shop():
    line_length = 31
    empty_line = f"{' ' * (line_length)}"

    available_weapons = [
        {'name': 'sword', 'attack': 10, 'price': 100},
        {'name': 'axe', 'attack': 15, 'price': 150},
        {'name': 'bow', 'attack': 20, 'price': 200}
    ]
    available_armors = [
        {'name': 'leather', 'defense': 10, 'price': 50},
        {'name': 'chainmail', 'defense': 15, 'price': 100},
        {'name': 'iron', 'defense': 20, 'price': 150}
    ]

    shop_items = []
    shop_items.append(empty_line)
    shop_items.append(f"{c.bg['white']}{c.c['black']}{'Weapons:'.center(line_length)}{c.r}")

    for weapon in available_weapons:
        shop_items.append(f" {weapon['name'].ljust(12)} ATK: {str(weapon['attack']).ljust(3)} {str(weapon['price']).rjust(4)} ${' ' * 2}")

    shop_items.append(empty_line)
    shop_items.append(f"{c.bg['white']}{c.c['black']}{'Armors:'.center(line_length)}{c.r}")

    for armor in available_armors:
        shop_items.append(f" {armor['name'].ljust(12)} DEF: {str(armor['defense']).ljust(3)} {str(armor['price']).rjust(4)} ${' ' * 2}")

    shop_items.append(empty_line)
    shop_items.append(f"{'Player Gold:'.ljust(line_length - len(str(s.gs['player']['stats']['gold'])) - 2)}{c.bg['yellow']}{c.c['black']}{str(s.gs['player']['stats']['gold']).rjust(len(str(s.gs['player']['stats']['gold'])))} ${c.r}")

    return draw_outlines("Shop", shop_items, line_length)


def draw_instructions():
    instructions = [
        f"{c.c['cyan']}┌───────────┐{c.r}",
        f"{c.c['cyan']}│           │{c.r}",
        f"{c.c['cyan']}│{c.r} buy  <it> {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} sell <it> {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} exit      {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│           {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│           {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}└───────────┘{c.r}",
    ]
    return instructions


def draw_actions():
    actions = [
        f"{c.c['cyan']}┌─────────────────────────┐{c.r}",
        f"{c.c['cyan']}│                         │{c.r}",
        f"{c.c['cyan']}│{c.r} 1 - Attack              {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} 2 - Use Potion (H)      {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} 3 - Use Potion (M)      {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} 4 - Escape              {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│                         │{c.r}",
        f"{c.c['cyan']}└─────────────────────────┘{c.r}",
    ]
    return actions

def print_fight():
    f.cls()
    fight_screen = draw_fight()
    stats_lines = draw_stats()
    equipment_lines = draw_equipment()
    
    combined_stats_equipment_lines = stats_lines + equipment_lines

    max_lines = max(len(fight_screen), len(combined_stats_equipment_lines))
    
    if len(fight_screen) < max_lines:
        fight_screen.extend([' ' * (len(fight_screen[0]) - 9)] * (max_lines - len(fight_screen)))
    
    if len(combined_stats_equipment_lines) < max_lines:
        combined_stats_equipment_lines.extend([' ' * 24] * (max_lines - len(combined_stats_equipment_lines)))

    for fight_line, stats_equipment_line in zip(fight_screen, combined_stats_equipment_lines):
        print(f"{fight_line} {stats_equipment_line}")
    
    actions = draw_actions()
    notification_box = draw_notifications()

    max_length = max(len(actions), len(notification_box))

    # Extend lists to match the maximum length
    actions.extend([''] * (max_length - len(actions)))
    notification_box.extend([''] * (max_length - len(notification_box)))

    for i in range(max_length):
        print(f"{actions[i]:<16} {notification_box[i]:<50}")
        
def draw_inventory():
    line_length = 31
    empty_line = f"{' ' * (line_length)}"

    player = s.gs['player']
    inventory = player['inventory']

    weapons = [item for item in inventory if item.get('type') == 'weapon']
    armors = [item for item in inventory if item.get('type') == 'armor']

    inventory_items = []
    inventory_items.append(empty_line)
    inventory_items.append(f"{c.bg['white']}{c.c['black']}{'Weapon:'.center(line_length)}{c.r}")

    for weapon in weapons:
        inventory_items.append(f" {weapon['name'].ljust(12)} ATK: {str(weapon['attack']).ljust(3)} {' ' * 8}")

    for _ in range(4 - len(weapons)):
        inventory_items.append(empty_line)

    inventory_items.append(f"{c.bg['white']}{c.c['black']}{'Armor:'.center(line_length)}{c.r}")

    for armor in armors:
        inventory_items.append(f" {armor['name'].ljust(12)} DEF: {str(armor['defense']).ljust(3)} {' ' * 8}")

    for _ in range(4 - len(armors)):
        inventory_items.append(empty_line)

    inventory_items.append(f"{'Player Gold:'.ljust(line_length - len(str(player['stats']['gold'])) - 2)}{c.bg['yellow']}{c.c['black']}{str(player['stats']['gold']).rjust(len(str(player['stats']['gold'])))} ${c.r}")

    return draw_outlines("Inventory", inventory_items, line_length)


def print_inventory():
    f.cls()
    inventory_lines = draw_inventory()
    for line in inventory_lines:
        print(line)
        

def print_shop():
    f.cls()
    shop_lines = draw_shop()
    inventory_lines = draw_inventory()
    instructions_lines = draw_instructions()
    notification_box = draw_notifications()
    current_biome_lines = current_biome()

    # Afficher shop et inventory
    for shop_line, inventory_line in zip(shop_lines, inventory_lines):
        print(f"{shop_line:<38} {inventory_line:<38}")

    # Afficher instructions et notification_box côte à côte en bas
    for instr, notif, biome in zip(instructions_lines, notification_box, current_biome_lines):
        print(f"{instr} {notif} {biome}")
        
def draw_equipment():
    line_length = 24
    empty_line = f"{' ' * (line_length)}"

    player = s.gs['player']
    equipment = player['equipment']
    
    title = "Equipment"
    equipment_lines = [
        f"{format_stat_line('Weapon', equipment['weapons'], line_length, 14)}",
        f"{format_stat_line('Armor', equipment['armor'], line_length, 14)}",
        f"{c.c['gray']}Potions:{c.r} {' ' * (line_length - 9)}",
    ]
    
    for potion in equipment['potions']:
        potion_label = f"  {potion['name']}"
        equipment_lines.append(
            f"{format_stat_line(potion_label, potion['amount'], line_length, 14)}"
        )
    
    return draw_outlines(title, equipment_lines, line_length)

def print_equipment():
    f.cls()
    stats_lines = draw_stats()
    equipment_lines = draw_equipment()
    notification_box = draw_notifications()

    for stats_line, equipment_line, notification_line in zip(stats_lines, equipment_lines, notification_box):
        print(f"{stats_line} {equipment_line} {notification_line}")
        
        
def draw_help():
    line_length = 67  # Adjust the line length as needed
    empty_line = f"{' ' * (line_length)}"
    categories = {
        "Directions": [
            {"command": "w", "description": "Move north"},
            {"command": "s", "description": "Move south"},
            {"command": "a", "description": "Move west"},
            {"command": "d", "description": "Move east"}
        ],
        "Commands": [
            {"command": "save", "description": "Save the game"},
            {"command": "quit", "description": "Quit the game"},
            {"command": "life", "description": "Display current HP"},
            {"command": "equip <item_name>", "description": "Equip the specified item"},
            {"command": "inventory", "description": "Display the inventory"},
            {"command": "help", "description": "Display this help menu"}
        ]
    }

    help_lines = []
    for category, cmds in categories.items():
        help_lines.append(f"{c.bg['white']}{c.c['black']}{category}:{c.r}{' ' * (line_length - len(category) - 1)}")
        for cmd in cmds:
            command_str = f"  {cmd['command']:<20} - {cmd['description']}"
            help_lines.append(command_str.ljust(line_length))
        help_lines.append(empty_line)  

    return draw_outlines("Help", help_lines, line_length)

def print_help():
    f.cls()
    help_lines = draw_help()
    for line in help_lines:
        print(line)


def print_game():
    if s.gs['play']:
        print_play()
    elif s.gs['rules']:
        f.cls()
        print(title)
        print(rules)
    elif s.gs['fight']:
        print_fight()
    elif s.gs['shop']:
        print_shop()
    elif s.gs['inventory']:
        print_inventory()
        notification_box = draw_notifications()
        for line in notification_box:
            print(line)
    elif s.gs['help']:
        print_help()
    else:
        print(title_screen)
