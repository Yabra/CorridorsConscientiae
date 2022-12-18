import pygame
from data_loader import load_font


# Класс кнопки
class Text:
    # text       - оторажаемый текст
    # pos        - кортеж с 2 координатами центра текста
    # color      - цвет текста
    # font_size  - размер отображаемого текста
    def __init__(self, text, pos, color=(0, 0, 200), font_size=50):
        self.text = text
        self.color = color
        self.font_size = font_size

        self.font = load_font("test.ttf", self.font_size)
        text = self.font.render(self.text, True, self.color)
        self.pos = (pos[0] - text.get_width() // 2, pos[1] - text.get_height() // 2)

    def draw(self, screen):
        text = self.font.render(self.text, True, self.color)
        screen.blit(text, self.pos)
