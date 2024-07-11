import functions as f
import states as s

if __name__ == "__main__":
    while s.gs['run']:
        if s.gs['menu']:
            f.menu()
        if s.gs['play']:
            f.play()
        if s.gs['fight']:
            f.fight()
