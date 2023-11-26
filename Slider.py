import pygame


class Slider:
    clamped_slider = None

    # x - координата левого верхнего угла прямоугольника
    # y - координата левого верхнего угла прямоугольника
    # h - высота прямоугольника
    # w - ширина прямоугольника
    # r - радиус круга
    def __init__(self,
                 x: int, y: int, h: int, w: int, r: int,
                 circle_color: pygame.Color, rect_color: pygame.Color,
                 screen: pygame.Surface):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = r
        self.circle_color = circle_color
        self.rect_color = rect_color
        self.slider_x = self.x
        self.screen = screen

    def draw_slider(self) -> None:
        pygame.draw.rect(self.screen, self.rect_color, (self.x, self.y, self.w, self.h))
        pygame.draw.circle(self.screen, self.circle_color, (self.slider_x, self.y + self.h // 2), self.r)

    def set_value(self, value: int) -> None:
        self.slider_x = self.x + self.w / 100 * value

    # возвращает значение в %
    def value(self) -> int:
        return int((self.slider_x - self.x) / self.w * 100)

    # эту функцию нужно вызывать в постоянно, чтобы круг не выходил за границы
    def check(self) -> None:
        button = pygame.mouse.get_pressed()
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]

        if button[0]:
            if (
                    self.y + self.h // 2 - self.r < y < self.y + self.h // 2 + self.r
                    and
                    self.slider_x - self.r < x < self.slider_x + self.r
            ):
                Slider.clamped_slider = self

        else:
            Slider.clamped_slider = None

        if Slider.clamped_slider == self:
            if x > self.x + self.w:
                self.slider_x = self.x + self.w
            elif x < self.x:
                self.slider_x = self.x
            else:
                self.slider_x = x
