import pygame

from data_loader import load_font


# Класс кнопки
class Button:
    # text       - отображаемый в кнопке текст
    # pos        - кортеж с 2 координатами левого верхнего угла кнопки
    # click_func - функция, вызывающаяся при нажатии на кнопку
    # color      - цвет текста
    # font_size  - размер отображаемого текста
    def __init__(self, text, pos, click_func, color=(0, 0, 200), font_size=50):
        self.text = text
        self.click_func = click_func
        self.color = color
        self.font_size = font_size

        self.font = load_font("test.ttf", self.font_size)
        text = self.font.render(self.text, True, self.color)
        self.rect = pygame.Rect(pos[0] - 10, pos[1] - 10, text.get_width() + 10, text.get_height() + 10)

    # pos - позиция клика
    def check_click(self, pos):
        if (
                (self.rect.left <= pos[0] <= self.rect.left + self.rect.width)
                and
                (self.rect.top <= pos[1] <= self.rect.top + self.rect.height)
        ):
            self.click_func()

    def draw(self, screen):
        text = self.font.render(self.text, True, self.color)
        screen.blit(text, (self.rect.left + 5, self.rect.top + 5))
