import pygame
from Tile import TileType
from Shield import Shield
from AnimatedSprite import AnimatedSprite

from data_loader import load_animation


class Player(AnimatedSprite):
    speed = 3
    max_mind = 500

    # sprites_group - группа всех спрайтов для отрисовки камерой
    # pos           - изначальная позиция игрока (pygame.math.Vector2)
    def __init__(self, sprites_group, pos):
        self.idle_anim = load_animation("player_idle", 1, 8)
        self.run_anim = load_animation("player_run", 4, 8)

        super().__init__(self.idle_anim, sprites_group)
        self.pos = pos
        self.mask = pygame.mask.from_surface(self.image)
        self.shield = Shield(sprites_group)
        self.mind = Player.max_mind
        self.is_left = False

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
        if keys[pygame.K_SPACE] and self.mind > 0:  # блокируем передвижение игрока при использовании щита
            movement = pygame.math.Vector2(0, 0)

        if movement.length() > 0:
            if self.animation != self.run_anim:
                self.animation = self.run_anim
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

        else:
            self.animation = self.idle_anim

        if movement.x < 0:
            self.is_left = True
        elif movement.x > 0:
            self.is_left = False

        super().update(ticks)
        self.image = pygame.transform.flip(self.image, self.is_left, False)
        self.mask = pygame.mask.from_surface(self.image)

        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

        items_collide = pygame.sprite.spritecollide(self, items_group, False)
        for i in items_collide:
            i.collide()

    def change_mind(self, value):
        self.mind += value
        if self.mind < 0:
            self.mind = 0
        elif self.mind > Player.max_mind:
            self.mind = Player.max_mind
