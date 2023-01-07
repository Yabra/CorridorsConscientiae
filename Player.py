import pygame
from Tile import TileType
from Shield import Shield

from data_loader import load_image


class Player(pygame.sprite.Sprite):
    speed = 3

    # sprites_group - группа всех спрайтов для отрисовки камерой
    # pos           - изначальная позиция игрока (pygame.math.Vector2)
    def __init__(self, sprites_group, pos):
        super().__init__(sprites_group)
        self.pos = pos
        self.image = load_image("test.png")
        self.rect = self.image.get_rect()
        self.shield = Shield(sprites_group)

    # labyrinth - объект Labyrinth
    def update(self, ticks, labyrinth, items_group):
        self.shield.update(ticks, self)
        # собираем нажатые клавиши для определения вектора движения
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
        if keys[pygame.K_SPACE]:
            movement = pygame.math.Vector2(0, 0)

        if movement.length() > 0:
            movement = movement.normalize()  # нормализуем вектор для одинаковой скорости во всех напоравлениях

            for i in range(Player.speed):  # цикл для постепенного движения, чтобы персонаж не залипал в стенах
                self.pos += movement
                self.rect.x = self.pos.x
                self.rect.y = self.pos.y

                # проверки на столкновение со стенами и обратное движение в этом случае
                for t in pygame.sprite.spritecollide(self, labyrinth.tiles_group, False):
                    if t.tile_type == TileType.WALL:
                        if (
                                t.rect.y <= self.rect.y
                                and
                                (
                                    (t.rect.x <= self.rect.x <= t.rect.x + t.rect.w)
                                    or
                                    (self.rect.x <= t.rect.x <= self.rect.x + self.rect.w)
                                )
                                and
                                movement.y < 0
                        ):
                            self.pos.y -= movement.y

                        elif (
                                t.rect.y >= self.rect.y
                                and
                                (
                                    (t.rect.x <= self.rect.x <= t.rect.x + t.rect.w)
                                    or
                                    (self.rect.x <= t.rect.x <= self.rect.x + self.rect.w)
                                )
                                and
                                movement.y > 0
                        ):
                            self.pos.y -= movement.y

                        if (
                                t.rect.x <= self.rect.x
                                and
                                (
                                    (t.rect.y <= self.rect.y <= t.rect.y + t.rect.h)
                                    or
                                    (self.rect.y <= t.rect.y <= self.rect.y + self.rect.h)
                                )
                                and
                                movement.x < 0
                        ):
                            self.pos.x -= movement.x

                        elif (
                                t.rect.x >= self.rect.x
                                and
                                (
                                    (t.rect.y <= self.rect.y <= t.rect.y + t.rect.h)
                                    or
                                    (self.rect.y <= t.rect.y <= self.rect.y + self.rect.h)
                                )
                                and
                                movement.x > 0
                        ):
                            self.pos.x -= movement.x

        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

        items_collide = pygame.sprite.spritecollide(self, items_group, False)
        for i in items_collide:
            i.collide()
