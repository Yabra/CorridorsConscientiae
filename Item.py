import pygame
from data_loader import load_image


class Item(pygame.sprite.Sprite):
    # pos            - координаты
    # collision_func - функция, вызывающаяся при столкновении игрока и предмета
    # img_name       - имя файла с изображением объекта
    def __init__(self, sprites_group, items_group, pos, collision_func, image_name):
        super().__init__(sprites_group, items_group)
        self.sprites_group = sprites_group
        self.items_group = items_group
        self.collision_func = collision_func
        self.image = load_image(image_name)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos

    def collide(self):
        self.collision_func()
        self.sprites_group.remove(self)
        self.items_group.remove(self)
