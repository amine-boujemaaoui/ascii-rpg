import curses

def draw_menu(stdscr, current_option):
    # Définir les couleurs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    # Contenu du menu
    menu = [
        "┌─────────────────────────────────────────────────────────────────────┐",
        "│                                                                     │",
        "│                  ██████╗  ██████╗ ███╗   ██╗██╗███████╗             │",
        "│                 ██╔════╝ ██╔═══██╗████╗  ██║██║██╔════╝             │",
        "│                 ██║  ███╗██║   ██║██╔██╗ ██║██║███████╗             │",
        "│                 ██║   ██║██║   ██║██║╚██╗██║██║╚════██║             │",
        "│                 ╚██████╔╝╚██████╔╝██║ ╚████║██║███████║             │",
        "│                  ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝╚══════╝             │",
        "│                                                                     │",
        "│                                                                     │",
        "│                        ┌────────────────────┐                       │",
        "│                        │  1. New Game       │                       │",
        "│                        │  2. Load Game      │                       │",
        "│                        │  3. Rules          │                       │",
        "│                        │  4. Quit Game      │                       │",
        "│                        └────────────────────┘                       │",
        "│                                                                     │",
        "└─────────────────────────────────────────────────────────────────────┘"
    ]
    
    # Afficher le menu avec la ligne sélectionnée surlignée
    for idx, line in enumerate(menu):
        if idx == 11:
            if current_option == 1:
                stdscr.addstr(idx, 0, line[:26], curses.color_pair(1))
                stdscr.addstr(idx, 26, "  1. New Game         ", curses.color_pair(2))
                stdscr.addstr(idx, 46, line[46:], curses.color_pair(1))
            else:
                stdscr.addstr(idx, 0, line, curses.color_pair(1))
        elif idx == 12:
            if current_option == 2:
                stdscr.addstr(idx, 0, line[:26], curses.color_pair(1))
                stdscr.addstr(idx, 26, "  2. Load Game        ", curses.color_pair(2))
                stdscr.addstr(idx, 46, line[46:], curses.color_pair(1))
            else:
                stdscr.addstr(idx, 0, line, curses.color_pair(1))
        elif idx == 13:
            if current_option == 3:
                stdscr.addstr(idx, 0, line[:26], curses.color_pair(1))
                stdscr.addstr(idx, 26, "  3. Rules             ", curses.color_pair(2))
                stdscr.addstr(idx, 46, line[46:], curses.color_pair(1))
            else:
                stdscr.addstr(idx, 0, line, curses.color_pair(1))
        elif idx == 14:
            if current_option == 4:
                stdscr.addstr(idx, 0, line[:26], curses.color_pair(1))
                stdscr.addstr(idx, 26, "  4. Quit Game        ", curses.color_pair(2))
                stdscr.addstr(idx, 46, line[46:], curses.color_pair(1))
            else:
                stdscr.addstr(idx, 0, line, curses.color_pair(1))
        else:
            stdscr.addstr(idx, 0, line, curses.color_pair(1))
    stdscr.refresh()

def main(stdscr):
    # Configuration initiale
    curses.curs_set(0)  # Masquer le curseur
    stdscr.nodelay(1)   # Ne pas bloquer lors de la lecture des entrées
    stdscr.timeout(100) # Délai pour la lecture des entrées

    current_option = 1

    while True:
        stdscr.clear()
        draw_menu(stdscr, current_option)

        key = stdscr.getch()

        if key == curses.KEY_UP | key == ord('w'):
            current_option = max(1, current_option - 1)
        elif key == curses.KEY_DOWN | key == ord('s'):
            current_option = min(4, current_option + 1)
        elif key == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)
