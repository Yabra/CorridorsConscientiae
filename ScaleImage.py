import pygame
from data_loader import load_image


class ScaleImage:
    # x - координата прямоугольника
    # y - координата прямоугольника
    # h - высота прямоугольника
    # w - ширина прямоугольника
    # max_value  - максималное значение
    # value - текущее значение
    # backround_color - цвет не заполненной шкалы
    # foreground_color - цвет заполненной шкалы
    # is_rigth - начение типа bool, если True, то шкала заполняется справа
    def __init__(self, x, y, max_value, value, is_right, backround_texture_name, foreground_texture_name):
        self.pos = pygame.Vector2(x, y)
        self.is_right = is_right
        self.max_value = max_value
        self.value = value
        self.backround_image = load_image(backround_texture_name)
        self.foreground_image = load_image(foreground_texture_name)
        self.size = pygame.Vector2(self.backround_image.get_rect().w, self.backround_image.get_rect().h)

    def draw(self, screen):
        screen.blit(self.backround_image, self.pos)
        if self.is_right:
            screen.blit(
                self.foreground_image,
                self.pos,
                area=(0, 0, (self.size.x * self.value / self.max_value), self.size.y)
            )
        else:
            screen.blit(
                self.foreground_image,
                (self.pos.x + self.size.x - self.size.x * self.value / self.max_value + 1, self.pos.y),
                area=(
                    self.size.x - self.size.x * self.value / self.max_value, 0,
                    (self.size.x * self.value / self.max_value), self.size.y
                )
            )

    # можно задать новое значение value
    def update(self, new_value):
        self.value = new_value
