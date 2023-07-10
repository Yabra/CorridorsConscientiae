from typing import Callable

import pygame

from ButtonBase import ButtonBase
from data_loader import load_font


class TextButton(ButtonBase):
    # text       - отображаемый в кнопке текст
    # pos        - кортеж с координатами центра кнопки
    # click_func - функция, вызывающаяся при нажатии на кнопку
    # color      - цвет текста
    # font_size  - размер отображаемого текста
    def __init__(self, pos: pygame.Vector2, click_func: Callable[[], None], text: str, font_size: int = 50,
                 color: pygame.Color = (0, 0, 0)):
        self.text: str = text
        self.color: pygame.Color = color
        self.font_size: int = font_size
        self.font: pygame.font.Font = load_font("test.ttf", self.font_size)
        self.rendered_text: pygame.Surface = self.font.render(self.text, True, self.color)
        self.rect: pygame.Rect = pygame.Rect(
            pos[0] - self.rendered_text.get_width() // 2,
            pos[1] - self.rendered_text.get_height() // 2,
            self.rendered_text.get_width(),
            self.rendered_text.get_height()
        )

        super().__init__(self.rect, click_func)

    def draw(self, screen) -> None:
        screen.blit(self.rendered_text, (self.rect.x, self.rect.y))
