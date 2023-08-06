import pygame


def add_brightness(image: pygame.Surface, brightness: int) -> pygame.Surface:
    """
    Функция для увеличения яркости изображения

    :param image:
        Исходное изображение
    :param brightness:
        Число, определяющее увеличение яркости изображения
    :return:
        Копия изображения с увеличенной яркостью
    """

    new_image: pygame.Surface = image.copy()
    new_image.fill((brightness, brightness, brightness), special_flags=pygame.BLEND_RGB_ADD)

    return new_image
