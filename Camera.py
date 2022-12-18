import pygame


class Camera:
    # pos - изначальная позиция камеры (pygame.math.Vector2)
    def __init__(self, pos):
        self.pos = pos
        self.start_pos = pos
        self.end_pos = pos
        self.time = 0

    # end_pos - позиция куда камера будет передвигаться (pygame.math.Vector2)
    def move_to(self, end_pos):
        self.start_pos = self.pos
        self.end_pos = end_pos
        self.time = 0

    def update(self, ticks):
        self.time += ticks

        if self.time > 1000:
            self.time = 1000

        self.pos = self.start_pos + (self.end_pos - self.start_pos) / 1000 * self.time

    def draw(self, screen, sprites):
        dx = -(self.pos.x - screen.get_size()[0] // 2)
        dy = -(self.pos.y - screen.get_size()[1] // 2)

        for s in sprites:
            s.rect.x += dx
            s.rect.y += dy

        sprites.draw(screen)

        for s in sprites:
            s.rect.x -= dx
            s.rect.y -= dy
