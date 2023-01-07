import pygame
from data_loader import load_image


class Monster(pygame.sprite.Sprite):
    speed = 2
    distance = 500

    def __init__(self, sprites_group, monsters_group, pos, collision_func):
        super().__init__(sprites_group, monsters_group)
        self.sprites_group = sprites_group
        self.monsters_group = monsters_group
        self.pos = pos
        self.collision_func = collision_func
        self.image = load_image("test.png")
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, player):
        if pygame.sprite.collide_mask(self, player.shield):
            self.sprites_group.remove(self)
            self.monsters_group.remove(self)
            return

        if pygame.sprite.collide_mask(self, player):
            self.collision_func()
            self.sprites_group.remove(self)
            self.monsters_group.remove(self)
            return

        if (self.pos - player.pos).length() <= Monster.distance:
            self.pos += (player.pos - self.pos).normalize() * Monster.speed

        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
