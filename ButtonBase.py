from typing import Callable

import pygame

from data_loader import load_sound


class ButtonBase:
    def __init__(self, rect: pygame.Rect, click_func: Callable[[], None]):
        self.click_func: Callable[[], None] = click_func
        self.rect: pygame.Rect = rect

    def check_click(self, pos) -> None:
        if (
                (self.rect.x <= pos[0] <= self.rect.x + self.rect.w)
                and
                (self.rect.y <= pos[1] <= self.rect.y + self.rect.h)
        ):
            load_sound("click.wav", 1.0).play()
            self.click_func()
