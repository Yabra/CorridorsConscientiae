from typing import List

import pygame


class Animation:
    """
    Описание:
        Данный класс является контейнером для кадров анимации и контроллером их обновления

    Аттрибуты:
        frames : List[pygame.Surface]
            Список, содержащий все кадры анимации
        current_frame : int
            Номер текущего кадра анимации
        fps : int
            Количество кадров, сменяющихся за одну секуду
        time : int
            Время в миллисекундах, прошедшее со смены последнего кадра

    Методы:
        update(time: int) -> None
            Обновляет кадр анимации. Должен вызываться перед отрисовкой
        get_current_frame() -> pygame.Surface
            Получение текущего кадра анимации
    """

    def __init__(self, frames: List[pygame.Surface], fps: int):
        """
        :param frames:
            Список кадров анимации типа pygame.Surface
        :param fps:
            Количество кадров, сменяющихся за секунду
        """
        self.frames: List[pygame.Surface] = frames
        self.current_frame: int = 0
        self.fps: int = fps
        self.time: int = 0

    def update(self, time: int) -> None:
        """
        Обновляет кадр анимации. Должен вызываться перед отрисовкой

        :param time:
            Время в миллисекундах, прошедшее со смены последнего кадра
        """
        self.time += time
        self.current_frame += self.time // (1000 // self.fps)
        self.time %= 1000 // self.fps
        self.current_frame %= len(self.frames)

    def get_current_frame(self) -> pygame.Surface:
        """
        Получение текущего кадра анимации

        :return:
            Текущий кадр анимации
        """
        return self.frames[self.current_frame]
