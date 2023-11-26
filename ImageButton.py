from typing import Callable

import pygame

from ButtonBase import ButtonBase
from add_brightness import add_brightness
from data_loader import load_image


class ImageButton(ButtonBase):
    # image_name - имя файла изображения
    # pos        - кортеж с 2 координатами левого верхнего угла кнопки
    # click_func - функция, вызывающаяся при нажатии на кнопку
    def __init__(self, pos: pygame.Vector2, click_func: Callable[[], None], image_name: str):
        self.image: pygame.Surface = load_image(image_name)
        self.default_rect: pygame.Rect = pygame.Rect(
            pos[0] - self.image.get_width() // 2,
            pos[1] - self.image.get_height() // 2,
            self.image.get_width(),
            self.image.get_height()
        )

        self.highlight_image: pygame.Surface = add_brightness(self.image, 30)
        self.highlight_image = pygame.transform.scale(
            self.highlight_image, (self.image.get_width() * 1.1, self.image.get_height() * 1.1)
        )

        self.highlight_rect: pygame.Rect = pygame.Rect(
            pos[0] - self.highlight_image.get_width() // 2,
            pos[1] - self.highlight_image.get_height() // 2,
            self.highlight_image.get_width(),
            self.highlight_image.get_height()
        )

        super().__init__(self.default_rect, click_func)

    def draw(self, screen: pygame.Surface) -> None:
        if self.highlight:
            self.set_rect(self.highlight_rect)
            screen.blit(self.highlight_image, (self.rect.x, self.rect.y))
        else:
            self.set_rect(self.default_rect)
            screen.blit(self.image, (self.rect.x, self.rect.y))
