import sys

import pygame

from AnimatedSprite import AnimatedSprite
from Text import Text
from Button import Button
from Camera import Camera
from Player import Player
from Labyrinth import Labyrinth
from data_loader import load_image, load_music, load_sound, load_animation


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
        pygame.display.set_icon(load_image("test.png"))

        self.clock = pygame.time.Clock()

        # menu
        self.game_title_text = Text("Corridors Conscientiae", (400, 150), font_size=70)
        self.start_button = Button("Начать игру", (30, 400), self.start_game)
        self.exit_button = Button("Выход", (30, 480), self.exit)

        # game
        self.paused = False
        self.camera = Camera(pygame.math.Vector2(64 * 5, 64 * 5))
        self.all_sprites = pygame.sprite.Group()

        self.paused_text = Text("Пауза", (400, 150), font_size=70)
        self.resume_button = Button("Продолжить", (30, 400), self.resume)
        self.in_menu_button = Button("В меню", (30, 480), self.in_menu)

        self.labyrinth = Labyrinth(self.all_sprites, (10, 10))

        self.sprite = AnimatedSprite(load_animation("test", 5, 5))  # помещаем анимированный спрайт на локацию
        self.sprite.rect.x = 64 * 5
        self.sprite.rect.y = 64 * 5
        self.all_sprites.add(self.sprite)

        self.player = Player(self.all_sprites, pygame.math.Vector2(64 * 5, 64 * 5))

        # music load
        load_music("test_music.ogg")

    def start_game(self):
        self.paused = False
        self.state = GameStates.GAME

    def in_menu(self):
        self.state = GameStates.MENU

    def resume(self):
        self.paused = False

    def update(self, ticks):
        if self.state == GameStates.GAME:
            if not self.paused:
                self.sprite.update(ticks)
                self.player.update()
                self.camera.move_to(
                    self.player.pos
                    +
                    pygame.math.Vector2(
                        self.player.rect.width / 2,
                        self.player.rect.height / 2
                    )
                )
                self.camera.update(ticks)

    def draw(self):
        self.screen.fill((0, 0, 0))

        if self.state == GameStates.MENU:
            self.game_title_text.draw(self.screen)
            self.start_button.draw(self.screen)
            self.exit_button.draw(self.screen)

        elif self.state == GameStates.GAME:
            self.camera.draw(self.screen, self.all_sprites)

            if self.paused:
                self.paused_text.draw(self.screen)
                self.resume_button.draw(self.screen)
                self.in_menu_button.draw(self.screen)

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
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.paused = not self.paused
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        # проигрываем тестовый звук
                        load_sound("test.wav", 0.1).play()

                        self.resume_button.check_click(event.pos)
                        self.in_menu_button.check_click(event.pos)

            ticks = self.clock.tick(60)

            # music replay
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()

            self.update(ticks)
            self.draw()

    def exit(self):
        pygame.quit()
        sys.exit()
