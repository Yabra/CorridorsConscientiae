import pygame

from data_loader import load_image


# Класс изображения
class Image:
    # pos        - кортеж с 2 координатами левого верхнего угла изображения
    # image_name - имя файла с изображением
    def __init__(self, pos: pygame.Vector2, image_name: str):
        self.pos: pygame.Vector2 = pos
        self.image: pygame.Surface = load_image(image_name)

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.pos)
