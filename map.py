from tile import *
import random

class Map:
    def __init__(self, width = 38, height = 20):
        self.width = width
        self.height = height
        self.map = self.generate_map()
        self.generate_patch(Tile('w'), 2, 5, 7)
        self.generate_patch(Tile('s'), 3, 3, 6)
        self.generate_patch(Tile('m'), 2, 4, 7)
        self.generate_patch(Tile('f'), 5, 5, 10)
        self.generate_shop(0.5)

    def generate_map(self):
        return [[grass for _ in range(self.width)] for _ in range(self.height)]

    def display(self):
        for row in self.map:
            print(''.join(row))
            
    def to_dict(self):
        return {
            'width': self.width,
            'height': self.height,
            'map': [[tile.to_dict() for tile in row] for row in self.map]
        }

    @classmethod
    def from_dict(cls, map_dict):
        map_instance = cls(map_dict['width'], map_dict['height'])
        map_instance.map = [[Tile.from_dict(tile) for tile in row] for row in map_dict['map']]
        return map_instance
    
    def generate_patch(self, tile: Tile, num_patches: int, min_length: int, max_length: int, irregular: bool = True) -> None:
        for _ in range(num_patches):
            # Ensure patch dimensions are within the map boundaries
            width = random.randint(min_length, min(max_length, self.width - 2))
            height = random.randint(min_length, min(max_length, self.height - 2))
            
            # Randomly select the starting point within valid range
            x = random.randint(1, self.width - width - 1)
            y = random.randint(1, self.height - height - 1)
            
            for i in range(height):
                if irregular:
                    width = random.randint(int(0.7 * max_length), max_length)
                    width = min(width, self.width - 2)
                    init_x = x + random.randint(-2, 2)
                    init_x = max(1, min(init_x, self.width - width - 1))
                else:
                    init_x = x

                for j in range(width):
                    if 0 <= (y + i) < self.height and 0 <= (init_x + j) < self.width:
                        self.map[y + i][init_x + j] = tile
                    else:
                        break  # Exit if out of bounds
        
    def generate_shop(self, probability: float) -> None:
        if random.random() < probability:
            shop_x = random.randint(1, self.width - 2)
            shop_y = random.randint(1, self.height - 2)
            self.map[shop_y][shop_x] = Tile('shop')
