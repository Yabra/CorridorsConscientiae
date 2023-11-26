from typing import Callable

import pygame


# типы перехода, осуществляемого в данный момент
class TransitionType:
    TO_BLACK = 0
    FROM_BLACK = 1


class StateTransition:
    transition_time = 500  # время требующееся на один этап перехода
    transition_type = TransitionType.FROM_BLACK  # тип перехода на данный момент
    time = 0  # время которое совершается переход
    func = None  # функция, вызывающаяся при окончании этапа перехода

    # обновление класса
    def update(ticks: int) -> None:
        StateTransition.time += ticks
        if StateTransition.time >= StateTransition.transition_time:
            StateTransition.time = 1000
            if StateTransition.func:
                StateTransition.func()
                StateTransition.func = None

    # отрисовка (вызов должен находиться после отрисовки всех спрайтов и т.п.)
    def draw(screen: pygame.Surface) -> None:
        surface = pygame.Surface((pygame.display.get_window_size()[0], pygame.display.get_window_size()[1]))
        surface.fill(pygame.Color(0, 0, 0))

        if StateTransition.transition_type == TransitionType.FROM_BLACK:
            surface.set_alpha(255 - int(255 / StateTransition.transition_time * StateTransition.time))

        elif StateTransition.transition_type == TransitionType.TO_BLACK:
            surface.set_alpha(int(255 / StateTransition.transition_time * StateTransition.time))

        screen.blit(surface, (0, 0))

    # функция перехода в режим затемнения
    def to_black(func: Callable[[], None]) -> None:
        StateTransition.time = 0
        StateTransition.transition_type = TransitionType.TO_BLACK
        StateTransition.func = func

    # функция перехода в режим просветления
    def from_black(func: Callable[[], None]) -> None:
        StateTransition.time = 0
        StateTransition.transition_type = TransitionType.FROM_BLACK
        StateTransition.func = func
