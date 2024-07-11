import colors as c
import states as s
import map as m
import functions as f

title_screen = f"""{c.c['cyan']}│{c.r}                       ┌────────────────────┐                      {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                       │  1. New Game       │                      {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                       │  2. Load Game      │                      {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                       │  3. Rules          │                      {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                       │  4. Quit Game      │                      {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                       └────────────────────┘                      {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                                                                   {c.c['cyan']}│{c.r}
{c.c['cyan']}└───────────────────────────────────────────────────────────────────┘{c.r}"""

rules = f"""{c.c['cyan']}│{c.r}                       ┌────────────────────┐                      {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                       │       RULES        │                      {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                       └────────────────────┘                      {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                                                                   {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}    1. Rule one description.                                       {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}    2. Rule two description.                                       {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}    3. Rule three description.                                     {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                                                                   {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                                                                   {c.c['cyan']}│{c.r}
{c.c['cyan']}└───────────────────────────────────────────────────────────────────┘{c.r}"""

prompt = f"{c.c['green']}gonis > {c.r}"


title = f"""{c.c['cyan']}┌───────────────────────────────────────────────────────────────────┐{c.r}
{c.c['cyan']}│{c.r}                                                                   {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                 ██████╗  ██████╗ ███╗   ██╗██╗███████╗            {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                ██╔════╝ ██╔═══██╗████╗  ██║██║██╔════╝            {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                ██║  ███╗██║   ██║██╔██╗ ██║██║███████╗            {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                ██║   ██║██║   ██║██║╚██╗██║██║╚════██║            {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                ╚██████╔╝╚██████╔╝██║ ╚████║██║███████║            {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                 ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚══════╝            {c.c['cyan']}│{c.r}
{c.c['cyan']}│{c.r}                                                                   {c.c['cyan']}│{c.r}"""

bottom = f"{c.c['cyan']}└───────────────────────────────────────────────────────────────────┘{c.r}"


