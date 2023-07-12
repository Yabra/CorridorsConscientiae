from typing import List, Callable

import pygame


class Animation:
    """
    Описание:
        Данный класс является контейнером для кадров анимации и контроллером их обновления

    Аттрибуты:
        frames : List[pygame.Surface]
            Список, содержащий все кадры анимации

        fps : int
            Количество кадров, сменяющихся за одну секуду

        loop : bool
            Будет ли анимация циклично повторяться

        animation_end_func : Callable[[], None]
            Функция, вызывающаяся при окончании незацикленной анимации

        stopped : bool
            Остановлена ли анимация

        current_frame_num : int
            Номер текущего кадра анимации

        time : int
            Время в миллисекундах, прошедшее со смены последнего кадра
    """

    def __init__(self, frames: List[pygame.Surface], fps: int, loop: bool = True,
                 animation_end_func: Callable[[], None] = lambda: None):
        """
        :param frames:
            Список кадров анимации типа pygame.Surface
        :param fps:
            Количество кадров, сменяющихся за секунду
        :param loop:
            Будет ли анимация циклично повторяться
        :param animation_end_func:
            Функция, вызывающаяся при окончании незацикленной анимации
        """

        self.frames: List[pygame.Surface] = frames
        self.fps: int = fps
        self.loop: bool = loop
        self.animation_end_func: Callable[[], None] = animation_end_func

        self.stopped: bool = False
        self.current_frame_num: int = 0
        self.time: int = 0

    def update(self, time: int) -> None:
        """
        Обновляет кадр анимации. Должен вызываться перед отрисовкой

        :param time:
            Время в миллисекундах, прошедшее со смены последнего кадра
        """

        if self.stopped:
            return

        self.time += time
        self.current_frame_num += self.time // (1000 // self.fps)
        self.time %= 1000 // self.fps

        if self.loop:
            self.current_frame_num %= len(self.frames)
        else:
            self.current_frame_num = len(self.frames) - 1
            self.animation_end_func()
            self.stopped = True

    def get_current_frame(self) -> pygame.Surface:
        """
        Получение текущего кадра анимации

        :return:
            Текущий кадр анимации
        """

        return self.frames[self.current_frame_num]

    def reset_to_first_frame(self) -> None:
        """
        Возвращает анимацию к первому кадру
        """

        self.current_frame_num = 0
        self.time = 0

    def get_fps(self) -> int:
        """
        Возвращает скорость анимации

        :return:
            Скорость анимации
        """

        return self.fps

    def is_looped(self) -> bool:
        """
        Возвращает зациклена ли анимация

        :return:
            Зациклена ли анимация
        """

        return self.loop

    def get_animation_end_func(self) -> Callable[[], None]:
        """
        Возвращает функцию, вызывающуюся при окончании незацикленной анимации

        :return:
            Функция, вызывающаяся при окончании незацикленной анимации
        """

        return self.animation_end_func

    def is_stopped(self) -> bool:
        """
        Возвращает остановлена ли анимация

        :return:
            Остановлена ли анимация
        """
        return self.stopped

    def get_current_frame_num(self) -> int:
        """
        Возвращает номер текущего кадра анимации

        :return:
            Номер текущего кадра анимации
        """

        return self.current_frame_num

    def set_fps(self, fps: int) -> None:
        """
        Устанавливает скорость анимации
        """

        self.fps = fps

    def set_loop(self, loop: int) -> None:
        """
        Устанавливает циклична ли анимация

        :param loop:
            Цикличность анимации
        """

        self.loop = loop

    def set_animation_end_func(self, animation_end_func: Callable[[], None]) -> None:
        """
        Устанавливает функцию, вызывающуюся при окончании незацикленной анимации

        :param animation_end_func:
            Функция, вызывающаяся при окончании незацикленной анимации
        """

        self.animation_end_func = animation_end_func

    def play(self) -> None:
        """
        Запускает анимацию
        """

        self.stopped = False

    def stop(self) -> None:
        """
        Останавливает анимацию
        """

        self.stopped = True

    def set_current_frame_num(self, current_frame_num: int) -> None:
        """
        Устанавливает текущий кадр анимации
        """

        self.current_frame_num = current_frame_num
