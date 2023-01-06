import pygame


class Slider:
    # x - координата левого верхнего угла прямоугольника
    # y - координата левого верхнего угла прямоугольника
    # h - высота прямоугольника
    # w - ширина прямоугольника
    # r - радиус круга
    def __init__(self, x, y, h, w, r, circle_color, rect_color, screen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.r = r
        self.circle_color = circle_color
        self.rect_color = rect_color
        self.slider_x = self.x
        self.screen = screen

    def draw_slider(self):
        pygame.draw.rect(self.screen, self.rect_color, (self.x, self.y,  self.w, self.h))
        pygame.draw.circle(self.screen, self.circle_color, (self.slider_x, self.y + self.h // 2), self.r)

    # возвращает значение в %
    def value(self):
        return int((self.slider_x - self.x) / self.w * 100)

    # эту функцию нужно вызывать в постоянно, чтобы круг не выходил за границы
    def check(self):
        button = pygame.mouse.get_pressed()
        if button[0]:
            pos = pygame.mouse.get_pos()
            x = pos[0]
            y = pos[1]
            if (
                self.y + self.h // 2 - self.r < y < self.y + self.h // 2 + self.r
                and
                self.slider_x - self.r < x < self.slider_x + self.r
            ):
                if x > self.x + self.w:
                    self.slider_x = self.x + self.w
                elif x < self.x:
                    self.slider_x = self.x
                else:
                    self.slider_x = x
