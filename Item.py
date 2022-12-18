import pygame


class Item(pygame.sprite.Sprite):
    # pos            - координаты
    # collision_func - функция, вызывающаяся при столкновении игрока и предмета
    def __init__(self, name, pos, collision_func):
        self.name = name
        self.collision_func = collision_func
        self.pos = pos
        super().__init__()

