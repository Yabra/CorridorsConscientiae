import pygame


class AnimatedSprite(pygame.sprite.Sprite):
    # animation - объект класса Animation. Все кадры должны быть одного размера
    def __init__(self, animation):
        super().__init__()
        self.animation = animation
        self.rect = self.animation.get_current_frame().get_rect()
        self.image = self.animation.get_current_frame()

    # update должен вызываться перед отрисовкой для обновления кадра на текущий
    # ticks - количество прошедших милисекунд
    def update(self, ticks):
        self.animation.update(ticks)
        self.image = self.animation.get_current_frame()
