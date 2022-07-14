from Game.Interface.BoardInterface import BoardInterface


class DrawerInterface:
    def __init__(self, bord: BoardInterface):
        pass

    def draw(self):
        raise NotImplementedError()