def draw_directions():
    directions = [ 
        f"{c.c['cyan']}┌───────────┐{c.r}",
        f"{c.c['cyan']}│           │{c.r}",
        f"{c.c['cyan']}│{c.r} {c.s['bold']}w - NORTH{c.r} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} {c.s['bold']}a - WEST{c.r}  {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} {c.s['bold']}s - SOUTH{c.r} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} {c.s['bold']}d - EAST{c.r}  {c.c['cyan']}│{c.r}",
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
        f"{c.c['cyan']}┌───────────────────────────────────────┐{c.r}",
        f"{c.c['cyan']}│{c.c[notifications[-6][co]]} {notifications[-6][t].ljust(37)} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.c[notifications[-5][co]]} {notifications[-5][t].ljust(37)} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.c[notifications[-4][co]]} {notifications[-4][t].ljust(37)} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.c[notifications[-3][co]]} {notifications[-3][t].ljust(37)} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.c[notifications[-2][co]]} {notifications[-2][t].ljust(37)} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.c[notifications[-1][co]]} {notifications[-1][t].ljust(37)} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}└───────────────────────────────────────┘{c.r}",
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
    table.extend(content)
    table.append(f"{c.c['cyan']}└{'─' * (line_length + 2)}┘{c.r}")
    return table

def draw_map():
    player_pos_x = s.gs['player']['pos']['x']
    player_pos_y = s.gs['player']['pos']['y']
    map_width = len(m.map[0])
    
    map_lines = [
        f"{c.c['cyan']}┌{'─' * map_width}┐{c.r}"
    ]
    
    for y, row in enumerate(m.map):
        line = f"{c.c['cyan']}│{c.r}"
        for x, cell in enumerate(row):
            if x == player_pos_x and y == player_pos_y:
                player_symbol = m.bioms['player']['symbol']
                player_color = m.bioms['player']['color']
                line += f"{player_color}{player_symbol}{c.r}"
            else:
                biom = m.bioms[cell]
                line += f"{biom['color']}{biom['symbol']}{c.r}"
        line += f"{c.c['cyan']}│{c.r}"
        map_lines.append(line)
    
    map_lines.append(f"{c.c['cyan']}└{'─' * map_width}┘{c.r}")
    
    return map_lines

def draw_stats():
    line_length = 24  # Adjust the line length as needed
    value_column_start = 10  # Column where the value starts
    player = s.gs['player']
    stats = player['stats']
    
    hp_bar = draw_hp_bar(stats['hp'], stats['max_hp'], line_length - 10)
    exp_bar = draw_bar(stats['exp'], stats['next_lvl_exp'], line_length - 10, c.c['cyan'], c.c['cyan'])
    empty_line = f"{c.c['cyan']}│{' ' * (line_length + 2)}│{c.r}"

    title = "Player Stats"
    stats_lines = [
        f"{c.c['cyan']}│{c.r} {format_stat_line('Name', player['name'], line_length, value_column_start)} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} {format_stat_line('HP', hp_bar, line_length, value_column_start)} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} {format_stat_line('Exp', exp_bar, line_length, value_column_start)} {c.c['cyan']}│{c.r}",
        empty_line,
        f"{c.c['cyan']}│{c.r} {format_stat_line('Attack', stats['attack'], line_length, value_column_start)} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} {format_stat_line('Defense', stats['defense'], line_length, value_column_start)} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} {format_stat_line('Speed', stats['speed'], line_length, value_column_start)} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} {format_stat_line('Level', stats['level'], line_length, value_column_start)} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} {format_stat_line('Gold', f"{c.c['yellow']}{stats['gold']}{c.r}$", line_length + 9, value_column_start)} {c.c['cyan']}│{c.r}",
        empty_line,
        f"{c.c['cyan']}│{c.r} {format_stat_line('XY', f'{player["pos"]["x"]}, {player["pos"]["y"]}', line_length, value_column_start)} {c.c['cyan']}│{c.r}",
    ]

    return draw_outlines(title, stats_lines, line_length)

def draw_inventory():
    line_length = 24  # Adjust the line length as needed
    value_column_start = 14  # Column where the value starts
    player = s.gs['player']
    inventory = player['inventory']
    
    title = "Inventory"
    inventory_lines = [
        f"{c.c['cyan']}│{c.r} {format_stat_line('Weapon', inventory['weapons'], line_length, value_column_start)} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} {format_stat_line('Armor', inventory['armor'], line_length, value_column_start)} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}│{c.r} {c.c['gray']}Potions:{c.r} {' ' * (line_length - 9)} {c.c['cyan']}│{c.r}",
    ]
    
    for potion in inventory['potions']:
        potion_label = f"  {potion['name']}:"
        inventory_lines.append(
            f"{c.c['cyan']}│{c.r} {format_stat_line(potion_label, potion['amount'], line_length, value_column_start)} {c.c['cyan']}│{c.r}"
        )
    
    return draw_outlines(title, inventory_lines, line_length)

def current_biome():
    player_pos_x = s.gs['player']['pos']['x']
    player_pos_y = s.gs['player']['pos']['y']
    current_biome_key = m.map[player_pos_y][player_pos_x]
    biome = m.bioms[f.get_biome()]

    art = m.ascii_art.get(biome['name'], [""] * 4)

    current_biome_box = [
        f"{c.c['cyan']}┌───────────┐{c.r}",
        f"{c.c['cyan']}│ {biome['name'].center(9)} {c.c['cyan']}│{c.r}",
        f"{c.c['cyan']}├───────────┤{c.r}",
        f"{c.c['cyan']}│ {art[0].center(9)} │{c.r}",
        f"{c.c['cyan']}│ {art[1].center(9)} │{c.r}",
        f"{c.c['cyan']}│ {art[2].center(9)} │{c.r}",
        f"{c.c['cyan']}│ {art[3].center(9)} │{c.r}",
        f"{c.c['cyan']}└───────────┘{c.r}"
    ]

    return current_biome_box

def print_game():
    f.cls()
    map_lines = draw_map()
    stats_lines = draw_stats()
    inventory_lines = draw_inventory()
    current_biome_lines = current_biome()

    combined_stats_inventory_lines = stats_lines + inventory_lines

    max_lines = max(len(map_lines), len(combined_stats_inventory_lines))
    
    if len(map_lines) < max_lines:
        map_lines.extend([' ' * (len(map_lines[0]) - 9)] * (max_lines - len(map_lines)))
    
    if len(combined_stats_inventory_lines) < max_lines:
        combined_stats_inventory_lines.extend([' ' * 24] * (max_lines - len(combined_stats_inventory_lines)))

    for map_line, stats_inventory_line in zip(map_lines, combined_stats_inventory_lines):
        print(f"{map_line} {stats_inventory_line}")
    
    directions = draw_directions()
    notification_box = draw_notifications()

    max_length = max(len(directions), len(notification_box), len(current_biome_lines))

    # Extend lists to match the maximum length
    directions.extend([''] * (max_length - len(directions)))
    notification_box.extend([''] * (max_length - len(notification_box)))
    current_biome_lines.extend([''] * (max_length - len(current_biome_lines)))

    for i in range(max_length):
        print(f"{directions[i]:<14} {notification_box[i]:<50} {current_biome_lines[i]}")
    