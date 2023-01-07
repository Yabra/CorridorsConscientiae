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


def set_sounds_volume(value):
    Settings.SOUNDS_VOLUME = value / 100


def set_music_volume(value):
    Settings.MUSIC_VOLUME = value / 100
    pygame.mixer.music.set_volume(Settings.MUSIC_VOLUME)


class Settings:
    SOUNDS_VOLUME = 1.0
    MUSIC_VOLUME = 1.0
