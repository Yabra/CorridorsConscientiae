import pygame
from data_loader import load_image


# Типы тайлов
class TileType:
    FLOOR = 0
    WALL = 1


class Tile(pygame.sprite.Sprite):
    # sprites_group - группа спрайтов для отрисовки камеров
    # tiles_group   - группа тайлов для проверки столкновений игрока с тайлами
    # tile_type     - значение из TileType
    # pos           - позиция тайла относительно центра координат
    def __init__(self, sprites_group, tiles_group, tile_type, pos):
        super().__init__(sprites_group, tiles_group)
        self.tile_type = tile_type
        if tile_type == TileType.FLOOR:
            self.image = load_image("floor.png")
        elif tile_type == TileType.WALL:
            self.image = load_image("wall.png")
        self.rect = pygame.rect.Rect(pos[0], pos[1], self.image.get_rect().width, self.image.get_rect().height)
