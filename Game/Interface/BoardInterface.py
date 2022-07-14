from Game.Interface.InputInterface import InputInterface
from Game.Snake import Snake
from Struct.Coordinates import Coordinates


class BoardInterface:
    def __init__(self, height: int, width: int, input: InputInterface = None):
        pass

    def get_height(self) -> int:
        raise NotImplementedError()

    def get_width(self) -> int:
        raise NotImplementedError()

    def get_snake(self) -> Snake:
        raise NotImplementedError()

    def get_goal(self) -> Coordinates:
        raise NotImplementedError()
