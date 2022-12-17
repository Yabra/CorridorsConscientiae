class Camera:
    def __init__(self, pos):
        self.pos = pos

    def set_pos(self, new_pos):
        self.pos = new_pos

    def draw(self, screen, sprites):
        dx = -(self.pos[0] - screen.get_size()[0] // 2)
        dy = -(self.pos[1] - screen.get_size()[1] // 2)

        for s in sprites:
            s.rect.x += dx
            s.rect.y += dy

        sprites.draw(screen)

        for s in sprites:
            s.rect.x -= dx
            s.rect.y -= dy
