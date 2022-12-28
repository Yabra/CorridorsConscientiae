import sys

from AnimatedSprite import AnimatedSprite
from Text import Text
from Button import Button
from ImageButton import ImageButton
from Camera import Camera
from Player import Player
from Labyrinth import Labyrinth
from data_loader import load_image, load_music, load_sound, load_animation
from Settings import *
from StateTransition import StateTransition


class GameStates:
    MENU = 0
    GAME = 1
    SETTINGS = 2


# Основной класс игры
class Game:
    def __init__(self):
        load_settings()
        self.state = GameStates.MENU
        pygame.init()
        pygame.display.set_caption("Corridors Conscientiae")
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_icon(load_image("test.png"))

        self.clock = pygame.time.Clock()
        self.block_buttons = False  # переменная для блокировки нажатия кнопок

        # menu
        self.game_title_text = Text("Corridors Conscientiae", (400, 150), font_size=70)
        self.start_button = Button("Начать игру", (150, 400), lambda: self.make_state_transition(self.start_game))
        self.exit_button = Button("Выход", (150, 480), self.exit)
        self.settings_button = ImageButton("obj.png", (700, 500), lambda: self.make_state_transition(self.in_settings))

        # game
        self.paused = False
        self.camera = Camera(pygame.math.Vector2(64 * 5, 64 * 5))
        self.all_sprites = pygame.sprite.Group()

        self.paused_text = Text("Пауза", (400, 150), font_size=70)
        self.resume_button = Button("Продолжить", (150, 400), self.resume)
        self.in_menu_button = Button("В меню", (150, 480), lambda: self.make_state_transition(self.in_menu))

        self.labyrinth = Labyrinth(self.all_sprites, (10, 10))

        self.sprite = AnimatedSprite(load_animation("test", 5, 5))  # помещаем анимированный спрайт на локацию
        self.sprite.rect.x = 64 * 5
        self.sprite.rect.y = 64 * 5
        self.all_sprites.add(self.sprite)

        self.player = Player(self.all_sprites, pygame.math.Vector2(64 * 5, 64 * 5))

        # settings
        self.settings_text = Text("Настройки", (400, 100), font_size=70)

        self.sounds_volume_text = Text("Громкость звуков", (400, 250), font_size=30)
        self.sounds_volume_value_text = Text("", (400, 300), font_size=50)
        self.sub_sounds_volume_button = Button("-", (320, 290), sub_sounds_volume, font_size=70)
        self.add_sounds_volume_button = Button("+", (480, 290), add_sounds_volume, font_size=70)

        self.music_volume_text = Text("Громкость музыки", (400, 350), font_size=30)
        self.music_volume_value_text = Text("", (400, 400), font_size=50)
        self.sub_music_volume_button = Button("-", (320, 390), sub_music_volume, font_size=70)
        self.add_music_volume_button = Button("+", (480, 390), add_music_volume, font_size=70)

        self.in_menu_from_settings_button = Button("В меню", (400, 500), lambda: self.make_state_transition(self.in_menu))

        # music load
        load_music("test_music.ogg")

    # метод для начала плавного перехода между состояниями игры
    def make_state_transition(self, func):
        StateTransition.to_black(func)
        self.block_buttons = True

    # метод перехода в меню
    def in_menu(self):
        self.state = GameStates.MENU

        # окончание плавного перехода и возвражение кнопкам кликабельности
        StateTransition.from_black(None)
        self.block_buttons = False

    # метод для старта игры
    def start_game(self):
        self.state = GameStates.GAME

        self.paused = False
        self.camera = Camera(pygame.math.Vector2(64 * 5, 64 * 5))
        self.all_sprites = pygame.sprite.Group()

        self.labyrinth = Labyrinth(self.all_sprites, (10, 10))

        self.sprite = AnimatedSprite(load_animation("test", 5, 5))  # помещаем анимированный спрайт на локацию
        self.sprite.rect.x = 64 * 5
        self.sprite.rect.y = 64 * 5
        self.all_sprites.add(self.sprite)

        self.player = Player(self.all_sprites, pygame.math.Vector2(64 * 5, 64 * 5))

        # окончание плавного перехода и возвражение кнопкам кликабельности
        StateTransition.from_black(None)
        self.block_buttons = False

    # метод перехода в настройки
    def in_settings(self):
        self.state = GameStates.SETTINGS

        # окончание плавного перехода и возвражение кнопкам кликабельности
        StateTransition.from_black(None)
        self.block_buttons = False

    # метод снятия игры с паузы
    def resume(self):
        self.paused = False

    def update(self, ticks):
        if self.state == GameStates.MENU:
            pass
        elif self.state == GameStates.GAME:
            if not self.paused:
                self.sprite.update(ticks)
                self.player.update(self.labyrinth)
                self.camera.move_to(
                    self.player.pos
                    +
                    pygame.math.Vector2(
                        self.player.rect.width / 2,
                        self.player.rect.height / 2
                    )
                )
                self.camera.update(ticks)
        elif self.state == GameStates.SETTINGS:
            self.sounds_volume_value_text.change_text(str(int(Settings.SOUNDS_VOLUME * 100)) + "%")
            self.music_volume_value_text.change_text(str(int(Settings.MUSIC_VOLUME * 100)) + "%")

        # обновление плавного перехода
        StateTransition.update(ticks)

    def draw(self):
        self.screen.fill((0, 0, 0))

        if self.state == GameStates.MENU:
            self.game_title_text.draw(self.screen)
            self.start_button.draw(self.screen)
            self.settings_button.draw(self.screen)
            self.exit_button.draw(self.screen)

        elif self.state == GameStates.GAME:
            self.camera.draw(self.screen, self.all_sprites)

            if self.paused:
                self.paused_text.draw(self.screen)
                self.resume_button.draw(self.screen)
                self.in_menu_button.draw(self.screen)

        elif self.state == GameStates.SETTINGS:
            self.settings_text.draw(self.screen)

            self.sounds_volume_text.draw(self.screen)
            self.sounds_volume_value_text.draw(self.screen)
            self.sub_sounds_volume_button.draw(self.screen)
            self.add_sounds_volume_button.draw(self.screen)

            self.music_volume_text.draw(self.screen)
            self.music_volume_value_text.draw(self.screen)
            self.sub_music_volume_button.draw(self.screen)
            self.add_music_volume_button.draw(self.screen)

            self.in_menu_from_settings_button.draw(self.screen)

        # отрисовка плавного перехода
        StateTransition.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # обработка закрытия оккна крестиком
                    self.exit()

                # орбработка нажатий клавиш клавиатуры и кликов
                if self.state == GameStates.MENU:
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1 and not self.block_buttons:
                            self.start_button.check_click(event.pos)
                            self.settings_button.check_click(event.pos)
                            self.exit_button.check_click(event.pos)
                elif self.state == GameStates.GAME:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.paused = not self.paused
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1 and not self.block_buttons:
                            load_sound("test.wav", 0.1).play()  # проигрываем тестовый звук
                            if self.paused:
                                self.resume_button.check_click(event.pos)
                                self.in_menu_button.check_click(event.pos)
                elif self.state == GameStates.SETTINGS:
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1 and not self.block_buttons:
                            self.sub_sounds_volume_button.check_click(event.pos)
                            self.add_sounds_volume_button.check_click(event.pos)
                            self.sub_music_volume_button.check_click(event.pos)
                            self.add_music_volume_button.check_click(event.pos)
                            self.in_menu_from_settings_button.check_click(event.pos)

            ticks = self.clock.tick(60)

            # music replay
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()

            self.update(ticks)
            self.draw()

    def exit(self):
        pygame.quit()
        save_settings()
        sys.exit()
