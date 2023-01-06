import pygame
from data_loader import load_image


class Monster(pygame.sprite.Sprite):
    # name - имя
    # pos - позиция
    # img_name - адрес картинки монстра
    # damage - урон монстра
    # collision_func - функция вызываемая при столкновении игрока и монстра
    def __init__(self, name, pos, img_name, damage, collision_func):
        self.name = name
        self.pos = pos
        self.damage = damage
        self.collision_func = collision_func
        super().__init__()
        self.image = load_image(f"{img_name}.png")
        self.rect = self.image.get_rect()

    def update(self, player):
        pass

