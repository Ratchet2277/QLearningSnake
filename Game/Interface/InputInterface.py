from abc import abstractmethod, ABC

from Enum.Direction import Direction


class InputInterface(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_input(self) -> Direction | None:
        raise NotImplementedError()
