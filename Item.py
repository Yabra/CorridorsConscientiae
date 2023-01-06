import pygame
from data_loader import load_image


class Item(pygame.sprite.Sprite):
    # pos            - координаты
    # collision_func - функция, вызывающаяся при столкновении игрока и предмета
    # img_name       - имя файла с изображением объекта
    def __init__(self, name, pos, collision_func, img_name):
        self.name = name
        self.collision_func = collision_func
        self.pos = pos
        super().__init__()
        self.image = load_image(f"{img_name}.png")
        self.rect = self.image.get_rect()
