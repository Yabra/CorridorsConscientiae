import pygame

from Animation import Animation


class AnimatedSprite(pygame.sprite.Sprite):
    """
    Описание:
        Данный класс предоставляет функционал анимированного спрайта

    Аттрибуты:
        animation : Animation
            Объект класса Animation, содержащий все кадры анимации
        rect : pygame.Rect
            Квадрат, описывающий размеры кадров анимации
        image : pygame.Surface
            Изображение, использующееся для отрисовки спрайта при отрисовке группы
    """

    def __init__(self, animation: Animation, *groups: pygame.sprite.Group):
        """
        :param animation:
            Объект класса Animation, содержащий все кадры анимации
        :param groups:
            Группы спрайтов типа pygame.sprite.Group, в которые будет добавлен спрайт при создании
        """

        super().__init__(*groups)
        self.animation: Animation = animation
        self.rect: pygame.Rect = self.animation.get_current_frame().get_rect()
        self.image: pygame.Surface = self.animation.get_current_frame()

    def update(self, time: int) -> None:
        """
        Обновляет кадр анимации. Должен вызываться перед отрисовкой

        :param time:
            Время в милисекундах, прошедшее с прошлого обновления спрайта
        """

        self.animation.update(time)
        self.image = self.animation.get_current_frame()

    def get_animation(self) -> Animation:
        """
        Возвращает анимацию спрайта

        :return:
            Анимация спрайта
        """
        return self.animation

    def set_animation(self, new_animation: Animation) -> None:
        """
        Устанавливает новую анимацию для данного анимированного спрайта

        :param new_animation:
        """
        self.animation = new_animation
        self.rect = self.animation.get_current_frame().get_rect()
        self.image = self.animation.get_current_frame()
