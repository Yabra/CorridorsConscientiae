import pygame
from AnimatedSprite import AnimatedSprite
from data_loader import load_animation, load_sound


class Monster(AnimatedSprite):
    speed = 90
    distance = 500

    def __init__(self, sprites_group, monsters_group, pos, collision_func):
        super().__init__(load_animation("monster_run", 2, 10), sprites_group, monsters_group)
        self.sprites_group = sprites_group
        self.monsters_group = monsters_group
        self.pos = pos
        self.collision_func = collision_func
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.is_left = False

    def update(self, ticks, player):
        super().update(ticks)

        if pygame.sprite.collide_mask(self, player.shield):
            self.sprites_group.remove(self)
            self.monsters_group.remove(self)
            load_sound("damage.wav", 0.5).play()
            return

        if pygame.sprite.collide_mask(self, player):
            self.collision_func()
            self.sprites_group.remove(self)
            self.monsters_group.remove(self)
            load_sound("damage.wav", 0.5).play()
            return

        if (self.pos - player.pos).length() <= Monster.distance:
            movement = (player.pos - self.pos).normalize() * Monster.speed * ticks / 1000
            self.pos += movement

            if movement.x < 0:
                self.is_left = True
            elif movement.x > 0:
                self.is_left = False

        super().update(ticks)
        self.image = pygame.transform.flip(self.image, self.is_left, False)
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
