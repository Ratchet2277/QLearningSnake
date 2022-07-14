from abc import abstractmethod, ABC

from Game.Interface.BoardInterface import BoardInterface

class DrawerInterface(ABC):
    @abstractmethod
    def __init__(self, bord: BoardInterface):
        pass

    @abstractmethod
    def draw(self):
        raise NotImplementedError()