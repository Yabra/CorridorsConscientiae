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
    def __init__(self,
                 x: int, y: int, h: int, w: int,
                 max_value: int, value: int, is_right: bool,
                 background_color: pygame.Color, foreground_color: pygame.Color,
                 screen: pygame.Surface):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.background_color = background_color
        self.foreground_color = foreground_color
        self.screen = screen
        self.max_value = max_value
        self.is_right = is_right
        self.value = value

    def draw_scale(self) -> None:
        pygame.draw.rect(self.screen, self.background_color, (self.x, self.y, self.w, self.h))
        if self.is_right:
            pygame.draw.rect(self.screen, self.foreground_color,
                             (self.x, self.y, (self.w * self.value / self.max_value), self.h))
        else:
            x = self.x + self.w - self.w * self.value / self.max_value
            pygame.draw.rect(self.screen, self.foreground_color,
                             (x, self.y, (self.w * self.value / self.max_value), self.h))

    # можно задать новое значение value
    def update(self, new_value: int) -> None:
        self.value = new_value
