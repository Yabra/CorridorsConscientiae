import pygame
from data_loader import load_image
from Tile import Tile, TileType


class Labyrinth:
    def __init__(self, sprites_group, size):
        tile_size = load_image("floor.png").get_width()
        self.size = size
        self.tiles_group = pygame.sprite.Group()
        self.sprites_group = sprites_group
        self.tiles = [[None for y in range(size[0])] for x in range(size[1])]

        for x in range(size[0]):
            for y in range(size[1]):
                tile_type = TileType.FLOOR

                if x == 0 or y == 0 or x == size[0] - 1 or y == size[1] - 1:
                    tile_type = TileType.WALL
                if x == y == 3:
                    tile_type = TileType.WALL

                Tile(sprites_group, self.tiles_group, tile_type, (x * tile_size, y * tile_size))
