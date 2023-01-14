import pygame

from data_loader import load_font, load_sound


class Button:
    # text       - отображаемый в кнопке текст
    # pos        - кортеж с координатами центра кнопки
    # click_func - функция, вызывающаяся при нажатии на кнопку
    # color      - цвет текста
    # font_size  - размер отображаемого текста
    def __init__(self, text, pos, click_func, color=(150, 0, 0), font_size=50):
        self.text = text
        self.click_func = click_func
        self.color = color
        self.font_size = font_size

        self.font = load_font("test.ttf", self.font_size)
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.rect = pygame.Rect(
            pos[0] - self.rendered_text.get_width() // 2,
            pos[1] - self.rendered_text.get_height() // 2,
            self.rendered_text.get_width(),
            self.rendered_text.get_height()
        )

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
        screen.blit(self.rendered_text, (self.rect.x, self.rect.y))
