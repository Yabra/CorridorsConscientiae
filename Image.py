from data_loader import load_image


# Класс изображения
class Image:
    # pos        - кортеж с 2 координатами левого верхнего угла изображения
    # image_name - имя файла с изображением
    def __init__(self, pos, image_name):
        self.pos = pos
        self.image = load_image(image_name)

    def draw(self, screen):
        screen.blit(self.image, self.pos)
