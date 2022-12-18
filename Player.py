import pygame
from data_loader import load_image


class Player(pygame.sprite.Sprite):
    speed = 3

    def __init__(self, sprites_group, x, y):
        super().__init__(sprites_group)
        self.x = x
        self.y = y
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
            self.x += movement.x
            self.y += movement.y

        self.rect.x = self.x
        self.rect.y = self.y
