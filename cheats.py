import pygame


def check_cheat_key(game, event):
    if event.mod & pygame.KMOD_CTRL:
        if event.key == pygame.K_n:
            game.next_level()
        elif event.key == pygame.K_m:
            game.heal_mind()
        elif event.key == pygame.K_l:
            game.remove_lostness()

    if event.mod & pygame.KMOD_LALT:
        if event.key == pygame.K_n:
            game.previous_level()
        elif event.key == pygame.K_l:
            game.add_lostness()
