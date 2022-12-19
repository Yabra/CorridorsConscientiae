import os
import sys

import pygame
from Animation import Animation
from Settings import Settings

loaded_images = {}
loaded_sounds = {}
loaded_fonts = {}
loaded_animations = {}


def load_image(name, colorkey=None):
    global loaded_images
    if name in loaded_images.keys():
        return loaded_images[name]

    fullname = os.path.join('data/sprites', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)

    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()

    loaded_images[name] = image

    return image


def load_music(name):
    fullname = os.path.join('data/sounds', name)
    if not os.path.isfile(fullname):
        print(f"Звуковой файл '{fullname}' не найден")
        sys.exit()

    pygame.mixer.music.load(fullname)


def load_sound(name, volume=1.0):
    global loaded_sounds
    if (name, volume * Settings.SOUNDS_VOLUME) in loaded_sounds.keys():
        return loaded_sounds[(name, volume * Settings.SOUNDS_VOLUME)]

    fullname = os.path.join('data/sounds', name)
    if not os.path.isfile(fullname):
        print(f"Звуковой файл '{fullname}' не найден")
        sys.exit()

    sound = pygame.mixer.Sound(fullname)
    sound.set_volume(volume * Settings.SOUNDS_VOLUME)
    loaded_sounds[(name, volume * Settings.SOUNDS_VOLUME)] = sound
    return sound


def load_font(name, size):
    global loaded_fonts
    if (name, size) in loaded_fonts.keys():
        return loaded_fonts[(name, size)]

    fullname = os.path.join('data/fonts', name)
    if not os.path.isfile(fullname):
        print(f"Файл шрифта '{fullname}' не найден")
        sys.exit()

    font = pygame.font.Font(fullname, size)
    loaded_fonts[(name, size)] = font
    return font


def load_animation(name, frames_count, fps):
    global loaded_animations

    frames = []
    if (name, frames_count) in loaded_animations.keys():
        frames = loaded_animations[(name, frames_count)]
    else:
        for i in range(frames_count):
            frames.append(load_image(name + "/" + str(i) + ".png"))

    return Animation(frames, fps)
