import pygame


def check_cheat_key(game, event):
    if event.mod & pygame.KMOD_CTRL:
        if event.key == pygame.K_l:
            game.next_level()
        elif event.key == pygame.K_z:
            game.heal_mind()
        elif event.key == pygame.K_x:
            game.remove_lostness()
        elif event.key == pygame.K_m:
            game.minimap = not game.minimap

    if event.mod & pygame.KMOD_LALT:
        if event.key == pygame.K_l:
            game.previous_level()
        elif event.key == pygame.K_x:
            game.add_lostness()
