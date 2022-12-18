import pygame
from Tile import TileType

from data_loader import load_image


class Player(pygame.sprite.Sprite):
    speed = 3

    # pos - изначальная позиция игрока (pygame.math.Vector2)
    def __init__(self, sprites_group, pos):
        super().__init__(sprites_group)
        self.pos = pos
        self.image = load_image("test.png")
        self.rect = self.image.get_rect()

    def update(self, labyrinth):
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

        for i in range(Player.speed):
            for t in pygame.sprite.spritecollide(self, labyrinth.tiles_group, False):
                if t.tile_type == TileType.WALL:
                    if (
                            t.rect.y <= self.pos.y
                            and
                            (
                                (t.rect.x <= self.pos.x and t.rect.x + t.rect.w >= self.pos.x)
                                or
                                (self.pos.x <= t.rect.x and self.pos.x + self.rect.w >= t.rect.x)
                            )
                            and movement.y < 0
                    ):
                        movement.y = 0

                    elif (
                            t.rect.y >= self.pos.y
                            and
                            (
                                (t.rect.x <= self.pos.x and t.rect.x + t.rect.w >= self.pos.x)
                                or
                                (self.pos.x <= t.rect.x and self.pos.x + self.rect.w >= t.rect.x)
                            )
                            and movement.y > 0
                    ):
                        movement.y = 0

                    if (
                            t.rect.x <= self.pos.x
                            and
                            (
                                (t.rect.y <= self.pos.y and t.rect.y + t.rect.h >= self.pos.y)
                                or
                                (self.pos.y <= t.rect.y and self.pos.y + self.rect.h >= t.rect.y)
                            )
                            and movement.x < 0
                    ):
                        movement.x = 0

                    elif (
                            t.rect.x >= self.pos.x
                            and
                            (
                                (t.rect.y <= self.pos.y and t.rect.y + t.rect.h >= self.pos.y)
                                or
                                (self.pos.y <= t.rect.y and self.pos.y + self.rect.h >= t.rect.y)
                            )
                            and movement.x > 0
                    ):
                        movement.x = 0

            if movement.length() > 0:
                movement.normalize()
                self.pos += movement

            self.rect.x = self.pos.x
            self.rect.y = self.pos.y
