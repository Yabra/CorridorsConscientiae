from data_loader import load_font


# Класс кнопки
class Text:
    # text       - оторажаемый текст
    # pos        - кортеж с 2 координатами центра текста
    # color      - цвет текста
    # font_size  - размер отображаемого текста
    def __init__(self, text, pos, color=(0, 0, 200), font_size=50):
        self.text = text
        self.color = color
        self.font_size = font_size
        self.center_pos = pos

        self.font = load_font("test.ttf", self.font_size)
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.pos = (pos[0] - self.rendered_text.get_width() // 2, pos[1] - self.rendered_text.get_height() // 2)

    def change_text(self, new_text):
        self.text = new_text
        self.rendered_text = self.font.render(self.text, True, self.color)
        self.pos = (
            self.center_pos[0] - self.rendered_text.get_width() // 2,
            self.center_pos[1] - self.rendered_text.get_height() // 2
        )

    def draw(self, screen):
        screen.blit(self.rendered_text, self.pos)
