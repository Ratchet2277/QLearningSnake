import pygame
from pygame.event import Event

from Enum.Direction import Direction
from Game.Interface.InputInterface import InputInterface


def process_key(event: Event) -> Direction | None:
    match event.key:
        case pygame.K_UP:
            return Direction.NORTH
        case pygame.K_DOWN:
            return Direction.SOUTH
        case pygame.K_LEFT:
            return Direction.WEST
        case pygame.K_RIGHT:
            return Direction.EAST
    return None


def process_events(events: list[pygame.event.Event]) -> Direction | None:
    for event in events:
        direction = process_key(event)
        if direction:
            return direction
    return None


class KeyboardInput(InputInterface):
    def __init__(self):
        super().__init__()

    def get_input(self) -> Direction|None:
        return process_events(pygame.event.get(pygame.KEYDOWN, pump=False))

