import pygame


def save_settings():
    settings_file = open("data/settings", "w")
    settings_file.write(str(Settings.SOUNDS_VOLUME) + "\n")
    settings_file.write(str(Settings.MUSIC_VOLUME) + "\n")
    settings_file.close()


def load_settings():
    try:
        settings_file = open("data/settings", "r")
        Settings.SOUNDS_VOLUME = float(settings_file.readline())
        Settings.MUSIC_VOLUME = float(settings_file.readline())
        settings_file.close()

    except ValueError:
        Settings.SOUNDS_VOLUME = 1.0
        Settings.MUSIC_VOLUME = 1.0

    except FileNotFoundError:
        Settings.SOUNDS_VOLUME = 1.0
        Settings.MUSIC_VOLUME = 1.0

    finally:
        save_settings()


def add_sounds_volume():
    Settings.SOUNDS_VOLUME += 0.1
    if Settings.SOUNDS_VOLUME > 1:
        Settings.SOUNDS_VOLUME = 1


def sub_sounds_volume():
    Settings.SOUNDS_VOLUME -= 0.1
    if Settings.SOUNDS_VOLUME < 0:
        Settings.SOUNDS_VOLUME = 0


def add_music_volume():
    Settings.MUSIC_VOLUME += 0.1
    if Settings.MUSIC_VOLUME > 1:
        Settings.MUSIC_VOLUME = 1
    pygame.mixer.music.set_volume(Settings.MUSIC_VOLUME)


def sub_music_volume():
    Settings.MUSIC_VOLUME -= 0.1
    if Settings.MUSIC_VOLUME < 0:
        Settings.MUSIC_VOLUME = 0
    pygame.mixer.music.set_volume(Settings.MUSIC_VOLUME)


class Settings:
    SOUNDS_VOLUME = 1.0
    MUSIC_VOLUME = 1.0