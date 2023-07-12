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
    def __init__(self, pos: pygame.Vector2, click_func: Callable[[], None], text: str,
                 can_highlight: bool = True,
                 font_size: int = 50,
                 highlight_font_size: int = None,
                 color: pygame.Color = pygame.Color(0, 0, 0),
                 highlight_color: pygame.Color = None):

        self.text: str = text
        self.font_size: int = font_size

        if highlight_font_size is None:
            self.highlight_font_size: int = font_size + 5

        else:
            self.highlight_font_size: int = highlight_font_size

        self.font: pygame.font.Font = load_font("test.ttf", self.font_size)
        self.highlight_font: pygame.font.Font = load_font("test.ttf", self.highlight_font_size)

        self.color: pygame.Color = color
        self.highlight_color: pygame.Color = color + pygame.Color(50, 50, 50)

        self.rendered_text: pygame.Surface = self.font.render(self.text, True, self.color)

        if highlight_color is None:
            self.rendered_highlighted_text: pygame.Surface = self.highlight_font.render(
                self.text, True, self.highlight_color
            )

        else:
            self.rendered_highlighted_text: pygame.Surface = self.font.render(self.text, True, self.highlight_color)

        self.default_rect: pygame.Rect = pygame.Rect(
            pos[0] - self.rendered_text.get_width() // 2,
            pos[1] - self.rendered_text.get_height() // 2,
            self.rendered_text.get_width(),
            self.rendered_text.get_height()
        )

        self.highlight_rect: pygame.Rect = pygame.Rect(
            pos[0] - self.rendered_highlighted_text.get_width() // 2,
            pos[1] - self.rendered_highlighted_text.get_height() // 2,
            self.rendered_highlighted_text.get_width(),
            self.rendered_highlighted_text.get_height()
        )

        super().__init__(self.default_rect, click_func, can_highlight)

    def draw(self, screen) -> None:
        if self.highlight:
            self.set_rect(self.highlight_rect)
            screen.blit(self.rendered_highlighted_text, (self.rect.x, self.rect.y))
        else:
            self.set_rect(self.default_rect)
            screen.blit(self.rendered_text, (self.rect.x, self.rect.y))
