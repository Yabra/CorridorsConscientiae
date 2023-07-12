import pygame


def add_brightness(image: pygame.Surface, brightness: int) -> pygame.Surface:
    new_image = image.copy()
    new_image.fill((brightness, brightness, brightness), special_flags=pygame.BLEND_RGB_ADD)

    return new_image
