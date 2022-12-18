import random
import sys
import pygame
from data_loader import load_image, load_music, load_sound
from Text import Text
from Button import Button
from Camera import Camera
from Player import Player


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

        # game
        self.camera = Camera([0, 0])
        self.all_sprites = pygame.sprite.Group()

        self.player = Player(self.all_sprites, 0, 0)

        # music load
        load_music("test_music.ogg")

    def start_game(self):
        self.state = GameStates.GAME

    def update(self):
        if self.state == GameStates.GAME:
            self.player.update()

    def draw(self):
        self.screen.fill((0, 0, 0))

        if self.state == GameStates.MENU:
            self.game_title_text.draw(self.screen)
            self.start_button.draw(self.screen)
            self.exit_button.draw(self.screen)

        elif self.state == GameStates.GAME:
            self.camera.draw(self.screen, self.all_sprites)

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
                elif self.state == GameStates.GAME:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # проигрываем тестовый звук
                        load_sound("test.wav", 0.1).play()

            # music replay
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()

            self.update()
            self.draw()

            self.clock.tick(60)

    def exit(self):
        pygame.quit()
        sys.exit()
