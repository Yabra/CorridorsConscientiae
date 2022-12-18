import pygame


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, animation):
        super().__init__()
        self.animation = animation
        self.rect = self.animation.get_current_frame().get_rect()

    def update(self, ticks):
        self.animation.update(ticks)
        self.image = self.animation.get_current_frame()
