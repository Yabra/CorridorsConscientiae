import pygame

from data_loader import load_font


# Класс кнопки
class Text:
    # text       - оторажаемый текст
    # pos        - кортеж с 2 координатами центра текста
    # color      - цвет текста
    # font_size  - размер отображаемого текста
    def __init__(self,
                 text: str, pos: pygame.Vector2,
                 color: pygame.Color = pygame.Color(150, 0, 0),
                 font_size: int = 50):
        self.text = text
        self.color = color
        self.font_size = font_size
        self.center_pos = pos

        self.font = load_font("test.ttf", self.font_size)
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.pos = (pos[0] - self.rendered_text.get_width() // 2, pos[1] - self.rendered_text.get_height() // 2)

    # функция для изменения текста
    # new_text - текст на который сменится содержание объекта
    def change_text(self, new_text: str) -> None:
        self.text = new_text
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.pos = (
            self.center_pos[0] - self.rendered_text.get_width() // 2,
            self.center_pos[1] - self.rendered_text.get_height() // 2
        )

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.rendered_text, self.pos)
