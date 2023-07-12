from typing import Callable

import pygame

from data_loader import load_sound


class ButtonBase:
    """
    Описание:
        Данный класс предоставляет базовый функционал кнопки

    Аттрибуты:
        rect : pygame.Rect
            Квадрат, описывающий размеры области клика кнопки
        click_func : Callable[[], None]
            Функция, вызывающаяся при нажатии на кнопку
        can_highlight : bool
            Может ли кнопка подсвечиваться при наведении на неё
        highlight : bool
            Подсвечивается ли кнопка в данный момент
    """

    def __init__(self, rect: pygame.Rect, click_func: Callable[[], None], can_highlight: bool = True):
        """
        :param rect:
            Квадрат, описывающий размеры области клика кнопки
        :param click_func:
            Функция, вызывающаяся при нажатии на кнопку
        :param can_highlight:
            Может ли кнопка подсвечиваться при наведении на неё
        """

        self.rect: pygame.Rect = rect
        self.click_func: Callable[[], None] = click_func
        self.can_highlight = can_highlight
        self.highlight = False

    def check_highlight(self, pos: pygame.Vector2) -> None:
        """
        Проверяет, находится ли курсор над кнопкой и включает подсветку в случае,
        если курсор находится над кнопкой, включает подсветку.
        Вызывается при возниконвении события pygame.MOUSEMOTION

        :param pos:
            Позиция курсора
        :return:
        """

        if (
                (self.rect.x <= pos[0] <= self.rect.x + self.rect.w)
                and
                (self.rect.y <= pos[1] <= self.rect.y + self.rect.h)
                and
                self.can_highlight
        ):
            self.highlight = True
        else:
            self.highlight = False

    def check_click(self, pos: pygame.Vector2) -> None:
        """
        Проверяет будет ли выполнено действие кнопки. Вызывается при возниконвении события pygame.MOUSEBUTTONUP

        :param pos:
            Позиция, где была отпущена кнопка мыши
        :return:
        """

        if (
                (self.rect.x <= pos[0] <= self.rect.x + self.rect.w)
                and
                (self.rect.y <= pos[1] <= self.rect.y + self.rect.h)
        ):
            load_sound("click.wav", 1.0).play()
            self.click_func()

    def get_rect(self) -> pygame.Rect:
        """
        Возвращает квадрат, описывающий размеры области клика кнопки

        :return:
            Квадрат, описывающий размеры области клика кнопки
        """

        return self.rect

    def get_click_func(self) -> Callable[[], None]:
        """
        Возвращает функцию, вызывающуюся при нажатии на кнопку

        :return:
            Квадрат, описывающий размеры области клика кнопки
        """

        return self.click_func

    def is_can_highlight(self) -> bool:
        """
        Возвращает может ли подсвечивается кнопка

        :return:
            Может ли подсвечивается кнопка
        """

        return self.can_highlight

    def is_highlighted(self) -> bool:
        """
        Возвращает подсвечивается ли кнопка

        :return:
            Подсвечивается ли кнопка
        """

        return self.highlight

    def set_rect(self, rect: pygame.Rect) -> None:
        """
        Устанавливает квадрат, описывающий размеры области клика кнопки

        :param rect:
            Квадрат, описывающий размеры области клика кнопки
        """

        self.rect = rect

    def set_click_func(self, click_func: Callable[[], None]) -> None:
        """
        Устанавливает функцию, вызывающуюся при нажатии на кнопку

        :param click_func:
            Функция, вызывающуюся при нажатии на кнопку
        """

        self.click_func = click_func

    def set_can_highlight(self, can_highlight: bool) -> None:
        """
        Устанавливает может ли подсвечивается кнопка

        :param can_highlight:
            Может ли подсвечивается кнопка
        """

        self.can_highlight = can_highlight

    def set_highlight(self, highlight: bool) -> None:
        """
        Устанавливает подсвечивается ли кнопка

        :param highlight:
            Подсвечивается ли кнопка
        """

        self.highlight = highlight
