import sys

import Settings
from AnimatedSprite import AnimatedSprite
from Text import Text
from Button import Button
from Slider import Slider
from Scale import Scale
from ImageButton import ImageButton
from Player import Player
from Labyrinth import Labyrinth
from data_loader import load_image, load_music, load_sound, load_animation
from Settings import *
from StateTransition import StateTransition
from database import *
from labyrinth_generator import create_maze
from cheats import check_cheat_key


class GameStates:
    MENU = 0
    GAME = 1
    SETTINGS = 2
    WIN = 3


# Основной класс игры
class Game:
    def __init__(self):
        load_settings()
        self.state = GameStates.MENU
        pygame.init()
        pygame.display.set_caption("Corridors Conscientiae")
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_icon(load_image("icon.png"))

        self.db = Database()
        self.clock = pygame.time.Clock()
        self.block_buttons = False  # переменная для блокировки нажатия кнопок

        # menu
        self.game_title_text = Text("Corridors Conscientiae", (400, 150), font_size=70)
        self.start_button = Button("Начать игру", (150, 400), lambda: self.make_state_transition(self.start_game))
        self.exit_button = Button("Выход", (150, 480), self.exit)
        self.settings_button = ImageButton(
            "settings.png", (700, 500), lambda: self.make_state_transition(self.in_settings)
        )

        # game
        self.paused = False
        self.level = 0
        self.score = 0
        self.lostness = 0
        
        self.all_sprites = pygame.sprite.Group()
        self.all_items = pygame.sprite.Group()
        self.all_monsters = pygame.sprite.Group()

        self.mind_bar = Scale(
            50, 50, 30, 200,
            Player.max_mind, Player.max_mind,
            True, pygame.Color("gray"), pygame.Color("yellow"),
            self.screen
        )

        self.lostness_bar = Scale(
            550, 50, 30, 200,
            3, 0,
            False, pygame.Color("gray"), pygame.Color(150, 0, 150),
            self.screen
        )

        self.level_text = Text("", (400, 50), font_size=40)
        self.paused_text = Text("Пауза", (400, 150), font_size=70)
        self.resume_button = Button("Продолжить", (150, 400), self.resume)
        self.in_menu_button = Button("В меню", (150, 480), lambda: self.make_state_transition(self.in_menu))

        self.camera = None
        self.labyrinth = None
        self.player = None

        # settings
        self.settings_text = Text("Настройки", (400, 100), font_size=70)

        self.sounds_volume_text = Text("Громкость звуков", (150, 200), font_size=30)
        self.sounds_volume_value_text = Text("", (150, 240), font_size=40)
        self.sounds_slider = Slider(50, 265, 18, 200, 10, pygame.Color("white"), pygame.Color(0, 0, 150), self.screen)
        self.sounds_slider.set_value(int(Settings.SOUNDS_VOLUME * 100))

        self.music_volume_text = Text("Громкость музыки", (150, 320), font_size=30)
        self.music_volume_value_text = Text("", (150, 360), font_size=40)
        self.music_slider = Slider(50, 385, 18, 200, 10, pygame.Color("white"), pygame.Color(0, 0, 150), self.screen)
        self.music_slider.set_value(int(Settings.MUSIC_VOLUME * 100))

        self.clear_db_button = Button(
            "Очистить рекорды", (650, 550), self.db.delete_all_points, font_size=30
        )

        self.in_menu_from_settings_button = Button(
            "В меню", (150, 500), lambda: self.make_state_transition(self.in_menu)
        )

        # win
        self.win_text = Text("Вы прошли лабиринт сознания!", (400, 100), font_size=50)
        self.score_text = Text("Очков осознания: ", (400, 250), font_size=40)
        self.record_text = Text("Рекорд: ", (400, 350), font_size=40)
        self.wins_text = Text("Количество прохождений: ", (400, 450), font_size=40)
        self.in_menu_from_win_button = Button("В меню", (400, 550), lambda: self.make_state_transition(self.in_menu))

        # music load
        pygame.mixer.music.set_volume(Settings.MUSIC_VOLUME)
        load_music("music.ogg")

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

    def reset_game(self):
        self.state = GameStates.GAME

        self.paused = False
        self.all_sprites = pygame.sprite.Group()
        self.all_items = pygame.sprite.Group()
        self.all_monsters = pygame.sprite.Group()

        self.labyrinth = Labyrinth(
            self,
            self.all_sprites,
            self.all_items,
            self.all_monsters,
            create_maze(
                15 + 5 * self.level,
                15 + 5 * self.level,
                2 * self.level,
                6 * self.level
            )
        )

    # метод для старта игры
    def start_game(self):
        self.reset_game()
        self.level = 0
        self.score = 0
        self.lostness = 0
        # окончание плавного перехода и возвражение кнопкам кликабельности
        StateTransition.from_black(None)
        self.block_buttons = False

    def next_level(self):
        load_sound("portal.wav", 1.0).play()
        self.level += 1
        self.score += 100
        self.reset_game()
        if self.level == 7:
            self.db.add_points(self.score)
            self.state = GameStates.WIN
            self.score_text.change_text("Очков осознания: " + str(self.score))
            self.record_text.change_text("Рекорд: " + str(self.db.get_record()))
            self.wins_text.change_text("Количество прохождений: " + str(self.db.total_attempts()))
        StateTransition.from_black(None)
        self.block_buttons = False

    def previous_level(self):
        load_sound("portal.wav", 1.0).play()
        self.level -= 1
        self.score -= 100
        if self.score < 0:
            self.score = 0
        self.reset_game()
        StateTransition.from_black(None)
        self.block_buttons = False

    def add_lostness(self):
        self.lostness += 1
        self.score -= 100
        if self.score < 0:
            self.score = 0
        if self.lostness == 3:
            self.previous_level()
            self.lostness = 0

    def heal_mind(self):
        self.score += 100
        self.player.change_mind(Player.max_mind)
        load_sound("crystal.wav", 0.7).play()

    def remove_lostness(self):
        self.score += 100
        self.lostness -= 1
        if self.lostness < 0:
            self.lostness = 0
        load_sound("crystal.wav", 0.7).play()

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
            self.level_text.change_text("Уровень " + str(self.level + 1))
            if not self.paused:
                self.player.update(ticks, self.labyrinth, self.all_items)
                self.camera.move_to(
                    self.player.pos
                    +
                    pygame.math.Vector2(
                        self.player.rect.width / 2,
                        self.player.rect.height / 2
                    )
                )
                self.camera.update(ticks)
                for m in self.all_monsters:
                    m.update(ticks, self.player)
            self.mind_bar.value = self.player.mind
            self.lostness_bar.value = self.lostness
        elif self.state == GameStates.SETTINGS:
            self.sounds_slider.check()
            self.music_slider.check()
            set_sounds_volume(self.sounds_slider.value())
            set_music_volume(self.music_slider.value())
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

            self.level_text.draw(self.screen)

            self.mind_bar.draw_scale()
            self.lostness_bar.draw_scale()
            if self.paused:
                self.paused_text.draw(self.screen)
                self.resume_button.draw(self.screen)
                self.in_menu_button.draw(self.screen)

        elif self.state == GameStates.SETTINGS:
            self.settings_text.draw(self.screen)

            self.sounds_volume_text.draw(self.screen)
            self.sounds_volume_value_text.draw(self.screen)
            self.sounds_slider.draw_slider()

            self.music_volume_text.draw(self.screen)
            self.music_volume_value_text.draw(self.screen)
            self.music_slider.draw_slider()

            self.clear_db_button.draw(self.screen)

            self.in_menu_from_settings_button.draw(self.screen)

        elif self.state == GameStates.WIN:
            self.win_text.draw(self.screen)
            self.score_text.draw(self.screen)
            self.record_text.draw(self.screen)
            self.wins_text.draw(self.screen)
            self.in_menu_from_win_button.draw(self.screen)

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
                        if Settings.CHEATS:
                            check_cheat_key(self, event)
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1 and not self.block_buttons:
                            if self.paused:
                                self.resume_button.check_click(event.pos)
                                self.in_menu_button.check_click(event.pos)

                elif self.state == GameStates.SETTINGS:
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1 and not self.block_buttons:
                            self.in_menu_from_settings_button.check_click(event.pos)
                            self.clear_db_button.check_click(event.pos)

                elif self.state == GameStates.WIN:
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1 and not self.block_buttons:
                            self.in_menu_from_win_button.check_click(event.pos)

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
