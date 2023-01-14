import pygame

from data_loader import load_image, load_sound


class ImageButton:
    # image_name - имя файла изображения
    # pos        - кортеж с 2 координатами левого верхнего угла кнопки
    # click_func - функция, вызывающаяся при нажатии на кнопку
    def __init__(self, image_name, pos, click_func):
        self.click_func = click_func
        self.image = load_image(image_name)
        self.rect = pygame.Rect(pos[0], pos[1], self.image.get_width(), self.image.get_height())

    # check_click вызывается при событии отпускания кнопки мыши
    # pos - позиция клика
    def check_click(self, pos):
        if (
                (self.rect.x <= pos[0] <= self.rect.x + self.rect.w)
                and
                (self.rect.y <= pos[1] <= self.rect.y + self.rect.h)
        ):
            load_sound("click.wav", 1.0).play()
            self.click_func()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
