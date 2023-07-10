from typing import Callable

import pygame

from ButtonBase import ButtonBase
from data_loader import load_image


class ImageButton(ButtonBase):
    # image_name - имя файла изображения
    # pos        - кортеж с 2 координатами левого верхнего угла кнопки
    # click_func - функция, вызывающаяся при нажатии на кнопку
    def __init__(self, pos: pygame.Vector2, click_func: Callable[[], None], image_name: str):
        self.image: pygame.Surface = load_image(image_name)
        self.rect: pygame.Rect = pygame.Rect(pos[0], pos[1], self.image.get_width(), self.image.get_height())
        super().__init__(self.rect, click_func)

    def draw(self, screen) -> None:
        screen.blit(self.image, (self.rect.x, self.rect.y))
