from Enum.Direction import Direction


class InputInterface:
    def __init__(self):
        pass

    def get_input(self) -> Direction|None:
        raise NotImplementedError()