import pygame


class Camera:
    # pos - изначальная позиция камеры (pygame.math.Vector2)
    def __init__(self, pos: pygame.Vector2):
        self.pos: pygame.Vector2 = pos
        self.start_pos: pygame.Vector2 = pos
        self.end_pos: pygame.Vector2 = pos
        self.time: int = 0

    # end_pos - позиция куда камера будет медленно передвигаться (pygame.math.Vector2)
    def move_to(self, end_pos: pygame.Vector2):
        self.start_pos = self.pos
        self.end_pos = end_pos
        self.time = 0

    def update(self, time: int):
        self.time += time

        if self.time > 1000:
            self.time = 1000

        self.pos = self.start_pos + (self.end_pos - self.start_pos) / 1000 * self.time

    def draw(self, screen: pygame.Surface, sprites: pygame.sprite.Group):
        dx: int = int(self.pos.x) - screen.get_size()[0] // 2
        dy: int = int(self.pos.y) - screen.get_size()[1] // 2

        for s in sprites:
            s.rect.x -= dx
            s.rect.y -= dy

        sprites.draw(screen)

        for s in sprites:
            s.rect.x += dx
            s.rect.y += dy
