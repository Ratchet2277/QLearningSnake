from abc import ABC, abstractmethod

from Game.Interface.InputInterface import InputInterface
from Game.Snake import Snake
from Struct.Coordinates import Coordinates


class BoardInterface(ABC):

    @abstractmethod
    def __init__(self, height: int, width: int, input: InputInterface = None):
        pass

    @abstractmethod
    def get_height(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def get_width(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def get_snake(self) -> Snake:
        raise NotImplementedError()

    @abstractmethod
    def get_goal(self) -> Coordinates:
        raise NotImplementedError()
