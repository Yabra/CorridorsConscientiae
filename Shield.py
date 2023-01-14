import pygame

from data_loader import load_image


class Shield(pygame.sprite.Sprite):
    max_size = 90

    def __init__(self, sprites_group):
        super().__init__(sprites_group)
        self.size = 0
        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()
        self.time = 0
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, ticks, player):
        self.time += ticks
        if self.time >= 30:
            if player.mind <= 0:
                self.size = 0
            elif pygame.key.get_pressed()[pygame.K_SPACE]:
                self.size += self.time // 30
                player.change_mind(-1 * (self.time // 30))
                if self.size > Shield.max_size:
                    self.size = Shield.max_size
            else:
                self.size = 0
            self.time %= 30

        self.rect.x = player.pos.x + player.rect.w // 2 - self.size // 2
        self.rect.y = player.pos.y + player.rect.h // 2 - self.size // 2
        self.rect.w = self.size
        self.rect.h = self.size
        self.image = pygame.transform.scale(load_image("shield.png"), (self.size, self.size))
        self.mask = pygame.mask.from_surface(self.image)
