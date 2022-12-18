import pygame

from data_loader import load_image


class Player(pygame.sprite.Sprite):
    speed = 3

    # pos - изначальная позиция игрока (pygame.math.Vector2)
    def __init__(self, sprites_group, pos):
        super().__init__(sprites_group)
        self.pos = pos
        self.image = load_image("test.png")
        self.rect = self.image.get_rect()

    def update(self):
        movement = pygame.math.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            movement.x -= 1
        if keys[pygame.K_RIGHT]:
            movement.x += 1
        if keys[pygame.K_UP]:
            movement.y -= 1
        if keys[pygame.K_DOWN]:
            movement.y += 1

        if movement.length() > 0:
            movement.normalize()
            movement *= Player.speed
            self.pos += movement

        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
