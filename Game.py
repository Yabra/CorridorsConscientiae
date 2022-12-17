import sys
import pygame
from Text import Text
from Button import Button


class GameStates:
    MENU = 0
    GAME = 1


# Основной класс игры
class Game:
    def __init__(self):
        self.state = GameStates.MENU
        pygame.init()
        pygame.display.set_caption("Corridors Conscientiae")
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        # menu
        self.game_title_text = Text("Corridors Conscientiae", (400, 150), font_size=70)
        self.start_button = Button("Начать игру", (30, 400), self.start_game)
        self.exit_button = Button("Выход", (30, 480), self.exit)

    def start_game(self):
        self.state = GameStates.GAME

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))

        if self.state == GameStates.MENU:
            self.game_title_text.draw(self.screen)
            self.start_button.draw(self.screen)
            self.exit_button.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit()

                if self.state == GameStates.MENU:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.start_button.check_click(event.pos)
                        self.exit_button.check_click(event.pos)

            self.update()
            self.draw()

    def exit(self):
        pygame.quit()
        sys.exit()
