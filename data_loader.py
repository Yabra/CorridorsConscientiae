import os
import sys
import pygame

loaded_images = {}
loaded_sounds = {}


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
    if name in loaded_sounds.keys():
        return loaded_sounds[name]

    fullname = os.path.join('data/sounds', name)
    if not os.path.isfile(fullname):
        print(f"Звуковой файл '{fullname}' не найден")
        sys.exit()

    sound = pygame.mixer.Sound(fullname)
    sound.set_volume(volume)
    loaded_sounds[name] = sound
    return sound

