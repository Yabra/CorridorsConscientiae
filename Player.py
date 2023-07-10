import pygame

from AnimatedSprite import AnimatedSprite
from Shield import Shield
from Tile import TileType
from data_loader import load_animation, load_sound

ALT_K_W = 1094
ALT_K_A = 1092
ALT_K_S = 1099
ALT_K_D = 1074


class Player(AnimatedSprite):
    speed = 3
    max_mind = 500

    # sprites_group - группа всех спрайтов для отрисовки камерой
    # pos           - изначальная позиция игрока (pygame.math.Vector2)
    def __init__(self, sprites_group, pos, mind):
        self.idle_anim = load_animation("player_idle", 1, 8)
        self.run_anim = load_animation("player_run", 4, 8)

        super().__init__(self.idle_anim, sprites_group)
        self.pos = pos
        self.mask = pygame.mask.from_surface(self.image)
        self.shield = Shield(sprites_group)
        self.mind = mind
        self.is_left = False
        self.time = 0

    # labyrinth - объект Labyrinth
    def update(self, time, labyrinth, items_group):
        self.time += time
        self.shield.update(time, self)
        # собираем нажатые клавиши для определения вектора движения
        movement = pygame.math.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[ALT_K_A]:
            movement.x -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[ALT_K_D]:
            movement.x += 1
        if keys[pygame.K_UP] or keys[pygame.K_w] or keys[ALT_K_W]:
            movement.y -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s] or keys[ALT_K_S]:
            movement.y += 1
        if keys[pygame.K_SPACE] and self.mind > 0:  # блокируем передвижение игрока при использовании щита
            movement = pygame.math.Vector2(0, 0)

        if movement.length() > 0:
            if self.time > 300:
                load_sound("step.wav", 0.5).play()
                self.time = 0
            if self.animation != self.run_anim:
                self.animation = self.run_anim

            # нормализуем вектор для одинаковой скорости во всех напоравлениях
            movement = movement.normalize() * time / 1000 * 50

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

        super().update(time)
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
