import mapInfos as m

class Tile:
    def __init__(self, biome = 'g'):
        self.biome = m.bioms[biome]
        
    def to_dict(self):
        return {
            'biome': self.biome
        }

    @classmethod
    def from_dict(cls, tile_dict):
        # We assume the 'biome' key contains a valid biome dictionary from m.bioms
        tile = cls()
        tile.biome = tile_dict['biome']
        return tile
        
grass = Tile('g')
water = Tile('w')
sand = Tile('s')
mountain = Tile('m')
forest = Tile('f')
shop = Tile('shop')
castle = Tile('castle')
player = Tile('player')
