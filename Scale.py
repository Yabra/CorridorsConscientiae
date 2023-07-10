import pygame


class Scale:
    # x - координата прямоугольника
    # y - координата прямоугольника
    # h - высота прямоугольника
    # w - ширина прямоугольника
    # max_value  - максималное значение
    # value - текущее значение
    # backround_color - цвет не заполненной шкалы
    # foreground_color - цвет заполненной шкалы
    # is_rigth - начение типа bool, если True, то шкала заполняется справа
    def __init__(self, x, y, h, w, max_value, value, is_rigth, backround_color, foreground_color, screen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.backround_color = backround_color
        self.foreground_color = foreground_color
        self.screen = screen
        self.max_value = max_value
        self.is_right = is_rigth
        self.value = value

    def draw_scale(self):
        pygame.draw.rect(self.screen, self.backround_color, (self.x, self.y, self.w, self.h))
        if self.is_right:
            pygame.draw.rect(self.screen, self.foreground_color,
                             (self.x, self.y, (self.w * self.value / self.max_value), self.h))
        else:
            x = self.x + self.w - self.w * self.value / self.max_value
            pygame.draw.rect(self.screen, self.foreground_color,
                             (x, self.y, (self.w * self.value / self.max_value), self.h))

    # можно задать новое значение value
    def update(self, new_value):
        self.value = new_value
