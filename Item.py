from enum import Enum
from typing import Callable

import pygame

from data_loader import load_image


# Типы предметов
class ItemType(Enum):
    PORTAL = 0
    MIND_CRYSTAL = 1
    LOSTNESS_CRYSTAL = 2


class Item(pygame.sprite.Sprite):
    # pos            - координаты
    # collision_func - функция, вызывающаяся при столкновении игрока и предмета
    # img_name       - имя файла с изображением объекта
    def __init__(self, sprites_group: pygame.sprite.Group, items_group: pygame.sprite.Group, item_type: ItemType,
                 pos: pygame.Vector2, collision_func: Callable[[], None], image_name: str):
        super().__init__(sprites_group, items_group)
        self.item_type: ItemType = item_type
        self.sprites_group: pygame.sprite.Group = sprites_group
        self.items_group: pygame.sprite.Group = items_group
        self.collision_func: Callable[[], None] = collision_func
        self.image: pygame.Surface = load_image(image_name)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def collide(self) -> None:
        self.collision_func()
        self.sprites_group.remove(self)
        self.items_group.remove(self)
