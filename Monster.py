import pygame
from data_loader import load_image


class Monster(pygame.sprite.Sprite):
    speed = 2
    distance = 500

    def __init__(self, sprites_group, monsters_group, pos, collision_func, image_name):
        super().__init__(sprites_group, monsters_group)
        self.sprites_group = sprites_group
        self.monsters_group = monsters_group
        self.pos = pos
        self.collision_func = collision_func
        self.image = load_image(image_name)
        self.rect = self.image.get_rect()

    def update(self, player):
        if pygame.sprite.collide_rect(self, player):
            self.collision_func()
            self.sprites_group.remove(self)
            self.monsters_group.remove(self)

        if (self.pos - player.pos).length() <= Monster.distance:
            self.pos += (player.pos - self.pos).normalize() * Monster.speed

        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
